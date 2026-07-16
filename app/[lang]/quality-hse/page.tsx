import { PageHero } from "@/components/PageHero";
import { isLocale, t } from "@/lib/i18n";
import { BadgeCheck, HardHat, Recycle, ShieldCheck } from "lucide-react";
import { notFound } from "next/navigation";
import { pc } from "@/lib/public-copy";
export default async function Quality({ params }: { params: Promise<{ lang: string }> }) { const { lang } = await params; if (!isLocale(lang)) notFound(); const c=t(lang),p=pc(lang); const items=[[BadgeCheck,"IQC / IPQC / OQC"],[ShieldCheck,"CAPA & 8D"],[HardHat,"PPE & Risk control"],[Recycle,"Environmental compliance"]] as const; return <main><PageHero kicker={p.qualityKicker} title={c.quality} text={p.qualityLead}/><section className="section"><div className="container quality-grid">{items.map(([Icon,title])=><article key={title}><Icon/><h2>{title}</h2><p>{p.qualityDesc}</p></article>)}</div></section></main>; }
