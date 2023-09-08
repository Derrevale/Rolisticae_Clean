# Rolisticae V2

Ce projet est une application web pour les jeux de rôle, développée avec Django pour le backend et React pour le frontend.

## Structure du Projet

```
Rolisticae V2/
├── myenv/                  # Environnement virtuel Python
├── rolisticae_api/         # Backend Django
│   ├── manage.py
│   └── ...
└── rolisticae_client/      # Frontend React
    ├── package.json
    └── ...
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
    cd rolisticae_api
    python manage.py runserver
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
