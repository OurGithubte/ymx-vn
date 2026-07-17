"use client";
import { AlertTriangle } from "lucide-react";

export function ConfirmDialog({ open, title, message, confirmLabel = "Xác nhận", cancelLabel = "Hủy", danger, onConfirm, onCancel }: {
  open: boolean;
  title: string;
  message: string;
  confirmLabel?: string;
  cancelLabel?: string;
  danger?: boolean;
  onConfirm: () => void;
  onCancel: () => void;
}) {
  if (!open) return null;
  return (
    <div className="modal-backdrop" onMouseDown={e => { if (e.currentTarget === e.target) onCancel(); }}>
      <div className="confirm-dialog" role="alertdialog" aria-modal="true">
        <AlertTriangle className={danger ? "confirm-icon danger" : "confirm-icon"} />
        <h3>{title}</h3>
        <p>{message}</p>
        <div className="button-row">
          <button type="button" className="button" onClick={onCancel}>{cancelLabel}</button>
          <button type="button" className={danger ? "button danger-solid" : "button primary"} onClick={onConfirm}>{confirmLabel}</button>
        </div>
      </div>
    </div>
  );
}
