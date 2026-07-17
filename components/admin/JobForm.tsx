"use client";
import { useMemo, useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { LoaderCircle, Eye, Save, Send, X } from "lucide-react";
import type { Job } from "@/lib/jobs";
import { slugify, STATUS_LABELS, type JobInput } from "@/lib/job-schema";
import { arrayToRichText } from "@/lib/rich-text";
import { useToast } from "./Toast";
import { ConfirmDialog } from "./ConfirmDialog";

const LOCALE_TABS = [
  { key: "vi", label: "Tiếng Việt" },
  { key: "en", label: "English" },
  { key: "zh", label: "中文" },
] as const;

const STATUS_OPTIONS = ["draft", "published", "closed"] as const;

function emptyForm(): JobInput {
  return {
    slug: "", department: "", location: "Đồng Nai", employmentType: "Toàn thời gian",
    vacancies: 1, level: "", salaryText: "", applicationDeadline: "", publishedAt: "",
    title: { vi: "", en: "", zh: "" }, summary: { vi: "", en: "", zh: "" },
    responsibilities: { vi: "", en: "", zh: "" }, requirements: { vi: "", en: "", zh: "" },
    benefits: { vi: "", en: "", zh: "" },
    status: "draft",
  };
}

function jobToForm(job: Job): JobInput {
  return {
    slug: job.slug, department: job.department, location: job.location,
    employmentType: job.employmentType, vacancies: job.vacancies ?? 1, level: job.level || "",
    salaryText: job.salaryText || "", applicationDeadline: job.applicationDeadline || "",
    publishedAt: job.publishedAt ? job.publishedAt.slice(0, 10) : "",
    title: { vi: job.title.vi || "", en: job.title.en || "", zh: job.title.zh || "" },
    summary: { vi: job.summary.vi || "", en: job.summary.en || "", zh: job.summary.zh || "" },
    responsibilities: { vi: arrayToRichText(job.responsibilities.vi), en: arrayToRichText(job.responsibilities.en), zh: arrayToRichText(job.responsibilities.zh) },
    requirements: { vi: arrayToRichText(job.requirements.vi), en: arrayToRichText(job.requirements.en), zh: arrayToRichText(job.requirements.zh) },
    benefits: { vi: job.benefits?.vi || "", en: job.benefits?.en || "", zh: job.benefits?.zh || "" },
    status: job.status || "draft",
  };
}

export function JobForm({ mode, job, jobId }: { mode: "create" | "edit"; job?: Job; jobId?: string }) {
  const router = useRouter();
  const { notify } = useToast();
  const [form, setForm] = useState<JobInput>(() => (job ? jobToForm(job) : emptyForm()));
  const [activeLocale, setActiveLocale] = useState<"vi" | "en" | "zh">("vi");
  const [slugTouched, setSlugTouched] = useState(mode === "edit");
  const [dirty, setDirty] = useState(false);
  const [saving, setSaving] = useState<"" | "save" | "publish" | "preview">("");
  const [confirmCancel, setConfirmCancel] = useState(false);

  useEffect(() => {
    function handler(e: BeforeUnloadEvent) { if (dirty) { e.preventDefault(); e.returnValue = ""; } }
    window.addEventListener("beforeunload", handler);
    return () => window.removeEventListener("beforeunload", handler);
  }, [dirty]);

  function update<K extends keyof JobInput>(key: K, value: JobInput[K]) {
    setForm(prev => ({ ...prev, [key]: value }));
    setDirty(true);
  }

  function updateLocaleField(field: "title" | "summary" | "responsibilities" | "requirements" | "benefits", locale: "vi" | "en" | "zh", value: string) {
    setForm(prev => ({ ...prev, [field]: { ...prev[field], [locale]: value } }));
    setDirty(true);
    if (field === "title" && locale === "vi" && !slugTouched) {
      setForm(prev => ({ ...prev, title: { ...prev.title, vi: value }, slug: slugify(value) }));
    }
  }

  const viTitleFilled = useMemo(() => Boolean(form.title.vi.trim()), [form.title.vi]);

  async function persist(status: JobInput["status"], redirect: "dashboard" | "preview") {
    if (status === "published" && !viTitleFilled) {
      notify("Cần nhập tên vị trí bằng Tiếng Việt trước khi đăng tuyển.", "error");
      return;
    }
    setSaving(redirect === "preview" ? "preview" : status === "published" ? "publish" : "save");
    try {
      const payload = { ...form, status };
      const endpoint = mode === "create" ? "/api/admin/jobs" : `/api/admin/jobs/${jobId}`;
      const method = mode === "create" ? "POST" : "PATCH";
      const response = await fetch(endpoint, { method, headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Không thể lưu tin tuyển dụng.");
      setForm(prev => ({ ...prev, status }));
      setDirty(false);
      const savedId = result.job?.id || jobId;
      notify(status === "published" ? "Đã đăng tuyển thành công." : "Đã lưu tin tuyển dụng.", "success");
      if (redirect === "preview" && savedId) router.push(`/admin/jobs/${savedId}/preview`);
      else router.push("/admin");
    } catch (error) {
      notify(error instanceof Error ? error.message : "Có lỗi xảy ra, vui lòng thử lại.", "error");
    } finally {
      setSaving("");
    }
  }

  function handleCancel() {
    if (dirty) setConfirmCancel(true);
    else router.push("/admin");
  }

  return (
    <div className="job-form-page">
      <header className="job-form-header">
        <div>
          <Link href="/admin" className="text-link back-link">← Quay lại danh sách</Link>
          <h1>{mode === "create" ? "Tạo tin tuyển dụng" : `Sửa tin: ${form.title.vi || form.title.en || form.title.zh || "…"}`}</h1>
        </div>
      </header>

      <section className="form-card">
        <h2>Thông tin cơ bản</h2>
        <div className="form-grid">
          <label>Tên vị trí (Tiếng Việt)<input value={form.title.vi} onChange={e => updateLocaleField("title", "vi", e.target.value)} placeholder="VD: Kỹ sư Chất lượng" required /></label>
          <label>Slug (đường dẫn)
            <input value={form.slug} onChange={e => { setSlugTouched(true); update("slug", slugify(e.target.value)); }} pattern="[a-z0-9-]+" required />
          </label>
          <label>Phòng ban<input value={form.department} onChange={e => update("department", e.target.value)} required /></label>
          <label>Địa điểm<input value={form.location} onChange={e => update("location", e.target.value)} required /></label>
          <label>Hình thức làm việc<input value={form.employmentType} onChange={e => update("employmentType", e.target.value)} placeholder="VD: Toàn thời gian" required /></label>
          <label>Số lượng tuyển<input type="number" min={1} value={form.vacancies} onChange={e => update("vacancies", Number(e.target.value) || 1)} /></label>
          <label>Cấp bậc<input value={form.level} onChange={e => update("level", e.target.value)} placeholder="VD: Nhân viên, Trưởng nhóm…" /></label>
          <label>Mức lương<input value={form.salaryText} onChange={e => update("salaryText", e.target.value)} placeholder="VD: Thỏa thuận, hoặc 10-15 triệu/tháng" /></label>
          <label>Hạn nộp hồ sơ<input type="date" value={form.applicationDeadline} onChange={e => update("applicationDeadline", e.target.value)} /></label>
          <label>Trạng thái
            <select value={form.status} onChange={e => update("status", e.target.value as JobInput["status"])}>
              {STATUS_OPTIONS.map(opt => <option key={opt} value={opt}>{STATUS_LABELS[opt]}</option>)}
            </select>
          </label>
        </div>
      </section>

      <section className="form-card">
        <h2>Nội dung đa ngôn ngữ</h2>
        <div className="locale-tabs" role="tablist">
          {LOCALE_TABS.map(tab => (
            <button type="button" key={tab.key} role="tab" aria-selected={activeLocale === tab.key} className={activeLocale === tab.key ? "active" : ""} onClick={() => setActiveLocale(tab.key)}>
              {tab.label}
            </button>
          ))}
        </div>
        <div className="locale-tab-panel">
          <label>Tóm tắt vị trí<textarea rows={3} value={form.summary[activeLocale]} onChange={e => updateLocaleField("summary", activeLocale, e.target.value)} /></label>
          <label>Mô tả công việc <span className="field-hint">(mỗi dòng là một gạch đầu dòng)</span>
            <textarea rows={6} value={form.responsibilities[activeLocale]} onChange={e => updateLocaleField("responsibilities", activeLocale, e.target.value)} />
          </label>
          <label>Yêu cầu công việc <span className="field-hint">(mỗi dòng là một gạch đầu dòng)</span>
            <textarea rows={6} value={form.requirements[activeLocale]} onChange={e => updateLocaleField("requirements", activeLocale, e.target.value)} />
          </label>
          <label>Quyền lợi <span className="field-hint">(mỗi dòng là một gạch đầu dòng)</span>
            <textarea rows={4} value={form.benefits[activeLocale]} onChange={e => updateLocaleField("benefits", activeLocale, e.target.value)} />
          </label>
        </div>
      </section>

      <div className="job-action-bar">
        <button type="button" className="button" onClick={handleCancel}><X size={16} />Hủy</button>
        <div className="job-action-bar-main">
          <button type="button" className="button" disabled={!!saving} onClick={() => persist(form.status === "published" ? "published" : "draft", "preview")}>
            {saving === "preview" ? <LoaderCircle className="spin" size={16} /> : <Eye size={16} />}Xem trước
          </button>
          <button type="button" className="button" disabled={!!saving} onClick={() => persist(form.status, "dashboard")}>
            {saving === "save" ? <LoaderCircle className="spin" size={16} /> : <Save size={16} />}Lưu nháp
          </button>
          <button type="button" className="button primary" disabled={!!saving} onClick={() => persist("published", "dashboard")}>
            {saving === "publish" ? <LoaderCircle className="spin" size={16} /> : <Send size={16} />}Đăng tuyển
          </button>
        </div>
      </div>

      <ConfirmDialog
        open={confirmCancel}
        title="Hủy thay đổi?"
        message="Dữ liệu chưa lưu sẽ bị mất. Bạn có chắc chắn muốn rời khỏi trang này?"
        confirmLabel="Rời khỏi trang"
        danger
        onConfirm={() => router.push("/admin")}
        onCancel={() => setConfirmCancel(false)}
      />
    </div>
  );
}
