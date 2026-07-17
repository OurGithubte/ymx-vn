"use client";
import { ToastProvider } from "./Toast";

/** Client wrapper so /admin/* server components can still use the toast system. */
export function AdminChrome({ children }: { children: React.ReactNode }) {
  return <ToastProvider>{children}</ToastProvider>;
}
