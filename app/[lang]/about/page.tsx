import { PageHero } from "@/components/PageHero";
import { isLocale, t } from "@/lib/i18n";
import { notFound } from "next/navigation";
import { pc } from "@/lib/public-copy";

export default async function About({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params; if (!isLocale(lang)) notFound(); const c = t(lang),p=pc(lang);
  return <main><PageHero kicker={c.about} title={c.about} text={c.aboutText}/><section className="section"><div className="container content-grid"><article className="prose"><h2>YMX Vietnam Electronic Technology</h2><p>{c.aboutText}</p>{p.aboutParas.map(text=><p key={text}>{text}</p>)}</article><aside className="info-panel"><h3>{p.profile}</h3><dl><div><dt>{p.businessId}</dt><dd>3604072330</dd></div><div><dt>{p.factory}</dt><dd>Tam Phuoc Industrial Park, Dong Nai</dd></div><div><dt>{p.capacity}</dt><dd>10,000,000 products / year</dd></div><div><dt>{p.facility}</dt><dd>1,484 m²</dd></div></dl></aside></div></section></main>;
}
