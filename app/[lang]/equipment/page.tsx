import Image from "next/image";
import { PageHero } from "@/components/PageHero";
import { isLocale, t } from "@/lib/i18n";
import { notFound } from "next/navigation";
import { equipmentNames, pc } from "@/lib/public-copy";

const machines = ["xe-ranh","cat-cuon","cat-khuon","can-mang","can-mang-new","vmm","luc-keo"];
export default async function Equipment({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params; if (!isLocale(lang)) notFound(); const c = t(lang),p=pc(lang);
  return <main><PageHero kicker={c.capabilities} title={c.equipment} text={p.equipmentLead}/><section className="section"><div className="container card-grid equipment-grid">{machines.map((slug,index) => <article className="media-card" key={slug}><div className="media"><Image fill sizes="(max-width: 768px) 100vw, 33vw" src={`/assets/equipment/${slug}/hero.jpg`} alt={equipmentNames[lang][index]}/></div><div><span>YMX</span><h2>{equipmentNames[lang][index]}</h2><p>{p.equipmentDesc}</p></div></article>)}</div></section></main>;
}
