import type { Locale } from "./i18n";

export type Job = {
  id: string; slug: string; title: Record<Locale, string>; department: string; location: string;
  employmentType: string; summary: Record<Locale, string>; responsibilities: Record<Locale, string[]>;
  requirements: Record<Locale, string[]>; publishedAt: string;
};

export const sampleJobs: Job[] = [
  {
    id: "quality-engineer", slug: "quality-engineer", department: "Quality", location: "Đồng Nai", employmentType: "Full-time", publishedAt: "2026-07-15",
    title: { vi: "Kỹ sư Chất lượng", en: "Quality Engineer", zh: "质量工程师" },
    summary: { vi: "Kiểm soát chất lượng sản phẩm cắt bế và phối hợp cải tiến quy trình cùng các bộ phận sản xuất.", en: "Own die-cut product quality and coordinate cross-functional process improvement.", zh: "负责模切产品质量并协调生产部门持续改进流程。" },
    responsibilities: { vi: ["Theo dõi IQC/IPQC/OQC", "Phân tích lỗi và thực hiện CAPA/8D", "Quản lý hồ sơ đo lường"], en: ["Monitor IQC/IPQC/OQC", "Lead defect analysis and CAPA/8D", "Maintain measurement records"], zh: ["跟进IQC/IPQC/OQC", "执行缺陷分析及CAPA/8D", "维护测量记录"] },
    requirements: { vi: ["Tốt nghiệp kỹ thuật", "Có kinh nghiệm QA/QC sản xuất", "Tư duy dữ liệu và giao tiếp tốt"], en: ["Engineering degree", "Manufacturing QA/QC experience", "Strong analytical communication"], zh: ["工程相关专业", "制造业QA/QC经验", "良好的分析与沟通能力"] },
  },
  {
    id: "production-technician", slug: "production-technician", department: "Production", location: "Đồng Nai", employmentType: "Full-time", publishedAt: "2026-07-12",
    title: { vi: "Kỹ thuật viên Sản xuất", en: "Production Technician", zh: "生产技术员" },
    summary: { vi: "Vận hành, kiểm tra và bảo dưỡng cơ bản dây chuyền cắt cuộn, cắt bế và cán màng.", en: "Operate, inspect and perform basic maintenance on slitting, die-cutting and laminating lines.", zh: "操作、检查并基础维护分切、模切及覆膜设备。" },
    responsibilities: { vi: ["Vận hành máy theo PWI", "Kiểm tra thông số đầu ca", "Ghi nhận sản lượng và bất thường"], en: ["Operate machines to PWI", "Verify shift-start parameters", "Record output and abnormalities"], zh: ["按PWI操作设备", "确认开班参数", "记录产量及异常"] },
    requirements: { vi: ["Trung cấp kỹ thuật trở lên", "Làm việc theo ca", "Cẩn thận và tuân thủ an toàn"], en: ["Technical diploma or above", "Available for shift work", "Safety-focused and detail-oriented"], zh: ["中专或以上技术学历", "可接受倒班", "注重细节并遵守安全规范"] },
  },
];
