import { NextResponse } from "next/server";
import { z } from "zod";
import { Resend } from "resend";
import { createAdminClient } from "@/lib/supabase/admin";
import { applicationReceived, escapeHtml, safeSubject } from "@/lib/email-templates";

export const runtime = "nodejs";
const schema = z.object({ jobId:z.string().min(2).max(100), fullName:z.string().min(2).max(120), email:z.email(), phone:z.string().min(6).max(30), experienceYears:z.coerce.number().min(0).max(50).optional(), coverNote:z.string().max(2000).optional(), locale:z.enum(["vi","en","zh"]).default("vi") });
const allowed = new Set(["application/pdf","application/vnd.openxmlformats-officedocument.wordprocessingml.document","application/msword"]);

export async function POST(request: Request) {
  try {
    if(!request.headers.get("content-type")?.toLowerCase().includes("multipart/form-data")) return NextResponse.json({error:"Expected a multipart form submission."},{status:415});
    const form = await request.formData();
    if (String(form.get("website")||"")) return NextResponse.json({ok:true},{status:201});
    if (form.get("consent") !== "on") return NextResponse.json({error:"Consent is required."},{status:400});
    const parsed=schema.safeParse(Object.fromEntries([...form.entries()].filter(([,v])=>typeof v==="string")));
    if(!parsed.success) return NextResponse.json({error:parsed.error.issues[0]?.message||"Invalid application."},{status:400});
    const cv=form.get("cv"); if(!(cv instanceof File)||cv.size===0) return NextResponse.json({error:"CV is required."},{status:400});
    if(cv.size>5*1024*1024||!allowed.has(cv.type)) return NextResponse.json({error:"CV must be a PDF or DOCX file up to 5 MB."},{status:400});
    const bytes=Buffer.from(await cv.arrayBuffer()); const isPdf=bytes.subarray(0,4).toString()==="%PDF"; const isOfficeZip=bytes[0]===0x50&&bytes[1]===0x4b; const isLegacyDoc=bytes.subarray(0,8).equals(Buffer.from([0xd0,0xcf,0x11,0xe0,0xa1,0xb1,0x1a,0xe1]));
    if(!isPdf&&!isOfficeZip&&!isLegacyDoc) return NextResponse.json({error:"The uploaded file is not a valid PDF or Word document."},{status:400});
    const supabase=createAdminClient(); if(!supabase) return NextResponse.json({error:"Recruitment service is being configured. Please email your CV to our recruitment team."},{status:503});
    const {data:job,error:jobError}=await supabase.from("jobs").select("id,title").eq("id",parsed.data.jobId).eq("status","published").single();
    if(jobError||!job) return NextResponse.json({error:"This position is no longer accepting applications."},{status:404});
    const titles=job.title as Partial<Record<"vi"|"en"|"zh",string>>;const jobTitle=titles[parsed.data.locale]||titles.vi||titles.en||titles.zh;
    if(!jobTitle) return NextResponse.json({error:"This position is not configured correctly."},{status:500});
    const duplicateSince=new Date(Date.now()-10*60*1000).toISOString(); const {data:duplicate}=await supabase.from("applications").select("id").eq("job_id",parsed.data.jobId).eq("email",parsed.data.email.toLowerCase()).gte("created_at",duplicateSince).limit(1);
    if(duplicate?.length) return NextResponse.json({error:"An application with this email was submitted recently. Please wait before trying again."},{status:429});
    const id=crypto.randomUUID(); const extension=cv.name.split(".").pop()?.toLowerCase()||"pdf"; const path=`${parsed.data.jobId}/${id}.${extension}`;
    const upload=await supabase.storage.from("candidate-cvs").upload(path,bytes,{contentType:cv.type,upsert:false});
    if(upload.error) throw upload.error;
    const inserted=await supabase.from("applications").insert({id,job_id:parsed.data.jobId,job_title:jobTitle,full_name:parsed.data.fullName,email:parsed.data.email.toLowerCase(),phone:parsed.data.phone,experience_years:parsed.data.experienceYears??null,cover_note:parsed.data.coverNote||null,cv_path:path,locale:parsed.data.locale,status:"new",consent_at:new Date().toISOString()});
    if(inserted.error){await supabase.storage.from("candidate-cvs").remove([path]);throw inserted.error;}
    if(process.env.RESEND_API_KEY&&process.env.RECRUITMENT_FROM_EMAIL){
      const resend=new Resend(process.env.RESEND_API_KEY);const confirmation=applicationReceived(parsed.data.locale,parsed.data.fullName,jobTitle);
      try{const {data,error}=await resend.emails.send({from:process.env.RECRUITMENT_FROM_EMAIL,to:parsed.data.email,...confirmation});await supabase.from("email_logs").insert({application_id:id,template_key:"application_received",recipient:parsed.data.email,provider_id:data?.id||null,status:error?"failed":"sent"});if(error)console.error("application_confirmation_failed",error.message)}catch(error){console.error("application_confirmation_failed",error)}
      if(process.env.HR_NOTIFICATION_EMAIL){try{const {data,error}=await resend.emails.send({from:process.env.RECRUITMENT_FROM_EMAIL,to:process.env.HR_NOTIFICATION_EMAIL,subject:`New candidate – ${safeSubject(jobTitle)}`,html:`<p>${escapeHtml(parsed.data.fullName)} has submitted an application for ${escapeHtml(jobTitle)}.</p>`});await supabase.from("email_logs").insert({application_id:id,template_key:"hr_new_application",recipient:process.env.HR_NOTIFICATION_EMAIL,provider_id:data?.id||null,status:error?"failed":"sent"});if(error)console.error("hr_notification_failed",error.message)}catch(error){console.error("hr_notification_failed",error)}}
    }
    return NextResponse.json({ok:true,id},{status:201});
  } catch(error){console.error("application_submit_failed",error);return NextResponse.json({error:"We could not submit your application. Please try again."},{status:500});}
}
