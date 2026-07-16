export function PageHero({ kicker, title, text }: { kicker: string; title: string; text: string }) {
  return <section className="page-hero"><div className="container"><span className="eyebrow">{kicker}</span><h1>{title}</h1><p>{text}</p></div></section>;
}
