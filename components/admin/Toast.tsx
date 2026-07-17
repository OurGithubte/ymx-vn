"use client";
import { createContext, useCallback, useContext, useRef, useState } from "react";
import { AlertTriangle, CheckCircle2, Info, X } from "lucide-react";

type ToastKind = "success" | "error" | "info";
type ToastItem = { id: number; kind: ToastKind; message: string };
type ToastContextValue = { notify: (message: string, kind?: ToastKind) => void };

const ToastContext = createContext<ToastContextValue | null>(null);

export function useToast(): ToastContextValue {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error("useToast must be used within <ToastProvider>");
  return ctx;
}

const icons: Record<ToastKind, React.ReactNode> = {
  success: <CheckCircle2 size={18} />,
  error: <AlertTriangle size={18} />,
  info: <Info size={18} />,
};

export function ToastProvider({ children }: { children: React.ReactNode }) {
  const [items, setItems] = useState<ToastItem[]>([]);
  const counter = useRef(0);

  const notify = useCallback((message: string, kind: ToastKind = "info") => {
    const id = ++counter.current;
    setItems(list => [...list, { id, kind, message }]);
    window.setTimeout(() => setItems(list => list.filter(item => item.id !== id)), 5000);
  }, []);

  const dismiss = (id: number) => setItems(list => list.filter(item => item.id !== id));

  return (
    <ToastContext.Provider value={{ notify }}>
      {children}
      <div className="toast-host" role="status" aria-live="polite">
        {items.map(item => (
          <div key={item.id} className={`toast toast-${item.kind}`}>
            {icons[item.kind]}
            <span>{item.message}</span>
            <button aria-label="Đóng thông báo" onClick={() => dismiss(item.id)}><X size={14} /></button>
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}
