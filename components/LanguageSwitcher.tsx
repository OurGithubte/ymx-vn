"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import type { Locale } from "@/lib/i18n";
import { switchLocalePath } from "@/lib/i18n";
export function LanguageSwitcher({locale}:{locale:Locale}){const pathname=usePathname();return <div className="language-switch">{(["vi","en","zh"] as const).map(lang=><Link className={locale===lang?"active":""} key={lang} href={switchLocalePath(pathname,lang)}>{lang==="zh"?"中文":lang.toUpperCase()}</Link>)}</div>}
