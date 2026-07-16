import { PageHero } from "@/components/PageHero";
import { isLocale, t } from "@/lib/i18n";
import { Mail, MapPin, Phone } from "lucide-react";
import { notFound } from "next/navigation";
import { pc } from "@/lib/public-copy";
export default async function Contact({ params }: { params: Promise<{ lang: string }> }) { const {lang}=await params;if(!isLocale(lang))notFound();const c=t(lang),p=pc(lang); return <main><PageHero kicker={c.contact} title={c.contact} text={p.contactLead}/><section className="section"><div className="container contact-layout"><div className="contact-panel"><div><MapPin/><span><strong>{p.factoryAddress}</strong>Workshop 3A, Lot 33, Tam Phuoc Industrial Park, Dong Nai, Vietnam</span></div><div><Mail/><span><strong>Email</strong>steven@ljdzsz.com</span></div><div><Phone/><span><strong>{p.phone}</strong>{p.phoneHelp}</span></div></div><div className="map"><iframe title="YMX Vietnam factory map" loading="lazy" src="https://www.google.com/maps?q=C%C3%94NG+TY+TNHH+ELECTRONIC+TECHNOLOGY+YMX+VI%E1%BB%86T+NAM&output=embed"/></div></div></section></main>; }
