Ce projet est une application Python utilisant Flask pour fournir des services d'API REST, notamment pour le calcul de l'IMC (BMI) et du métabolisme de base (BMR). Le projet inclut également une intégration continue (CI) avec GitHub Actions et un processus de déploiement sur Azure Web App.

Les principaux composants du projet sont les suivants :

  - Flask API pour les calculs de santé.
  - Docker pour conteneuriser l'application.
  - GitHub Actions pour l'intégration continue et le déploiement automatisé.
  - Azure Web App pour héberger l'application en production.

## Structure du Projet

python_devops/
│
├── app.py               # Application Flask
├── Dockerfile           # Conteneurisation Docker
├── Makefile             # Script pour automatiser les tâches (tests, build, etc.)
├── requirements.txt     # Dépendances Python
├── ci.yml               # Workflow GitHub Actions pour CI
├── main_pythondevops.yml # Workflow GitHub Actions pour déploiement Azure
├── health_utils.py      # Fonctions utilitaires pour les calculs santé
└── test_utils.py        # Tests unitaires

## Fonctionnalités
### 1. Application Flask (app.py)

L'application expose deux points d'API REST :

    GET / : Point d'entrée simple renvoyant "Coucou".
    POST /bmi : Accepte un JSON avec height (taille en mètres) et weight (poids en kg), et retourne le calcul de l'IMC.
    POST /bmr : Accepte un JSON avec height, weight, age, et gender, et retourne le calcul du BMR (Basal Metabolic Rate).

Les calculs sont réalisés par les fonctions importées de health_utils.py (calculate_bmi et calculate_bmr).
### 2. Dockerfile

Le projet est conteneurisé avec Docker. Voici les étapes principales :

    Utilisation de l'image Docker officielle Python 3.11 (python:3.11-slim).
    Création du répertoire /app pour contenir le code source.
    Installation des dépendances Python via le fichier requirements.txt.
    Exposition du port 5000 pour l'API Flask.
    Lancement de l'application avec python app.py.

FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

### 3. Makefile

Le Makefile permet d'automatiser les tâches courantes du projet, comme l'installation des dépendances, l'exécution des tests, la construction de l'image Docker, et le lancement de l'application.

Exemples de commandes :

    make init : Crée un environnement virtuel et installe les dépendances.
    make test : Lance les tests unitaires définis dans test_utils.py.
    make build : Construit l'image Docker.
    make run-container : Démarre l'application dans un conteneur Docker.

### 4. Tests unitaires (test_utils.py)

Les tests sont écrits en Python et valident les fonctions utilitaires définies dans health_utils.py. Ces tests sont exécutés via la commande make test.

Exemple de tests :

import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_bmi(self):
        self.assertEqual(calculate_bmi(1.75, 70), 22.86)

    def test_bmr(self):
        self.assertEqual(calculate_bmr(1.75, 70, 25, 'M'), 1750)

### 5. GitHub Actions pour CI (ci.yml)

Le fichier ci.yml configure un pipeline d'intégration continue sur GitHub Actions. À chaque push sur la branche main, il exécute les étapes suivantes :

    Checkout du code : Récupération du code source.
    Installation des dépendances : Création d'un environnement virtuel et installation des dépendances via make init.
    Exécution des tests : Lancement des tests avec make test.
    Construction de l'image Docker : Création de l'image Docker avec make build.

name: CI Pipeline

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: make init
      - name: Run unittests
        run: make test
      - name: Build Docker image
        run: make build

### 6. GitHub Actions pour Déploiement Azure (main_pythondevops.yml)

Le fichier main_pythondevops.yml configure un workflow GitHub Actions pour déployer l'application sur Azure Web App.
Étapes du déploiement :

    Build :
        Création de l'environnement virtuel Python.
        Installation des dépendances.
        Création d'un fichier ZIP de l'application pour le déploiement.
    Déploiement :
        Téléchargement du fichier ZIP créé lors du build.
        Connexion à Azure via l'action azure/login.
        Déploiement sur l'Azure Web App avec azure/webapps-deploy.

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python version
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Create and start virtual environment
        run: |
          python -m venv venv
          source venv/bin/activate
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Zip artifact for deployment
        run: zip release.zip ./* -r
      - name: Upload artifact for deployment jobs
        uses: actions/upload-artifact@v4
        with:
          name: python-app
          path: |
            release.zip
            !venv/

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Download artifact from build job
        uses: actions/download-artifact@v4
        with:
          name: python-app
      - name: Unzip artifact for deployment
        run: unzip release.zip
      - name: Login to Azure
        uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
      - name: 'Deploy to Azure Web App'
        uses: azure/webapps-deploy@v3
        with:
          app-name: 'PythonDevOps'
          slot-name: 'Production'

## Conclusion

Ce projet met en place une application Python utilisant Flask, conteneurisée avec Docker, et déployée automatiquement sur Azure Web App via GitHub Actions. Le processus inclut l'intégration continue avec tests unitaires et construction d'images Docker, ainsi qu'un déploiement fluide et sécurisé sur Azure.

Les étapes sont entièrement automatisées, de la construction à la mise en production, garantissant une livraison continue fiable et rapide pour l'application.