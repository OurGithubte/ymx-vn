import Image from "next/image";
import { PageHero } from "@/components/PageHero";
import { isLocale, t } from "@/lib/i18n";
import { notFound } from "next/navigation";
import { pc, productNames } from "@/lib/public-copy";

const products = [
  ["printer", "foam.png"], ["mobile", "graphite.png"], ["notebook", "thermal-conductive-sheet.png"],
  ["backlight", "reflective-sheet.png"], ["automobile", "felt.png"], ["other", "special-tape.png"],
];
export default async function Products({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params; if (!isLocale(lang)) notFound(); const c = t(lang),p=pc(lang);
  return <main><PageHero kicker={c.capabilities} title={c.products} text={p.productLead}/><section className="section"><div className="container card-grid">{products.map(([slug,image],index) => <article className="media-card" key={slug}><div className="media"><Image fill sizes="(max-width: 768px) 100vw, 33vw" src={`/assets/products/${slug}/${image}`} alt={productNames[lang][index]}/></div><div><span>YMX</span><h2>{productNames[lang][index]}</h2><p>{p.productDesc}</p></div></article>)}</div></section></main>;
}
