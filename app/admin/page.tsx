import { redirect } from "next/navigation";
import { requireStaff } from "@/lib/supabase/server";
import { AdminWorkspace } from "@/components/AdminWorkspace";

export const dynamic="force-dynamic";
export default async function AdminDashboard(){const staff=await requireStaff();if(!staff)redirect("/admin/login");const [{data:jobs},{data:applications}]=await Promise.all([staff.client.from("jobs").select("id,slug,department,location,employment_type,title,status,published_at").order("created_at",{ascending:false}),staff.client.from("applications").select("id,job_id,job_title,full_name,email,phone,experience_years,status,rating,hr_notes,created_at,cv_path").order("created_at",{ascending:false}).limit(200)]);return <AdminWorkspace profile={staff.profile} jobs={jobs||[]} applications={applications||[]}/>}
