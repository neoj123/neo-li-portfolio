export default function Skills() {
  const categories = [
    {
      title: 'Languages',
      items: ['Java', 'Python', 'C', 'C++', 'JavaScript', 'TypeScript', 'SQL', 'HTML/CSS'],
    },
    {
      title: 'AI & Machine Learning',
      items: ['Agentic AI', 'MCP', 'Scikit-learn', 'PyTorch', 'Azure ML'],
    },
    {
      title: 'Frameworks & Concepts',
      items: ['OOP', 'Data Structures', 'Algorithms', 'System Design', 'RESTful APIs', 'CI/CD', 'Agile'],
    },
    {
      title: 'Developer Tools',
      items: ['Git/GitHub', 'Docker', 'Kubernetes', 'Azure DevOps', 'Linux', 'CMake'],
    },
  ];

  return (
    <section id="skills" className="skills-section">
      <div className="section-header">
        <h2>Technical Skills</h2>
        <div className="underline" />
      </div>
      <div className="skills-grid">
        {categories.map((cat, idx) => (
          <div key={idx} className="skill-category glow-card">
            <h3>{cat.title}</h3>
            <div className="skill-tags">
              {cat.items.map((item, i) => (
                <span key={i} className="skill-tag">{item}</span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
