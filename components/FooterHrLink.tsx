"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { KeyRound, ShieldCheck } from "lucide-react";
import { createBrowserClient } from "@supabase/ssr";

const STAFF_ROLES = ["admin", "hr", "interviewer"];

/**
 * Public-footer link for recruitment staff.
 * - Default (no session, or session without a staff profile): links to /admin/login.
 * - Valid Supabase session + profiles.role in (admin, hr, interviewer): links to /admin.
 * Uses the public anon key only (client-side), matching AdminLoginForm. No service-role
 * key or secret is used here; /admin remains protected server-side by proxy.ts + requireStaff().
 */
export function FooterHrLink({ loginLabel, portalLabel }: { loginLabel: string; portalLabel: string }) {
  const [isStaff, setIsStaff] = useState(false);

  useEffect(() => {
    let active = true;
    const url = process.env.NEXT_PUBLIC_SUPABASE_URL, key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
    if (!url || !key) return;
    const client = createBrowserClient(url, key);
    (async () => {
      const { data: { session } } = await client.auth.getSession();
      const user = session?.user;
      if (!user || !active) return;
      const { data: profile } = await client.from("profiles").select("role").eq("id", user.id).single();
      if (active && profile && STAFF_ROLES.includes(profile.role)) setIsStaff(true);
    })();
    return () => { active = false; };
  }, []);

  if (isStaff) return <Link href="/admin"><ShieldCheck size={17}/>{portalLabel}</Link>;
  return <Link href="/admin/login"><KeyRound size={17}/>{loginLabel}</Link>;
}
