import Link from "next/link";
export default function NotFound() { return <main className="empty-state"><div className="logo-mark">YMX</div><h1>Không tìm thấy trang</h1><p>Nội dung bạn cần có thể đã được di chuyển.</p><Link className="button primary" href="/vi">Về trang chủ</Link></main>; }
