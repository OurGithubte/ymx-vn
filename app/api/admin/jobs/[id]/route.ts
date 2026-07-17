import { NextResponse } from "next/server";
import { z } from "zod";
import { requireStaff } from "@/lib/supabase/server";
import { jobInputSchema } from "@/lib/job-schema";
import { mapJobRow } from "@/lib/jobs";

const quickStatusSchema = z.object({ status: z.enum(["draft", "published", "closed", "archived"]) });

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const staff = await requireStaff();
  if (!staff || !["admin", "hr"].includes(staff.profile.role)) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const { id } = await params;
  const body = await request.json();

  // Quick action from the job table (Đóng tin / Lưu trữ / re-publish): only { status } is sent.
  const isQuickAction = Object.keys(body).length === 1 && "status" in body;

  if (isQuickAction) {
    const parsed = quickStatusSchema.safeParse(body);
    if (!parsed.success) return NextResponse.json({ error: "Trạng thái không hợp lệ." }, { status: 400 });
    const { data: current } = await staff.client.from("jobs").select("published_at").eq("id", id).single();
    const updates = {
      status: parsed.data.status,
      published_at: parsed.data.status === "published" ? (current?.published_at || new Date().toISOString()) : null,
      updated_at: new Date().toISOString(),
    };
    const { data, error } = await staff.client.from("jobs").update(updates).eq("id", id).select().single();
    if (error) return NextResponse.json({ error: error.message }, { status: 400 });
    return NextResponse.json({ job: mapJobRow(data) });
  }

  const parsed = jobInputSchema.safeParse(body);
  if (!parsed.success) return NextResponse.json({ error: parsed.error.issues[0]?.message || "Dữ liệu không hợp lệ." }, { status: 400 });
  const x = parsed.data;

  if (x.status === "published" && !x.title.vi.trim()) {
    return NextResponse.json({ error: "Cần nhập tên vị trí bằng Tiếng Việt trước khi đăng tuyển." }, { status: 400 });
  }

  const { data: current } = await staff.client.from("jobs").select("published_at").eq("id", id).single();
  const updates = {
    slug: x.slug,
    department: x.department,
    location: x.location,
    employment_type: x.employmentType,
    vacancies: x.vacancies,
    level: x.level || null,
    salary_text: x.salaryText || null,
    application_deadline: x.applicationDeadline || null,
    title: x.title,
    summary: x.summary,
    responsibilities: x.responsibilities,
    requirements: x.requirements,
    benefits: x.benefits,
    status: x.status,
    published_at: x.status === "published" ? new Date(x.publishedAt || current?.published_at || Date.now()).toISOString() : null,
    updated_at: new Date().toISOString(),
  };

  const { data, error } = await staff.client.from("jobs").update(updates).eq("id", id).select().single();
  if (error) {
    const message = error.code === "23505" ? "Slug này đã được sử dụng, vui lòng chọn slug khác." : error.message;
    return NextResponse.json({ error: message }, { status: 400 });
  }
  return NextResponse.json({ job: mapJobRow(data) });
}
