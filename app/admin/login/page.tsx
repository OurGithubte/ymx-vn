import { AdminLoginForm } from "@/components/AdminLoginForm";
import { redirect } from "next/navigation";
import { requireStaff } from "@/lib/supabase/server";
export default async function AdminLogin(){const staff=await requireStaff();if(staff)redirect("/admin");return <main className="admin-login"><section><div className="logo-mark">YMX</div><span className="eyebrow blue">Recruitment operations</span><h1>HR workspace</h1><p>Secure access for authorized YMX recruitment staff.</p><AdminLoginForm/></section></main>}
