import { notFound, redirect } from "next/navigation";
import { requireStaff } from "@/lib/supabase/server";
import { JobForm } from "@/components/admin/JobForm";
import { mapJobRow } from "@/lib/jobs";
import type { Metadata } from "next";

export const metadata: Metadata = { title: "Sửa tin tuyển dụng — YMX Recruitment Admin", robots: { index: false, follow: false, nocache: true } };
export const dynamic = "force-dynamic";

export default async function EditJobPage({ params }: { params: Promise<{ id: string }> }) {
  const staff = await requireStaff();
  if (!staff) redirect("/admin/login");
  if (!["admin", "hr"].includes(staff.profile.role)) redirect("/admin");
  const { id } = await params;
  const { data, error } = await staff.client.from("jobs").select("*").eq("id", id).single();
  if (error || !data) notFound();
  return (
    <main className="admin-shell admin-shell-form">
      <JobForm mode="edit" job={mapJobRow(data)} jobId={id} />
    </main>
  );
}
