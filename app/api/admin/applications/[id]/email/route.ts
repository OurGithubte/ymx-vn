import { NextResponse } from "next/server";
import { Resend } from "resend";
import { z } from "zod";
import { candidateStatusEmail } from "@/lib/email-templates";
import { requireStaff } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";

const schema=z.object({type:z.enum(["interview","rejected","offered"]),interviewAt:z.string().max(40).optional(),location:z.string().max(500).optional(),note:z.string().max(1000).optional()}).superRefine((value,context)=>{if(value.type==="interview"&&(!value.interviewAt||!Number.isFinite(Date.parse(value.interviewAt))))context.addIssue({code:"custom",path:["interviewAt"],message:"Interview date and time are required."});if(value.type==="interview"&&!value.location?.trim())context.addIssue({code:"custom",path:["location"],message:"Interview location is required."})});

export async function POST(request:Request,{params}:{params:Promise<{id:string}>}){
  const staff=await requireStaff();if(!staff||!["admin","hr"].includes(staff.profile.role))return NextResponse.json({error:"Unauthorized"},{status:401});
  if(!process.env.RESEND_API_KEY||!process.env.RECRUITMENT_FROM_EMAIL)return NextResponse.json({error:"Email service not configured"},{status:503});
  const parsed=schema.safeParse(await request.json());if(!parsed.success)return NextResponse.json({error:parsed.error.issues[0]?.message||"Invalid template"},{status:400});
  const admin=createAdminClient();if(!admin)return NextResponse.json({error:"Recruitment service not configured"},{status:503});
  const {id}=await params;const {data:app}=await admin.from("applications").select("full_name,email,job_title,locale,status").eq("id",id).single();if(!app)return NextResponse.json({error:"Candidate not found"},{status:404});
  const template=candidateStatusEmail({locale:app.locale,type:parsed.data.type,name:app.full_name,job:app.job_title,interviewAt:parsed.data.interviewAt,location:parsed.data.location,note:parsed.data.note});
  const resend=new Resend(process.env.RESEND_API_KEY);const {data,error}=await resend.emails.send({from:process.env.RECRUITMENT_FROM_EMAIL,to:app.email,...template});if(error)return NextResponse.json({error:error.message},{status:400});
  const nextStatus=parsed.data.type==="interview"?"interview":parsed.data.type==="offered"?"offered":"rejected";
  const [logResult,updateResult,eventResult]=await Promise.all([admin.from("email_logs").insert({application_id:id,template_key:parsed.data.type,recipient:app.email,provider_id:data?.id,status:"sent",sent_by:staff.user.id}),admin.from("applications").update({status:nextStatus,updated_at:new Date().toISOString()}).eq("id",id),admin.from("application_events").insert({application_id:id,actor_id:staff.user.id,event_type:"email_sent",from_status:app.status,to_status:nextStatus,note:`Template: ${parsed.data.type}`})]);
  if(logResult.error||updateResult.error||eventResult.error)console.error("email_audit_write_failed",{log:logResult.error?.message,update:updateResult.error?.message,event:eventResult.error?.message});
  return NextResponse.json({ok:true,status:nextStatus});
}
