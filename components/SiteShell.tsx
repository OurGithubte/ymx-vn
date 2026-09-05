import Link from "next/link";
import { BriefcaseBusiness, Mail, MapPin } from "lucide-react";
import type { Locale } from "@/lib/i18n";
import { t } from "@/lib/i18n";
import { MobileNav } from "./MobileNav";
import { DesktopNav } from "./DesktopNav";
import { LanguageSwitcher } from "./LanguageSwitcher";
import { FooterHrLink } from "./FooterHrLink";

const paths = ["", "about", "products", "equipment", "quality-hse", "careers", "contact"];

export function SiteShell({ locale, children }: { locale: Locale; children: React.ReactNode }) {
  const c = t(locale);
  const items = c.nav.map((label, i) => ({ label, href: `/${locale}${paths[i] ? `/${paths[i]}` : ""}` }));
  return <div className="site-shell">
    <header className="site-header"><div className="container header-inner">
      <Link className="brand" href={`/${locale}`}><img src="/assets/logo.png" alt="YMX" className="logo-img"/><span><strong>YMX VIETNAM</strong><small>ELECTRONIC TECHNOLOGY</small></span></Link>
      <DesktopNav items={items}/>
      <div className="header-actions"><LanguageSwitcher locale={locale}/><MobileNav items={items} /></div>
    </div></header>
    {children}
    <footer><div className="container footer-grid"><div><div className="brand footer-brand"><img src="/assets/logo.png" alt="YMX" className="logo-img"/><span><strong>YMX VIETNAM</strong><small>ELECTRONIC TECHNOLOGY CO., LTD</small></span></div><p>Precision materials. Reliable partnership.</p></div><div><h3>{c.contact}</h3><p><MapPin size={17}/> Workshop 3A, Lot 33, Tam Phuoc Industrial Park, Dong Nai</p><p><Mail size={17}/> steven@ljdzsz.com</p></div><div><h3>{c.jobs}</h3><Link href={`/${locale}/careers`}><BriefcaseBusiness size={17}/>{c.openRoles}</Link><Link href={`/${locale}/privacy`}>Privacy</Link><FooterHrLink loginLabel={c.footerHrLogin} portalLabel={c.footerAdminPortal}/></div></div><div className="container footer-bottom">© 2026 YMX Vietnam Electronic Technology Company Limited.</div></footer>
  </div>;
}
