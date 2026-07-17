import { renderRichText } from "@/lib/rich-text";

/** Renders a rich-text field (job description/requirements/benefits/additional info) as safe HTML. */
export function RichTextView({ value, className }: { value: string | string[] | undefined | null; className?: string }) {
  const html = renderRichText(value);
  if (!html) return null;
  return <div className={className ? `rich-text ${className}` : "rich-text"} dangerouslySetInnerHTML={{ __html: html }} />;
}
