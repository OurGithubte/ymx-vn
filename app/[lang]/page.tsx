import Link from "next/link";
import { ArrowRight, BadgeCheck, Factory, Globe2, Layers3, ShieldCheck } from "lucide-react";
import { isLocale, t } from "@/lib/i18n";
import { notFound } from "next/navigation";

export default async function Home({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params; if (!isLocale(lang)) notFound(); const c = t(lang);
  return <main>
    <section className="hero"><div className="container hero-grid"><div className="hero-copy"><span className="eyebrow">{c.heroKicker}</span><h1>{c.heroTitle}</h1><p>{c.heroText}</p><div className="button-row"><Link className="button primary" href={`/${lang}/products`}>{c.explore}<ArrowRight size={18}/></Link><Link className="button ghost" href={`/${lang}/careers`}>{c.careers}</Link></div></div><div className="hero-visual" aria-hidden="true"><div className="precision-ring"><span>±0.1</span><small>mm precision</small></div><div className="tech-card card-a"><Layers3/><span>Die-cutting</span></div><div className="tech-card card-b"><ShieldCheck/><span>Quality assured</span></div></div></div><div className="container stats"><div><strong>2013</strong><span>Group established</span></div><div><strong>6</strong><span>Global factories</span></div><div><strong>10M</strong><span>Products / year</span></div><div><strong>1,484 m²</strong><span>Dong Nai facility</span></div></div></section>
    <section className="section"><div className="container split"><div><span className="eyebrow blue">{c.about}</span><h2>{c.about}</h2></div><div><p className="lead">{c.aboutText}</p><Link className="text-link" href={`/${lang}/about`}>{c.explore}<ArrowRight size={17}/></Link></div></div></section>
    <section className="section soft"><div className="container"><div className="section-heading"><span className="eyebrow blue">{c.valuesTitle}</span><h2>{c.valuesTitle}</h2></div><div className="value-grid">{c.values.map((value, i) => <article key={value}><span>0{i + 1}</span>{[<BadgeCheck key="a"/>, <ShieldCheck key="b"/>, <Globe2 key="c"/>, <Factory key="d"/>][i]}<h3>{value}</h3></article>)}</div></div></section>
    <section className="section"><div className="container callout"><div><span className="eyebrow">{c.jobs}</span><h2>{c.jobsLead}</h2></div><Link className="button light" href={`/${lang}/careers`}>{c.openRoles}<ArrowRight size={18}/></Link></div></section>
  </main>;
}
