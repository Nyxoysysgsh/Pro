import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import Link from '@docusaurus/Link';

type FeatureItem = {
  title: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Szybki start',
    description: (
      <>
        Zainstaluj PMMP i <Link to="/devtools">DevTools</Link>,
        uruchom serwer i napisz pierwszy plugin!
      </>
    ),
  },
  {
    title: 'API 5 – nowoczesne praktyki',
    description: (
      <>
        Struktura pluginu, komendy, eventy, konfiguracja i scheduler –
        wszystko na przykładach.
      </>
    ),
  },
  {
    title: 'Build i release',
    description: (
      <>
        Buduj lokalnie lub użyj <Link to="/poggit-github">Poggit CI</Link>
        , publikuj i aktualizuj bez bólu.
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}