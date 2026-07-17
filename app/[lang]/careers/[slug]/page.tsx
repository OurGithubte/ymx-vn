import { notFound } from "next/navigation";
import { isLocale } from "@/lib/i18n";
import { getPublishedJobBySlug } from "@/lib/recruitment";
import { JobDetailView } from "@/components/JobDetailView";

export const dynamic = "force-dynamic";

export default async function JobDetail({ params }: { params: Promise<{ lang: string; slug: string }> }) {
  const { lang, slug } = await params;
  if (!isLocale(lang)) notFound();
  const job = await getPublishedJobBySlug(slug);
  if (!job) notFound();
  return <JobDetailView job={job} locale={lang} mode="public" />;
}
