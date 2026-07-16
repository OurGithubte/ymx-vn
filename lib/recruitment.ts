import { createAdminClient } from "./supabase/admin";
import { sampleJobs, type Job } from "./jobs";

export async function getPublishedJobs(): Promise<Job[]> {
  const client=createAdminClient(); if(!client) return sampleJobs;
  const {data,error}=await client.from("jobs").select("id,slug,department,location,employment_type,title,summary,responsibilities,requirements,published_at").eq("status","published").order("published_at",{ascending:false});
  if(error){console.error("published_jobs_load_failed",error.message);return []}
  if(!data?.length) return [];
  return data.map(row=>({id:row.id,slug:row.slug,department:row.department,location:row.location,employmentType:row.employment_type,title:row.title,summary:row.summary,responsibilities:row.responsibilities,requirements:row.requirements,publishedAt:row.published_at||new Date().toISOString()})) as Job[];
}
