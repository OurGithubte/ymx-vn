import { notFound } from "next/navigation";
import { BriefcaseBusiness, Clock3, MapPin } from "lucide-react";
import { ApplicationForm } from "@/components/ApplicationForm";
import { isLocale, t } from "@/lib/i18n";
import { getPublishedJobs } from "@/lib/recruitment";
import { pc } from "@/lib/public-copy";

export const dynamic = "force-dynamic";
export default async function JobDetail({params}:{params:Promise<{lang:string;slug:string}>}){const {lang,slug}=await params;if(!isLocale(lang))notFound();const jobs=await getPublishedJobs();const job=jobs.find(item=>item.slug===slug);if(!job)notFound();const c=t(lang),p=pc(lang);return <main><section className="job-hero"><div className="container"><span className="job-dept"><BriefcaseBusiness size={16}/>{job.department}</span><h1>{job.title[lang]}</h1><p>{job.summary[lang]}</p><div className="job-meta"><span><MapPin size={17}/>{job.location}</span><span><Clock3 size={17}/>{job.employmentType}</span></div><a className="button primary" href="#apply">{c.apply}</a></div></section><section className="section"><div className="container job-detail"><article className="prose"><h2>{p.responsibilities}</h2><ul>{job.responsibilities[lang].map(x=><li key={x}>{x}</li>)}</ul><h2>{p.requirements}</h2><ul>{job.requirements[lang].map(x=><li key={x}>{x}</li>)}</ul><h2>{p.expect}</h2><p>{p.expectText}</p></article><aside id="apply"><h2>{c.apply}</h2><p>{p.completeForm}</p><ApplicationForm jobId={job.id} locale={lang}/></aside></div></section></main>}
