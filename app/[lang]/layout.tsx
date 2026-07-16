import { notFound } from "next/navigation";
import { isLocale } from "@/lib/i18n";
import { SiteShell } from "@/components/SiteShell";

export function generateStaticParams() { return ["vi", "en", "zh"].map(lang => ({ lang })); }

export default async function LocaleLayout({ children, params }: { children: React.ReactNode; params: Promise<{ lang: string }> }) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  return <SiteShell locale={lang}>{children}</SiteShell>;
}
