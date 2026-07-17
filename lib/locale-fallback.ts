import type { Locale } from "./i18n";
import { isRichTextEmpty } from "./rich-text";

/** If the current-locale translation is missing, fall back to Vietnamese so the public page never crashes or shows a blank section. */
export function pickText(field: Record<Locale, string> | undefined, locale: Locale): string {
  if (!field) return "";
  const value = field[locale];
  if (value && value.trim()) return value;
  return field.vi || "";
}

export function pickRich(field: Record<Locale, string | string[]> | undefined, locale: Locale): string | string[] {
  if (!field) return "";
  const value = field[locale];
  if (!isRichTextEmpty(value)) return value;
  return field.vi || "";
}
