import { useState } from 'react';
import { Link } from 'react-scroll';

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  const handleScroll = () => {
    setScrolled(window.scrollY > 50);
  };

  window.addEventListener('scroll', handleScroll);

  const links = [
    { to: 'hero', label: 'Home' },
    { to: 'about', label: 'About' },
    { to: 'experience', label: 'Experience' },
    { to: 'projects', label: 'Projects' },
    { to: 'skills', label: 'Skills' },
    { to: 'contact', label: 'Contact' },
  ];

  return (
    <nav className={scrolled ? 'nav scrolled' : 'nav'}>
      <div className="nav-logo">
        <span className="logo-text">neo</span>
        <span className="logo-accent">li</span>
      </div>
      <ul className="nav-links">
        {links.map((link) => (
          <li key={link.to}>
            <Link to={link.to} smooth={true} duration={500} offset={-70}>
              {link.label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
