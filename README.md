# FastAPI RPN Calculator

Cette application est une calculatrice en notation polonaise inverse (RPN) basée sur FastAPI. Elle permet d'envoyer des opérations RPN via une API et de retourner le résultat. Les opérations et les résultats sont enregistrés dans une base de données SQLite et peuvent être exportés dans un fichier CSV.

## Fonctionnalités

- Évaluation d'expressions RPN
- Enregistrement des opérations et résultats dans une base de données SQLite
- Exportation des données dans un fichier CSV
- Téléchargement du fichier CSV via l'API

## Prérequis

- Python 3.10 ou supérieur
- pip
- Docker (pour l'exécution avec Docker)
- git (pour la gestion du code source)

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/kaddari53/Test-ayomi.git
cd Test-ayomi

Créer et activer un environnement virtuel

bash

python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`

Installer les dépendances

bash

pip install -r requirements.txt

Utilisation
Exécuter l'application localement

bash

uvicorn main:app --reload

L'application sera accessible à l'adresse http://127.0.0.1:8000.
Utiliser Docker

    Construire l'image Docker

bash

docker-compose build

    Démarrer les services

bash

docker-compose up

L'application sera accessible à l'adresse http://127.0.0.1:8000.
Endpoints
Racine

    URL: /
    Méthode: GET
    Description: Vérifie que l'application fonctionne.
    Réponse:

    json

    {
        "message": "Welcome to the FastAPI RPN Calculator API!"
    }

Évaluer une expression

    URL: /evaluate/
    Méthode: POST
    Description: Évalue une expression RPN.
    Corps de la requête:

    json

{
    "expression": "3 4 +"
}

Réponse:

json

    {
        "expression": "3 4 +",
        "result": 7.0
    }

Exporter les données

    URL: /export/
    Méthode: GET
    Description: Exporte les opérations et les résultats dans un fichier CSV.
    Réponse:

    json

    {
        "message": "Data exported to data/operations.csv"
    }

Télécharger le fichier CSV

    URL: /download/
    Méthode: GET
    Description: Télécharge le fichier CSV contenant les opérations et les résultats.
    Réponse: Fichier CSV

Tests
Exécuter les tests

Assurez-vous d'avoir pytest et httpx installés dans votre environnement virtuel :

bash

pip install pytest httpx

Exécutez les tests avec la commande suivante :

bash

pytest

Utilisation de l'extension REST Client

Pour tester votre API avec l'extension REST Client de Visual Studio Code, vous pouvez utiliser le fichier api.http. Voici un exemple de contenu pour api.http :

http

GET http://127.0.0.1:8000/

###

POST http://127.0.0.1:8000/evaluate
Content-Type: application/json

{
    "expression" : "4 5 + 7 *"
}

###

POST http://127.0.0.1:8000/evaluate
Content-Type: application/json

{
    "expression" : "4 5 + 10 *"
}

###

GET http://127.0.0.1:8000/export

###

GET http://127.0.0.1:8000/download

Structure du projet

plaintext

rpn-calculator/
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── main.py
├── README.md
├── requirements.txt
├── api.http
└── tests/
    ├── __init__.py
    └── test_main.py

Documentation
FastAPI

Documentation : https://devdocs.io/fastapi/
Docker

Documentation : https://docker-docs.uclv.cu/