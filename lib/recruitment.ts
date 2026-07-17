import { createAdminClient } from "./supabase/admin";
import { sampleJobs, mapJobRow, type Job } from "./jobs";

/** select("*") on purpose: works whether or not migration 0002 has run yet — extra columns just come back as undefined and mapJobRow() fills in safe defaults. */
export async function getPublishedJobs(): Promise<Job[]> {
  const client = createAdminClient();
  if (!client) return sampleJobs;
  const { data, error } = await client.from("jobs").select("*").eq("status", "published").order("published_at", { ascending: false });
  if (error) { console.error("published_jobs_load_failed", error.message); return []; }
  if (!data?.length) return [];
  return data.map(mapJobRow);
}

export async function getPublishedJobBySlug(slug: string): Promise<Job | null> {
  const jobs = await getPublishedJobs();
  return jobs.find(job => job.slug === slug) || null;
}
