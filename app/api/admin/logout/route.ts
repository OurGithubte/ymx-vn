import { NextResponse } from "next/server";
import { createUserClient } from "@/lib/supabase/server";

export async function POST(){
  const client=await createUserClient();
  if(client)await client.auth.signOut();
  return NextResponse.json({ok:true});
}
