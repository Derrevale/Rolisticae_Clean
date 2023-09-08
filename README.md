# Rolisticae V2

Ce projet est une application web pour les jeux de rôle, développée avec Django pour le backend et React pour le frontend.

## Structure du Projet

```
Rolisticae_Clean/
├── .github/                        # Fichiers de configuration GitHub
│     └── workflows/                    # Fichiers de configuration des workflows
│             └── main.yml               # Fichier de configuration du workflow du backend
├── docs/                           # Documentation
├── venv/                         # Environnement virtuel Python
├── backend/                        # Backend Django
│   └── rolisticae_api/                # Projet Django
│        ├── rolisticae_core/             # Application principale
│        ├── apps/                        # Applications secondaires
│        ├── media/                       # Fichiers médias
│        ├── static/                      # Fichiers statiques
│        ├── settings/                    # Fichiers de configuration
│        │       ├── base.py                 # Fichier de configuration de base
│        │       ├── dev.py                  # Fichier de configuration de développement
│        │       └── prod.py                 # Fichier de configuration de production
│        ├── db.sqlite3                   # Base de données SQLite
│        ├── __init__.py                  # Initialisation du projet
│        └── manage.py                 # Fichier de gestion du projet
│
└── frontend/              # Frontend React
    ├── rolisticae_client/      # Application React
    │   ├── public/                 # Fichiers publics
    │   ├── src/                    # Fichiers sources
    │   │   ├── components/              # Composants React
    │   │   ├── pages/                   # Pages React
    │   │   ├── css/                     # Fichiers de style
    │   │   ├── config/                  # Fichiers de configuration      
    │   │   ├── App.css                  # Fichier de style global
    │   │   ├── App.js                   # Composant principal
    │   │   ├── index.css                # Fichier de style de la page principale
    │   │   ├── index.js                 # Fichier de la page principale
    │   │   ├── logo.svg                 # Logo React
    │   │   ├── reportWebVitals.js       # Fichier de rapport de performances
    │   │   └── setupTests.js            # Fichier de configuration des tests
    │   │
    │   ├── .env                    # Fichier de variables d'environnement
    │   ├── .gitignore              # Fichier d'ignorance Git
    │   ├── package-lock.json      # Fichier de verrouillage des dépendances
    │   ├── package.json           # Fichier de configuration des dépendances
    │   ├── README.md              # Fichier README
    │   └── yarn.lock              # Fichier de verrouillage des dépendances
    │
    ├── README.md              # Fichier README
    └── gitignore               # Fichier d'ignorance Git
```

## Prérequis

- Python 3.x
- Node.js et npm
- Git

## Installation

### Backend (Django)

1. Clonez le dépôt GitHub :

    ```bash
    git clone [URL_DU_DEPOT]
    ```

2. Naviguez vers le dossier \`Rolisticae V2\` :

    ```bash
    cd "Rolisticae V2"
    ```

3. Activez l'environnement virtuel :

    - Sur Windows : `myenv\\Scripts\\activate`
    - Sur macOS et Linux : `source myenv/bin/activate`

4. Installez les dépendances :

    ```bash
    pip install -r rolisticae_api/requirements.txt
    ```

5. Lancez le serveur de développement :

    ```bash
    cd rolisticae_core
    python manage.py runserver
    ```
6. Créez un superutilisateur :

    ```bash
    python manage.py createsuperuser
    ```
   
7. Création application :

    ```bash
    cd apps
   python ../manage.py startapp [AppName]
    ```
8. Création migration :

    ```bash
    python manage.py makemigrations
    ```
9. Mise à jour de la base de données :

    ```bash
       python manage.py migrate 
   ```   
   
### Frontend (React)

1. Naviguez vers le dossier `rolisticae_client` :

    ```bash
    cd rolisticae_client
    ```

2. Installez les dépendances :

    ```bash
    npm install
    ```

3. Lancez l'application React :

    ```bash
    npm start
    ```

## Utilisation

Ouvrez votre navigateur et accédez à :

- Backend : `http://localhost:8000/`
- Frontend : `http://localhost:3000/`

