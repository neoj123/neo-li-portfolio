import microchipLogo from '../assets/logos/microchip-logo.png';
import osintLogo from '../assets/logos/osint-logo.jpg';

export default function Experience() {
  const experiences = [
    {
      title: 'Software Engineer Intern',
      company: 'Microchip Technology',
      location: 'Ottawa, ON',
      dates: 'May 2026 – Aug 2026',
      logo: 'M',
      logoSrc: microchipLogo,
      items: [
        'Engaged in full lifecycle product development within an Agile/Scrum team, applying modern design patterns to modernize a critical enterprise debugging tool',
        'Ported a legacy Perl codebase to a unified Python and C++ architecture, actively making code changes that directly improved system interoperability',
        'Engineered a CI/CD pipeline using Jenkins and Docker to streamline multi-platform builds, reducing manual deployment time by 40%',
        'Authored 400+ automated tests with pytest and resolved 45+ software bugs across a 23K-line codebase',
      ],
    },
    {
      title: 'Director of Technology',
      company: 'UofT Open-Source Intelligence',
      location: 'Toronto, ON',
      dates: 'Oct 2025 – Present',
      logo: 'U',
      logoSrc: osintLogo,
      items: [
        'Led a cross-functional team of 10+ engineers to architect an AI platform exploring agentic AI methodologies with 80% accuracy',
        'Researched and integrated the Model Context Protocol (MCP) to standardize contextual data feeding between localized LLMs',
        'Deployed scalable backend infrastructure using Docker and Azure Kubernetes Service (AKS) for real-time data processing',
      ],
    },
    {
      title: 'Lead Engineer',
      company: 'UofT BOTE Consulting',
      location: 'Toronto, ON',
      dates: 'Jan 2025 – Apr 2025',
      logo: 'B',
      logoHint: 'bote-logo.png',
      items: [
        'Leading engineering efforts on a consulting project, driving technical direction and delivery',
        'Collaborating with cross-functional teams to build impactful solutions for real-world challenges',
      ],
    },
  ];

  return (
    <section id="experience" className="experience-section">
      <div className="section-header">
        <h2>Experience</h2>
        <div className="underline" />
      </div>
      <div className="experience-timeline">
        {experiences.map((exp, idx) => (
          <div key={idx} className="timeline-card glow-card">
            <div className="timeline-marker">
              <span className="marker-icon" title={exp.logoHint ? `Logo placeholder: ${exp.logoHint}` : exp.company}>
                {exp.logoSrc ? <img src={exp.logoSrc} alt={`${exp.company} logo`} /> : exp.logo}
              </span>
              {idx < experiences.length - 1 && <div className="marker-line" />}
            </div>
            <div className="timeline-content">
              <div className="timeline-header">
                <h3>{exp.title}</h3>
                <span className="timeline-dates">{exp.dates}</span>
              </div>
              <div className="timeline-company">
                <span className="company-name">{exp.company}</span>
                <span className="company-location">{exp.location}</span>
              </div>
              <ul className="timeline-items">
                {exp.items.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
