// @ts-check

const config = {
  title: 'PocketMine‑MP Plugin Dev (API 5)',
  tagline: 'Nowoczesny przewodnik tworzenia pluginów dla PMMP',
  url: 'https://nyxoysysgsh.github.io',
  baseUrl: '/Pro/',
  favicon: 'img/favicon.ico',
  organizationName: 'Nyxoysysgsh',
  projectName: 'Pro',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  i18n: {
    defaultLocale: 'pl',
    locales: ['pl'],
  },
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/Nyxoysysgsh/Pro/edit/main/',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'PMMP Docs',
        logo: {
          alt: 'PMMP Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            href: 'https://github.com/Nyxoysysgsh/Pro',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `© 2025 • PocketMine‑MP Plugin Dev`,
      },
      prism: {
        theme: require('prism-react-renderer/themes/github'),
        darkTheme: require('prism-react-renderer/themes/dracula'),
        additionalLanguages: ['php', 'yaml', 'bash'],
      },
    }),
};

module.exports = config;