import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  poweredByHeader: false,
  images: {
    formats: ["image/avif", "image/webp"],
  },
  async headers() {
    const csp = [
      "default-src 'self'",
      "script-src 'self' 'unsafe-inline'",
      "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
      "font-src 'self' https://fonts.gstatic.com data:",
      "img-src 'self' data: blob:",
      "connect-src 'self' https://*.supabase.co",
      "frame-src https://www.google.com",
      "object-src 'none'",
      "base-uri 'self'",
      "form-action 'self'",
      "frame-ancestors 'none'",
      "upgrade-insecure-requests",
    ].join("; ");
    return [{ source:"/(.*)", headers:[
      { key:"Content-Security-Policy", value:csp },
      { key:"Referrer-Policy", value:"strict-origin-when-cross-origin" },
      { key:"X-Content-Type-Options", value:"nosniff" },
      { key:"X-Frame-Options", value:"DENY" },
      { key:"Permissions-Policy", value:"camera=(), microphone=(), geolocation=()" },
      { key:"Strict-Transport-Security", value:"max-age=31536000" },
    ] }];
  },
};

export default nextConfig;
