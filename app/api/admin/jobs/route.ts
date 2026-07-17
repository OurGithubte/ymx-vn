import { NextResponse } from "next/server";
import { requireStaff } from "@/lib/supabase/server";
import { jobInputSchema } from "@/lib/job-schema";
import { mapJobRow } from "@/lib/jobs";

export async function POST(request: Request) {
  const staff = await requireStaff();
  if (!staff || !["admin", "hr"].includes(staff.profile.role)) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  const parsed = jobInputSchema.safeParse(await request.json());
  if (!parsed.success) return NextResponse.json({ error: parsed.error.issues[0]?.message || "Dữ liệu không hợp lệ." }, { status: 400 });
  const x = parsed.data;

  if (x.status === "published" && !x.title.vi.trim()) {
    return NextResponse.json({ error: "Cần nhập tên vị trí bằng Tiếng Việt trước khi đăng tuyển." }, { status: 400 });
  }

  const row = {
    id: crypto.randomUUID(),
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
    published_at: x.status === "published" ? new Date(x.publishedAt || Date.now()).toISOString() : null,
    created_by: staff.user.id,
  };

  const { data, error } = await staff.client.from("jobs").insert(row).select().single();
  if (error) {
    const message = error.code === "23505" ? "Slug này đã được sử dụng, vui lòng chọn slug khác." : error.message;
    return NextResponse.json({ error: message }, { status: 400 });
  }
  return NextResponse.json({ job: mapJobRow(data) }, { status: 201 });
}
