export default function Contact() {
  const socials = [
    { label: 'Email', value: 'neoj.li@mail.utoronto.ca', icon: '✉', href: 'mailto:neoj.li@mail.utoronto.ca' },
    { label: 'LinkedIn', value: 'linkedin.com/in/neoj-li', icon: 'in', href: 'https://www.linkedin.com/in/neoj-li/' },
    { label: 'GitHub', value: 'github.com/neoj123', icon: '⌨', href: 'https://github.com/neoj123' },
    { label: 'Resume', value: 'View PDF', icon: 'CV', href: `${import.meta.env.BASE_URL}resume.pdf` },
    { label: 'Phone', value: '613-415-3603', icon: '☎', href: 'tel:6134153603' },
  ];

  return (
    <section id="contact" className="contact-section">
      <div className="section-header">
        <h2>Let's Connect</h2>
        <div className="underline" />
      </div>
      <p className="contact-subtitle">
        Always open to new opportunities, collaborations, and conversations.
      </p>
      <div className="contact-grid">
        {socials.map((s, idx) => (
          <a key={idx} href={s.href} className="contact-card glow-card">
            <span className="contact-icon">{s.icon}</span>
            <div className="contact-info">
              <span className="contact-label">{s.label}</span>
              <span className="contact-value">{s.value}</span>
            </div>
          </a>
        ))}
      </div>
      <div className="contact-quote">
        <blockquote>
          "Closed mouths don't get fed."
        </blockquote>
      </div>
    </section>
  );
}
