import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "YMX Vietnam Electronic Technology", template: "%s | YMX Vietnam" },
  description: "Precision die-cutting manufacturer for advanced electronic materials in Vietnam.",
  icons: {
    icon: [
      { url: "/assets/favicon.svg", type: "image/svg+xml" },
      { url: "/assets/favicon-32x32.png", sizes: "32x32", type: "image/png" },
      { url: "/assets/favicon-16x16.png", sizes: "16x16", type: "image/png" },
    ],
    apple: "/assets/apple-touch-icon.png",
  },
  manifest: "/site.webmanifest",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="vi"><body>{children}</body></html>;
}
