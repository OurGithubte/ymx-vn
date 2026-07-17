"use client";
import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowLeft, LoaderCircle, Send, X } from "lucide-react";
import { useToast } from "./Toast";

export function PreviewActions({ jobId, status }: { jobId: string; status: string }) {
  const router = useRouter();
  const { notify } = useToast();
  const [publishing, setPublishing] = useState(false);

  async function publish() {
    setPublishing(true);
    try {
      const response = await fetch(`/api/admin/jobs/${jobId}`, { method: "PATCH", headers: { "content-type": "application/json" }, body: JSON.stringify({ status: "published" }) });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Không thể đăng tuyển.");
      notify("Đã đăng tuyển thành công.", "success");
      router.refresh();
    } catch (error) {
      notify(error instanceof Error ? error.message : "Có lỗi xảy ra.", "error");
    } finally {
      setPublishing(false);
    }
  }

  return (
    <div className="preview-actions">
      <Link href={`/admin/jobs/${jobId}/edit`} className="button"><ArrowLeft size={16} />Quay lại chỉnh sửa</Link>
      {status !== "published" && (
        <button type="button" className="button primary" onClick={publish} disabled={publishing}>
          {publishing ? <LoaderCircle className="spin" size={16} /> : <Send size={16} />}Đăng tuyển
        </button>
      )}
      <Link href="/admin" className="button"><X size={16} />Đóng bản xem trước</Link>
    </div>
  );
}
