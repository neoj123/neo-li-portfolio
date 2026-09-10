export default function About() {
  return (
    <section id="about" className="about-section">
      <div className="section-header">
        <h2>About Me</h2>
        <div className="underline" />
      </div>
      <div className="about-grid">
        <div className="about-card glow-card">
          <div className="about-avatar">NL</div>
          <h3>Neo Li</h3>
          <p className="about-role">Software Engineer &bull; Student</p>
        </div>
        <div className="about-text">
          <p>
            I'm a 3rd year Computer Engineering student at the University of
            Toronto, currently co-op'd as a Software Engineer at Microchip
            Technology. I'm also pursuing a minor in Artificial Intelligence and
            Engineering Business.
          </p>
          <p>
            When I'm not coding, you can find me diving into open-source
            intelligence, building side projects, or engineering with the UofT
            BOTE consulting team. I believe in writing code that matters — code
            that solves real problems and scales with purpose.
          </p>
          <div className="about-facts">
            <div className="fact">
              <span className="fact-number">23+</span>
              <span className="fact-label">Bugs Fixed</span>
            </div>
            <div className="fact">
              <span className="fact-number">400+</span>
              <span className="fact-label">Tests Written</span>
            </div>
            <div className="fact">
              <span className="fact-number">10+</span>
              <span className="fact-label">Team Members Led</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
