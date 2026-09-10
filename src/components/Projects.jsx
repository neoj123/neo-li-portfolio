export default function Projects() {
  const projects = [
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

  return (
    <section id="projects" className="projects-section">
      <div className="section-header">
        <h2>Projects</h2>
        <div className="underline" />
      </div>
      <div className="projects-grid">
        {projects.map((proj, idx) => (
          <div key={idx} className="project-card glow-card">
            <div className="project-color-bar" style={{ background: proj.color }} />
            <div className="project-body">
              <h3 className="project-name">{proj.name}</h3>
              <p className="project-desc">{proj.desc}</p>
              <div className="project-tags">
                {proj.tags.map((tag, i) => (
                  <span key={i} className="tag">{tag}</span>
                ))}
              </div>
              <a href={proj.link} className="project-link" target="_blank" rel="noopener noreferrer">
                View Project →
              </a>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
