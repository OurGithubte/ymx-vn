import { notFound, redirect } from "next/navigation";
import { requireStaff } from "@/lib/supabase/server";
import { mapJobRow } from "@/lib/jobs";
import { JobDetailView } from "@/components/JobDetailView";
import { PreviewActions } from "@/components/admin/PreviewActions";
import type { Metadata } from "next";

export const metadata: Metadata = { title: "Xem trước tin tuyển dụng — YMX Recruitment Admin", robots: { index: false, follow: false, nocache: true } };
export const dynamic = "force-dynamic";

export default async function JobPreviewPage({ params }: { params: Promise<{ id: string }> }) {
  const staff = await requireStaff();
  if (!staff) redirect("/admin/login");
  const { id } = await params;
  const { data, error } = await staff.client.from("jobs").select("*").eq("id", id).single();
  if (error || !data) notFound();
  const job = mapJobRow(data);
  return (
    <div className="admin-preview-shell">
      <PreviewActions jobId={id} status={job.status || "draft"} />
      <JobDetailView job={job} locale="vi" mode="preview" />
    </div>
  );
}
