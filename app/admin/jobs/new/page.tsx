import { redirect } from "next/navigation";
import { requireStaff } from "@/lib/supabase/server";
import { JobForm } from "@/components/admin/JobForm";
import type { Metadata } from "next";

export const metadata: Metadata = { title: "Tạo tin tuyển dụng — YMX Recruitment Admin", robots: { index: false, follow: false, nocache: true } };
export const dynamic = "force-dynamic";

export default async function NewJobPage() {
  const staff = await requireStaff();
  if (!staff) redirect("/admin/login");
  if (!["admin", "hr"].includes(staff.profile.role)) redirect("/admin");
  return (
    <main className="admin-shell admin-shell-form">
      <JobForm mode="create" />
    </main>
  );
}
