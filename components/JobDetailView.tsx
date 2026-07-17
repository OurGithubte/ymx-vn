import { Banknote, BriefcaseBusiness, CalendarClock, MapPin } from "lucide-react";
import type { Job } from "@/lib/jobs";
import type { Locale } from "@/lib/i18n";
import { pc } from "@/lib/public-copy";
import { t } from "@/lib/i18n";
import { pickText, pickRich } from "@/lib/locale-fallback";
import { RichTextView } from "./RichTextView";
import { ApplicationForm } from "./ApplicationForm";

export function JobDetailView({ job, locale, mode = "public" }: { job: Job; locale: Locale; mode?: "public" | "preview" }) {
  const p = pc(locale);
  const title = pickText(job.title, locale);
  const summary = pickText(job.summary, locale);
  const description = pickRich(job.responsibilities, locale);
  const requirements = pickRich(job.requirements, locale);
  const benefits = pickRich(job.benefits, locale);
  const isPreview = mode === "preview";
  const dateFormat = locale === "vi" ? "vi-VN" : locale === "zh" ? "zh-CN" : "en-US";

  return (
    <main>
      {isPreview && (
        <div className="preview-banner">
          <span>{p.previewBanner}</span>
        </div>
      )}
      <section className="job-hero">
        <div className="container">
          <span className="job-dept"><BriefcaseBusiness size={16} />{job.department}</span>
          <h1>{title}</h1>
          <p>{summary}</p>
          <div className="job-highlight-grid">
            <div><Banknote size={17} /><span>{p.salary}</span><strong>{job.salaryText?.trim() || p.negotiable}</strong></div>
            <div><MapPin size={17} /><span>{p.workplace}</span><strong>{job.location}</strong></div>
            <div><CalendarClock size={17} /><span>{p.deadline}</span><strong>{job.applicationDeadline ? new Date(job.applicationDeadline).toLocaleDateString(dateFormat) : p.noDeadline}</strong></div>
          </div>
          {!isPreview && <a className="button primary" href="#apply">{t(locale).apply}</a>}
          {isPreview && <span className="button primary disabled-preview">{t(locale).apply}</span>}
        </div>
      </section>

      <section className="section">
        <div className="container job-detail">
          <article className="prose">
            <h2>{p.responsibilities}</h2>
            <RichTextView value={description} />
            <h2>{p.requirements}</h2>
            <RichTextView value={requirements} />
            {benefits && (Array.isArray(benefits) ? benefits.length > 0 : benefits.trim()) && (<><h2>{p.benefits}</h2><RichTextView value={benefits} /></>)}
          </article>

          <aside id="apply">
            <h2>{t(locale).apply}</h2>
            {isPreview ? (
              <p className="preview-form-placeholder">{p.completeForm}</p>
            ) : (
              <>
                <p>{p.completeForm}</p>
                <ApplicationForm jobId={job.id} locale={locale} />
              </>
            )}
          </aside>
        </div>
      </section>
    </main>
  );
}
