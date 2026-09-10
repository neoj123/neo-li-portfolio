import { useEffect, useState } from 'react';

export default function Hero() {
  const [visible, setVisible] = useState(false);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });

  useEffect(() => {
    setVisible(true);
    const handleMouseMove = (e) => {
      setMousePos({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  const glowStyle = {
    '--mx': `${mousePos.x}px`,
    '--my': `${mousePos.y}px`,
  };

  return (
    <section id="hero" className={`hero-section ${visible ? 'visible' : ''}`}>
      <div className="hero-glow" style={glowStyle} />
      <div className="hero-content">
        <div className="hero-tag">
          <span className="pulse-dot" /> Available for opportunities
        </div>
        <h1 className="hero-title">
          Hi, I'm <span className="gradient-text">Neo Li</span>
        </h1>
        <h2 className="hero-subtitle">
          Software Engineer @ Microchip &bull; 3rd Year{' '}
          <span className="gradient-text">Computer Engineer</span> at UofT
        </h2>
        <p className="hero-bio">
          Building intelligent systems, architecting scalable platforms, and
          turning ideas into code. Currently exploring the intersection of AI and
          software engineering.
        </p>
        <div className="hero-buttons">
          <a href="#projects" className="btn-primary">
            View My Work
          </a>
          <a href="#contact" className="btn-secondary">
            Get In Touch
          </a>
        </div>
      </div>
      <div className="hero-floaters">
        {['⟨⟩', '{()}', 'λ', '∑', 'π', '∫', '≈', '→'].map((char, i) => (
          <span
            key={char}
            className="floater"
            style={{
              '--i': i,
              left: `${10 + (i * 12) % 80}%`,
              top: `${10 + (i * 15) % 70}%`,
              animationDelay: `${i * 0.4}s`,
              fontSize: `${14 + (i % 3) * 6}px`,
            }}
          >
            {char}
          </span>
        ))}
      </div>
    </section>
  );
}
