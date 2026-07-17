import type { Locale } from "./i18n";

export type LocaleText = Record<Locale, string>;
export type JobStatus = "draft" | "published" | "closed" | "archived";

export type Job = {
  id: string;
  slug: string;
  title: LocaleText;
  department: string;
  location: string;
  employmentType: string;
  summary: LocaleText;
  /** Plain multi-line text per locale; each non-empty line renders as one bullet. Also accepts legacy string[] rows created before this field existed. */
  responsibilities: Record<Locale, string | string[]>;
  requirements: Record<Locale, string | string[]>;
  benefits: LocaleText;
  publishedAt: string;
  status?: JobStatus;
  createdAt?: string;
  vacancies?: number;
  level?: string | null;
  salaryText?: string | null;
  applicationDeadline?: string | null;
};

/**
 * Map a raw Supabase `jobs` row (selected with `select("*")`, so this works
 * whether or not migration 0002_job_posting_fields.sql has run yet) into the
 * client-facing Job shape. Every new column falls back to a safe default so
 * older rows (including the two seeded sample jobs) never crash the UI.
 */
export function mapJobRow(row: Record<string, unknown>): Job {
  const emptyRichField: Record<Locale, string | string[]> = { vi: "", en: "", zh: "" };
  const emptyLocaleText: LocaleText = { vi: "", en: "", zh: "" };
  return {
    id: String(row.id),
    slug: String(row.slug),
    department: String(row.department),
    location: String(row.location),
    employmentType: String(row.employment_type || "Full-time"),
    title: (row.title as LocaleText) || emptyLocaleText,
    summary: (row.summary as LocaleText) || emptyLocaleText,
    responsibilities: (row.responsibilities as Record<Locale, string | string[]>) || emptyRichField,
    requirements: (row.requirements as Record<Locale, string | string[]>) || emptyRichField,
    benefits: (row.benefits as LocaleText) || emptyLocaleText,
    publishedAt: (row.published_at as string) || (row.created_at as string) || new Date().toISOString(),
    status: (row.status as JobStatus) || "draft",
    createdAt: row.created_at as string | undefined,
    vacancies: typeof row.vacancies === "number" ? row.vacancies : 1,
    level: (row.level as string | null) ?? null,
    salaryText: (row.salary_text as string | null) ?? null,
    applicationDeadline: (row.application_deadline as string | null) ?? null,
  };
}

export const sampleJobs: Job[] = [
  {
    id: "quality-engineer", slug: "quality-engineer", department: "Quality", location: "Đồng Nai", employmentType: "Full-time", publishedAt: "2026-07-15",
    title: { vi: "Kỹ sư Chất lượng", en: "Quality Engineer", zh: "质量工程师" },
    summary: { vi: "Kiểm soát chất lượng sản phẩm cắt bế và phối hợp cải tiến quy trình cùng các bộ phận sản xuất.", en: "Own die-cut product quality and coordinate cross-functional process improvement.", zh: "负责模切产品质量并协调生产部门持续改进流程。" },
    responsibilities: { vi: "Theo dõi IQC/IPQC/OQC\nPhân tích lỗi và thực hiện CAPA/8D\nQuản lý hồ sơ đo lường", en: "Monitor IQC/IPQC/OQC\nLead defect analysis and CAPA/8D\nMaintain measurement records", zh: "跟进IQC/IPQC/OQC\n执行缺陷分析及CAPA/8D\n维护测量记录" },
    requirements: { vi: "Tốt nghiệp kỹ thuật\nCó kinh nghiệm QA/QC sản xuất\nTư duy dữ liệu và giao tiếp tốt", en: "Engineering degree\nManufacturing QA/QC experience\nStrong analytical communication", zh: "工程相关专业\n制造业QA/QC经验\n良好的分析与沟通能力" },
    benefits: { vi: "", en: "", zh: "" },
    status: "published", vacancies: 1,
  },
  {
    id: "production-technician", slug: "production-technician", department: "Production", location: "Đồng Nai", employmentType: "Full-time", publishedAt: "2026-07-12",
    title: { vi: "Kỹ thuật viên Sản xuất", en: "Production Technician", zh: "生产技术员" },
    summary: { vi: "Vận hành, kiểm tra và bảo dưỡng cơ bản dây chuyền cắt cuộn, cắt bế và cán màng.", en: "Operate, inspect and perform basic maintenance on slitting, die-cutting and laminating lines.", zh: "操作、检查并基础维护分切、模切及覆膜设备。" },
    responsibilities: { vi: "Vận hành máy theo PWI\nKiểm tra thông số đầu ca\nGhi nhận sản lượng và bất thường", en: "Operate machines to PWI\nVerify shift-start parameters\nRecord output and abnormalities", zh: "按PWI操作设备\n确认开班参数\n记录产量及异常" },
    requirements: { vi: "Trung cấp kỹ thuật trở lên\nLàm việc theo ca\nCẩn thận và tuân thủ an toàn", en: "Technical diploma or above\nAvailable for shift work\nSafety-focused and detail-oriented", zh: "中专或以上技术学历\n可接受倒班\n注重细节并遵守安全规范" },
    benefits: { vi: "", en: "", zh: "" },
    status: "published", vacancies: 2,
  },
];
