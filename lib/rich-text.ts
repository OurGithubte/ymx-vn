/**
 * Minimal, dependency-free bullet-list renderer used for the job
 * description, requirements and benefits fields. This is a plain textarea
 * (no rich-text editor, no toolbar, no markup): every non-empty line the
 * admin types becomes one bullet item.
 *
 * Older rows created before this field existed may still store the value
 * as a plain string[] (one bullet per array item) instead of a single
 * newline-separated string. renderRichText() accepts either shape so old
 * jobs (including the two seeded sample jobs) keep rendering correctly.
 */

function escapeHtml(value: string): string {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function linesOf(source: string | string[] | undefined | null): string[] {
  if (Array.isArray(source)) return source.map(item => String(item).trim()).filter(Boolean);
  return String(source || "").replace(/\r\n/g, "\n").split("\n").map(line => line.trim()).filter(Boolean);
}

/** Renders each non-empty line/array-item as a <li> inside a <ul>. Returns "" when there is no content. */
export function renderRichText(source: string | string[] | undefined | null): string {
  const lines = linesOf(source);
  if (!lines.length) return "";
  return "<ul>" + lines.map(line => `<li>${escapeHtml(line)}</li>`).join("") + "</ul>";
}

/** True when the field has no meaningful content. */
export function isRichTextEmpty(source: string | string[] | undefined | null): boolean {
  return linesOf(source).length === 0;
}

/** Turn a legacy string[] into an editable plain-textarea string ("one item per line") for the form. */
export function arrayToRichText(source: string | string[] | undefined | null): string {
  if (Array.isArray(source)) return source.map(item => String(item)).join("\n");
  return source || "";
}
