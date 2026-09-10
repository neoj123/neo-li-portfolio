import { useEffect, useState } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Skills from './components/Skills';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './App.css';

const routes = {
  '/': HomePage,
  '/about': AboutPage,
  '/experience': ExperiencePage,
  '/projects': ProjectsPage,
  '/skills': SkillsPage,
  '/contact': ContactPage,
};

const getHashPath = () => {
  const hashPath = window.location.hash.replace('#', '');
  return routes[hashPath] ? hashPath : '/';
};

function App() {
  const [path, setPath] = useState(getHashPath);

  useEffect(() => {
    const handleHashChange = () => setPath(getHashPath());
    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  const navigate = (event, nextPath) => {
    event.preventDefault();
    if (path !== nextPath) {
      window.location.hash = nextPath;
      setPath(nextPath);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const Page = routes[path] || HomePage;

  return (
    <div className="app">
      <Navbar currentPath={path} onNavigate={navigate} resumeHref={`${import.meta.env.BASE_URL}resume.pdf`} />
      <Page onNavigate={navigate} />
      <Footer />
    </div>
  );
}

function HomePage({ onNavigate }) {
  const previewCards = [
    { href: '/projects', label: 'Projects', title: 'Systems, ML, and gaming analytics', text: 'A focused gallery of production-style builds and new standalone GitHub repos.' },
    { href: '/experience', label: 'Experience', title: 'Engineering in real teams', text: 'Internship, leadership, infrastructure, testing, and AI platform work.' },
    { href: '/skills', label: 'Skills', title: 'Tools I use to ship', text: 'Python, JavaScript, Azure, Docker, data systems, and software fundamentals.' },
  ];

  return (
    <main>
      <Hero />
      <section className="home-preview page-section">
        <div className="section-kicker">Portfolio Map</div>
        <h2>Explore the site by focus area.</h2>
        <div className="preview-grid">
          {previewCards.map((card) => (
            <a key={card.href} href={`#${card.href}`} className="preview-card" onClick={(event) => onNavigate(event, card.href)}>
              <span>{card.label}</span>
              <h3>{card.title}</h3>
              <p>{card.text}</p>
            </a>
          ))}
        </div>
      </section>
    </main>
  );
}

function AboutPage() {
  return <PageShell kicker="Profile" title="Engineer, student, and builder."><About /></PageShell>;
}

function ExperiencePage() {
  return <PageShell kicker="Experience" title="Work that spans tools, teams, and infrastructure."><Experience /></PageShell>;
}

function ProjectsPage() {
  return <PageShell kicker="Selected Work" title="Projects with clear problems, code, and outcomes."><Projects /></PageShell>;
}

function SkillsPage() {
  return <PageShell kicker="Stack" title="A practical toolkit for building and shipping."><Skills /></PageShell>;
}

function ContactPage() {
  return <PageShell kicker="Contact" title="Let’s build something useful."><Contact /></PageShell>;
}

function PageShell({ kicker, title, children }) {
  return (
    <main className="page-shell">
      <header className="page-hero">
        <div className="section-kicker">{kicker}</div>
        <h1>{title}</h1>
      </header>
      {children}
    </main>
  );
}

export default App;
