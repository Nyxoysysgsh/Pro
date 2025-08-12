/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Wprowadzenie',
    },
    {
      type: 'category',
      label: 'Podstawy',
      items: [
        'getting-started',
        'devtools',
        'plugin-structure',
        'commands-events',
        'config-scheduler',
      ],
    },
    {
      type: 'doc',
      id: 'poggit-github',
      label: 'Poggit i GitHub Pages',
    },
    {
      type: 'doc',
      id: 'faq',
      label: 'FAQ',
    },
  ],
};

module.exports = sidebars;