# YMX Vietnam Website & Recruitment Portal

Website doanh nghiệp ba ngôn ngữ và hệ thống tuyển dụng xây dựng bằng Next.js, TypeScript, Supabase và Resend.

## Chức năng

- Website Việt / Anh / Trung, responsive cho desktop và mobile.
- Danh sách và chi tiết vị trí tuyển dụng lấy từ PostgreSQL.
- Ứng viên nộp thông tin và CV PDF/DOCX tối đa 5 MB.
- CV được lưu trong private bucket, chỉ tài khoản HR được cấp quyền mới tải được.
- Trang quản trị `/admin`: đăng tin, tìm ứng viên, tải CV, chuyển trạng thái và gửi email kết quả.
- Lưu lịch sử đổi trạng thái và lịch sử email.

## Chạy local

1. Sao chép `.env.example` thành `.env.local` và điền cấu hình.
2. Chạy `pnpm install`.
3. Chạy `pnpm dev` và mở `http://localhost:3000`.

Nếu chưa cấu hình Supabase, website công khai vẫn hiển thị hai vị trí mẫu; form ứng tuyển sẽ thông báo dịch vụ đang được cấu hình và không làm mất CV.

## Khởi tạo Supabase

1. Tạo một Supabase project.
2. Mở SQL Editor và chạy `supabase/schema.sql`, sau đó chạy `supabase/seed.sql` để tạo hai tin tuyển dụng mẫu.
3. Trong Authentication, tạo tài khoản HR.
4. Lấy UUID của tài khoản rồi chạy:

```sql
insert into public.profiles (id, full_name, role)
values ('UUID_CUA_TAI_KHOAN', 'YMX HR', 'admin');
```

5. Điền URL, anon key và service role key vào Vercel Environment Variables.

## Email

Xác thực tên miền gửi thư trong Resend, sau đó cấu hình `RESEND_API_KEY`, `RECRUITMENT_FROM_EMAIL` và `HR_NOTIFICATION_EMAIL`. Có thể thay Resend bằng SMTP công ty trong giai đoạn tích hợp hạ tầng chính thức.

## Triển khai Vercel

Import repository GitHub vào Vercel, khai báo các biến môi trường giống `.env.example`, sau đó deploy. Region mặc định được đặt tại Singapore để gần người dùng và database khu vực châu Á.

Checklist nghiệm thu production nằm tại `docs/DEPLOYMENT-CHECKLIST.md`.
