import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Witaj w ${siteConfig.title}`}
      description="Dokumentacja PocketMine‑MP Plugin Dev (API 5)">
      <header className="hero hero--primary">
        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div>
            <Link className="button button--secondary button--lg" to="/getting-started">
              Zaczynajmy
            </Link>
          </div>
        </div>
      </header>
      <main>
        <section className="container margin-vert--lg">
          <div className="row">
            <div className="col col--6">
              <h2>Co znajdziesz</h2>
              <ul>
                <li>Instalacja PMMP i DevTools</li>
                <li>Struktura pluginu i dobre praktyki</li>
                <li>Komendy, eventy, konfiguracja</li>
                <li>Scheduler i przykłady</li>
                <li>Poggit i publikacja</li>
              </ul>
            </div>
            <div className="col col--6">
              <h2>Szybkie linki</h2>
              <ul>
                <li><Link to="/devtools">DevTools</Link></li>
                <li><Link to="/plugin-structure">Struktura pluginu</Link></li>
                <li><Link to="/commands-events">Komendy i eventy</Link></li>
                <li><Link to="/config-scheduler">Konfiguracja i scheduler</Link></li>
                <li><Link to="/poggit-github">Poggit i GitHub Pages</Link></li>
              </ul>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}