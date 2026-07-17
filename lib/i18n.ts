export const locales = ["vi", "en", "zh"] as const;
export type Locale = (typeof locales)[number];

export function isLocale(value: string): value is Locale {
  return locales.includes(value as Locale);
}

const copy = {
  vi: {
    nav: ["Trang chủ", "Giới thiệu", "Sản phẩm", "Thiết bị", "Chất lượng & HSE", "Cơ hội việc làm", "Liên hệ"],
    heroKicker: "Precision die-cutting manufacturer",
    heroTitle: "Kiến tạo độ chính xác cho ngành điện tử hiện đại",
    heroText: "YMX Việt Nam sản xuất và gia công cắt bế vật liệu điện tử công nghệ cao cho điện thoại, máy tính, ô tô và thiết bị điện – điện tử toàn cầu.",
    explore: "Khám phá năng lực", careers: "Gia nhập YMX", about: "Về YMX Việt Nam",
    aboutText: "Thành viên tại Việt Nam của hệ thống YMX/Lingjiang Electronics, với nền tảng sản xuất chuyên sâu từ năm 2013 và nhà máy tại KCN Tam Phước, Đồng Nai.",
    valuesTitle: "Bốn cam kết tạo nên YMX", values: ["Chính trực", "Chất lượng", "Dịch vụ", "Phát triển"],
    capabilities: "Năng lực cốt lõi", products: "Sản phẩm & ứng dụng", equipment: "Thiết bị sản xuất & kiểm tra",
    quality: "Chất lượng & HSE", contact: "Liên hệ hợp tác", jobs: "Cơ hội việc làm", jobsLead: "Cùng YMX xây dựng một môi trường sản xuất chính xác, an toàn và bền vững.",
    viewJob: "Xem vị trí", apply: "Ứng tuyển ngay", openRoles: "Vị trí đang tuyển", noJobs: "Hiện chưa có vị trí phù hợp. Vui lòng quay lại sau.",
    footerHrLogin: "Nhân sự đăng nhập", footerAdminPortal: "Trang quản trị",
  },
  en: {
    nav: ["Home", "About", "Products", "Equipment", "Quality & HSE", "Careers", "Contact"],
    heroKicker: "Precision die-cutting manufacturer", heroTitle: "Precision engineered for modern electronics",
    heroText: "YMX Vietnam manufactures high-tech precision die-cut materials for mobile, computing, automotive and global electronic applications.",
    explore: "Explore capabilities", careers: "Join YMX", about: "About YMX Vietnam",
    aboutText: "The Vietnam member of YMX/Lingjiang Electronics, backed by specialist manufacturing experience since 2013 and a factory in Tam Phuoc Industrial Park, Dong Nai.",
    valuesTitle: "Four commitments behind YMX", values: ["Integrity", "Quality", "Service", "Development"], capabilities: "Core capabilities",
    products: "Products & applications", equipment: "Production & testing equipment", quality: "Quality & HSE", contact: "Contact us",
    jobs: "Career opportunities", jobsLead: "Build a precise, safe and sustainable manufacturing future with YMX.", viewJob: "View role", apply: "Apply now", openRoles: "Open positions", noJobs: "No suitable openings right now. Please check back soon.",
    footerHrLogin: "HR Login", footerAdminPortal: "Admin Portal",
  },
  zh: {
    nav: ["首页", "公司简介", "产品与应用", "生产设备", "质量与HSE", "招聘机会", "联系我们"],
    heroKicker: "精密模切制造商", heroTitle: "以精密制造赋能现代电子产业", heroText: "越南YMX为手机、电脑、汽车及全球电子应用生产高科技精密模切材料。",
    explore: "了解制造能力", careers: "加入YMX", about: "关于越南YMX", aboutText: "YMX/Lingjiang Electronics越南成员企业，拥有自2013年以来的专业制造经验，工厂位于同奈省新福工业区。",
    valuesTitle: "YMX的四项承诺", values: ["诚信", "质量", "服务", "发展"], capabilities: "核心能力", products: "产品与应用", equipment: "生产与检测设备", quality: "质量与HSE", contact: "联系我们",
    jobs: "招聘机会", jobsLead: "与YMX共建精准、安全、可持续的制造未来。", viewJob: "查看职位", apply: "立即申请", openRoles: "招聘职位", noJobs: "目前暂无合适职位，敬请稍后关注。",
    footerHrLogin: "人事登录", footerAdminPortal: "管理后台",
  },
} as const;

export function t(locale: Locale) { return copy[locale]; }

export const pageSlugs = ["", "about", "products", "equipment", "quality-hse", "careers", "contact"];

export function switchLocalePath(pathname: string, locale: Locale) {
  const bits = pathname.split("/").filter(Boolean);
  if (bits.length && isLocale(bits[0])) bits[0] = locale; else bits.unshift(locale);
  return `/${bits.join("/")}`;
}
