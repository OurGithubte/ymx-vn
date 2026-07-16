"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
export function DesktopNav({items}:{items:{href:string;label:string}[]}){const pathname=usePathname();return <nav className="desktop-nav" aria-label="Main navigation">{items.map(item=>{const active=item.href.split("/").filter(Boolean).length===1?pathname===item.href:pathname.startsWith(item.href);return <Link className={active?"active":""} key={item.href} href={item.href}>{item.label}</Link>})}</nav>}
