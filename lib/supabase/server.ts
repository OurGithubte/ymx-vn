import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

export async function createUserClient() {
  const url=process.env.NEXT_PUBLIC_SUPABASE_URL, key=process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if(!url||!key) return null;
  const store=await cookies();
  return createServerClient(url,key,{cookies:{getAll(){return store.getAll()},setAll(values){try{values.forEach(({name,value,options})=>store.set(name,value,options))}catch{}}}});
}

export async function requireStaff() {
  const client=await createUserClient(); if(!client) return null;
  const {data:{user}}=await client.auth.getUser(); if(!user) return null;
  const {data:profile}=await client.from("profiles").select("id,full_name,role").eq("id",user.id).single();
  if(!profile) return null;
  return {client,user,profile};
}
