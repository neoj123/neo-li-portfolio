import { useEffect, useState } from 'react';

export default function Navbar({ currentPath, onNavigate, resumeHref }) {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 30);
    handleScroll();
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const links = [
    { to: '/', label: 'Home' },
    { to: '/about', label: 'About' },
    { to: '/experience', label: 'Experience' },
    { to: '/projects', label: 'Projects' },
    { to: '/skills', label: 'Skills' },
    { to: '/contact', label: 'Contact' },
  ];

  return (
    <nav className={scrolled ? 'nav scrolled' : 'nav'}>
      <a href="#/" className="nav-logo" onClick={(event) => onNavigate(event, '/')}>
        <span className="logo-text">neo</span>
        <span className="logo-accent">li</span>
      </a>
      <ul className="nav-links">
        {links.map((link) => (
          <li key={link.to}>
            <a
              href={`#${link.to}`}
              className={currentPath === link.to ? 'active' : ''}
              onClick={(event) => onNavigate(event, link.to)}
            >
              {link.label}
            </a>
          </li>
        ))}
        <li>
          <a href={resumeHref} target="_blank" rel="noopener noreferrer">Resume</a>
        </li>
      </ul>
    </nav>
  );
}
