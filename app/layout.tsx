import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "YMX Vietnam Electronic Technology", template: "%s | YMX Vietnam" },
  description: "Precision die-cutting manufacturer for advanced electronic materials in Vietnam.",
  icons: { icon: "/assets/favicon.svg" },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="vi"><body>{children}</body></html>;
}
