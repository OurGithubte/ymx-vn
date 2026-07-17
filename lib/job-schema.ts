import { z } from "zod";

/** Status labels shown on the admin job table and the form's status field. */
export const STATUS_LABELS: Record<string, string> = { draft: "Bản nháp", published: "Đang tuyển", closed: "Đã đóng", archived: "Lưu trữ" };

export function slugify(input: string): string {
  return input
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/đ/gi, "d")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

const localeText = z.object({ vi: z.string(), en: z.string(), zh: z.string() });

/** Full job payload as sent by the admin job form (create & edit share this shape). MVP scope only. */
export const jobInputSchema = z.object({
  slug: z.string().regex(/^[a-z0-9-]+$/, "Slug chỉ gồm chữ thường, số và dấu gạch ngang"),
  department: z.string().min(2, "Vui lòng nhập phòng ban"),
  location: z.string().min(2, "Vui lòng nhập địa điểm"),
  employmentType: z.string().min(2, "Vui lòng nhập hình thức làm việc"),
  vacancies: z.coerce.number().int().min(1).max(999).default(1),
  level: z.string().max(80).optional().default(""),
  salaryText: z.string().max(200).optional().default(""),
  applicationDeadline: z.string().max(20).optional().default(""),
  publishedAt: z.string().max(20).optional().default(""),

  title: localeText,
  summary: localeText,
  responsibilities: localeText,
  requirements: localeText,
  benefits: localeText,

  status: z.enum(["draft", "published", "closed", "archived"]).default("draft"),
});

export type JobInput = z.infer<typeof jobInputSchema>;
