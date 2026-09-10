export default function Projects() {
  const featuredProjects = [
    {
      name: 'GameLink',
      desc: 'Voice & Text Chat for Gamers — Full-stack app with JWT auth, Socket.IO real-time chat, and dark-mode UI serving 100+ concurrent users.',
      tags: ['JavaScript', 'Node.js', 'Express', 'Socket.IO', 'Docker', 'Jest'],
      link: 'https://github.com/neoj123/GameLink',
      color: '#f59e0b',
    },
    {
      name: 'Azure MLOps Predictive Maintenance',
      desc: 'Cloud-native ML solution using Random Forest regression for real-time telemetry inference, deployed to Azure Managed Online Endpoint.',
      tags: ['Python', 'Azure ML', 'Scikit-learn', 'Docker'],
      link: 'https://github.com/neoj123/predictive-maintenance-azure-project',
      color: '#3b82f6',
    },
    {
      name: 'Financial Data Analyzer',
      desc: 'Full-stack tool analyzing capital market sentiment with a Python/Flask REST API and React frontend processing live Reddit data.',
      tags: ['Python', 'Flask', 'React'],
      link: 'https://github.com/neoj123/reddit-stock-sentiment-analyzer',
      color: '#10b981',
    },
  ];

  const gamingAnalyticsProjects = [
    {
      name: 'League Decision Coach',
      desc: 'Macro decision-making toolkit for League of Legends that reviews lane pressure, objectives, vision, and team state to recommend the next best play.',
      tags: ['Python', 'Game Analytics', 'Decision Scoring', 'CLI'],
      link: 'https://github.com/neoj123/league-decision-coach',
      color: '#8b5cf6',
    },
    {
      name: 'Valorant Stat Tracker',
      desc: 'Valorant analytics toolkit that summarizes ACS, K/D, KAST, headshot rate, clutch rate, agent trends, map strengths, and improvement areas.',
      tags: ['Python', 'Match Analytics', 'JSON Data', 'CLI'],
      link: 'https://github.com/neoj123/valorant-stat-tracker',
      color: '#ef4444',
    },
  ];

  const renderProjectCard = (proj) => (
    <div key={proj.name} className="project-card glow-card">
      <div className="project-color-bar" style={{ background: proj.color }} />
      <div className="project-body">
        <h3 className="project-name">{proj.name}</h3>
        <p className="project-desc">{proj.desc}</p>
        <div className="project-tags">
          {proj.tags.map((tag) => (
            <span key={tag} className="tag">{tag}</span>
          ))}
        </div>
        <a href={proj.link} className="project-link" target="_blank" rel="noopener noreferrer">
          View Project
        </a>
      </div>
    </div>
  );

  return (
    <section id="projects" className="projects-section">
      <div className="section-header">
        <h2>Projects</h2>
        <div className="underline" />
      </div>
      <div className="projects-grid">
        {featuredProjects.map(renderProjectCard)}
      </div>

      <div className="section-header gaming-projects-header">
        <h2>Gaming Analytics</h2>
        <p>New standalone GitHub projects built around competitive game decision-making and performance review.</p>
        <div className="underline" />
      </div>
      <div className="projects-grid">
        {gamingAnalyticsProjects.map(renderProjectCard)}
      </div>
    </section>
  );
}
