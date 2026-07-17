import Link from "next/link";
import { ArrowRight, BriefcaseBusiness, Clock3, MapPin } from "lucide-react";
import { PageHero } from "@/components/PageHero";
import { isLocale, t } from "@/lib/i18n";
import { getPublishedJobs } from "@/lib/recruitment";
import { notFound } from "next/navigation";
import { pc } from "@/lib/public-copy";
import { pickText } from "@/lib/locale-fallback";

export const dynamic = "force-dynamic";

export default async function Careers({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  const c = t(lang), p = pc(lang);
  const jobs = await getPublishedJobs();
  return (
    <main>
      <PageHero kicker="YMX" title={c.jobs} text={c.jobsLead} />
      <section className="section">
        <div className="container jobs-layout">
          <aside><span className="eyebrow blue">{c.openRoles}</span><h2>{jobs.length} {c.openRoles}</h2><p>{p.careerProcess}</p></aside>
          <div className="job-list">
            {jobs.map(job => (
              <Link className="job-card" key={job.id} href={`/${lang}/careers/${job.slug}`}>
                <div>
                  <span className="job-dept"><BriefcaseBusiness size={16} />{job.department}</span>
                  <h2>{pickText(job.title, lang)}</h2>
                  <p>{pickText(job.summary, lang)}</p>
                  <div className="job-meta">
                    <span><MapPin size={16} />{job.location}</span>
                    <span><Clock3 size={16} />{job.employmentType}</span>
                    {job.salaryText?.trim() && <span>{job.salaryText}</span>}
                  </div>
                </div>
                <ArrowRight className="job-arrow" />
              </Link>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
