export default function About() {
  const interests = [
    {
      title: 'Pianist',
      text: 'Classical training and regular practice keep me sharp, patient, and detail-oriented.',
      image: 'https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?auto=format&fit=crop&w=900&q=80',
    },
    {
      title: 'Gamer at heart',
      text: 'Valorant Immortal 3, League Diamond 4, Overwatch Masters, and Brawlhalla Diamond Top 1000 NA East.',
      image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=900&q=80',
    },
    {
      title: 'Traveller',
      text: 'China, Taiwan, the United States, the Mediterranean, Peru, and many more places still on the list.',
      image: 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=900&q=80',
    },
  ];

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
          <p>
            Outside engineering, I'm a pianist, traveller, and competitive video
            game player. I like hobbies that reward consistency, fast learning,
            and reading the room under pressure.
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
      <div className="interests-grid">
        {interests.map((interest) => (
          <article key={interest.title} className="interest-card glow-card">
            <img src={interest.image} alt="" loading="lazy" />
            <div>
              <h3>{interest.title}</h3>
              <p>{interest.text}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
