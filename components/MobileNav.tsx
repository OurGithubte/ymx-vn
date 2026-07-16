"use client";
import { Menu, X } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

export function MobileNav({ items }: { items: { href: string; label: string }[] }) {
  const [open, setOpen] = useState(false);
  const pathname=usePathname();
  return <>
    <button className="menu-toggle" aria-label={open ? "Close menu" : "Open menu"} aria-expanded={open} onClick={() => setOpen(!open)}>{open ? <X /> : <Menu />}</button>
    <div className={`mobile-menu ${open ? "open" : ""}`}>{items.map(item => <Link className={pathname===item.href||pathname.startsWith(`${item.href}/`)?"active":""} key={item.href} href={item.href} onClick={() => setOpen(false)}>{item.label}</Link>)}</div>
  </>;
}
