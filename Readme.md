# Konsole Analyzer

Une application web qui analyse un site web et retourne des informations exploitables sur l'entreprise qui le détient.

## Demo
[https://youno.onrender.com](https://youno.onrender.com)

## Stack technique
- **Backend** : Python / Flask
- **Scraping** : BeautifulSoup + Requests
- **Analyse** : Groq API (LLaMA 3.3 70B)
- **Frontend** : HTML / CSS / JS vanilla
- **Déploiement** : Render

## Comment lancer en local

**1. Clone le repo**
```bash
git clone https://github.com/zwayzo/Youno.git
cd konsole-analyzer
```

**2. Crée ta clé Groq gratuitement**
- Va sur [console.groq.com/keys](https://console.groq.com/keys)
- Crée un compte (gratuit, pas de carte bancaire)
- Génère une clé 
- Lien d'un tutoriel : https://www.youtube.com/watch?v=9VDbhptCzlU

**3. Crée un fichier `.env` à la racine**
```
GROQ_API_KEY=ta_clé_groq
```

**4. Lance l'app**
```bash
# Première fois
make start

# Les fois suivantes
make run
```

**5. Ouvre** `http://localhost:8000`

## Architecture

L'app suit une logique en 3 étapes :
- **Scraper** : récupère le HTML du site (titre, description, scripts, liens)
- **Analyzer** : envoie les données brutes à un LLM pour les structurer
- **Scorer** : applique une logique de scoring pour évaluer le fit B2B SaaS

## Limites actuelles
- Certains sites bloquent le scraping (facebook, etc.)
- Le scoring est basé sur des règles fixes, pas du ML
- Pas de cache — chaque analyse refait un appel LLM

## Améliorations possibles
- Ajouter une API externe (Clearbit, Hunter) pour enrichir les données
- Mettre en cache les résultats pour les mêmes URLs
- Personnaliser le scoring selon le profil client de l'utilisateur