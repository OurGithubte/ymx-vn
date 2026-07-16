import { NextResponse } from "next/server";
import { z } from "zod";
import { requireStaff } from "@/lib/supabase/server";

const schema=z.object({status:z.enum(["draft","published","closed","archived"])});

export async function PATCH(request:Request,{params}:{params:Promise<{id:string}>}){
  const staff=await requireStaff();
  if(!staff||!["admin","hr"].includes(staff.profile.role)) return NextResponse.json({error:"Unauthorized"},{status:401});
  const parsed=schema.safeParse(await request.json());
  if(!parsed.success) return NextResponse.json({error:"Invalid job status"},{status:400});
  const {id}=await params;
  const updates={status:parsed.data.status,published_at:parsed.data.status==="published"?new Date().toISOString():null,updated_at:new Date().toISOString()};
  const {data,error}=await staff.client.from("jobs").update(updates).eq("id",id).select().single();
  if(error) return NextResponse.json({error:error.message},{status:400});
  return NextResponse.json({job:data});
}
