Ce projet est une application Python utilisant Flask pour fournir des services d'API REST, notamment pour le calcul de l'IMC (BMI) et du métabolisme de base (BMR). Le projet inclut également une intégration continue (CI) avec GitHub Actions et un processus de déploiement sur Azure Web App.

Les principaux composants du projet sont les suivants :

  - Flask API pour les calculs de santé.
  - Docker pour conteneuriser l'application.
  - GitHub Actions pour l'intégration continue et le déploiement automatisé.
  - Azure Web App pour héberger l'application en production.

## Structure du Projet

```
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
```

## Fonctionnalités
### 1. Application Flask (app.py)

L'application expose deux points d'API REST :

    GET / : Point d'entrée simple renvoyant "Coucou".
    POST /bmi : Accepte un JSON avec height (taille en mètres) et weight (poids en kg), et retourne le calcul de l'IMC.
    POST /bmr : Accepte un JSON avec height, weight, age, et gender, et retourne le calcul du BMR (Basal Metabolic Rate).

Les calculs sont réalisés par les fonctions importées de health_utils.py (calculate_bmi et calculate_bmr).
### 2. Dockerfile

Le projet est conteneurisé avec Docker. Voici les étapes principales :

- Utilisation de l'image Docker officielle Python 3.11 (python:3.11-slim).
- Création du répertoire /app pour contenir le code source.
- Installation des dépendances Python via le fichier requirements.txt.
- Exposition du port 5000 pour l'API Flask.
- Lancement de l'application avec python app.py.

### 3. Makefile

Le Makefile permet d'automatiser les tâches courantes du projet, comme l'installation des dépendances, l'exécution des tests, la construction de l'image Docker, et le lancement de l'application.

#### Exemples de commandes :

    make init : Crée un environnement virtuel et installe les dépendances.
    make test : Lance les tests unitaires définis dans test_utils.py.
    make build : Construit l'image Docker.
    make run-container : Démarre l'application dans un conteneur Docker.

### 4. Tests unitaires (test_utils.py)

Les tests sont écrits en Python et valident les fonctions utilitaires définies dans health_utils.py. Ces tests sont exécutés via la commande make test. Les tests sont écrits en utilisant la bibliothèque unittest de Python.

#### Exemples de tests :

- Test du calcul de l'IMC :
  - Test avec une taille de 1,75 m et un poids de 70 kg.
  - Test pour des valeurs incorrectes (taille en cm au lieu de m).
- Test du calcul du BMR :
  - Test pour un utilisateur de sexe féminin et masculin avec des valeurs correctes.
  - Test avec une valeur incorrecte pour le sexe.

### 5. Tests d'intégration API (test-api.py)

Le fichier test-api.py est un script de test d'intégration simple pour tester les points d'API /bmi et /bmr de l'application Flask. Il envoie des requêtes POST aux deux points d'API en utilisant la bibliothèque requests et affiche les réponses.
Fonctionnement du test :

    Le script envoie une requête POST à l'API /bmi avec des paramètres height et weight pour calculer l'IMC.

    Le script envoie une requête POST à l'API /bmr avec des paramètres height, weight, age et gender pour calculer le BMR.
    Les réponses des API sont affichées dans la console.

### 6. GitHub Actions pour CI (ci.yml)

Le fichier ci.yml configure un pipeline d'intégration continue sur GitHub Actions. À chaque push sur la branche main, il exécute les étapes suivantes :

    Checkout du code : Récupération du code source.
    Installation des dépendances : Création d'un environnement virtuel et installation des dépendances via make init.
    Exécution des tests : Lancement des tests avec make test.
    Construction de l'image Docker : Création de l'image Docker avec make build.


### 7. GitHub Actions pour Déploiement Azure (main_pythondevops.yml)

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


## Conclusion

Ce projet met en place une application Python utilisant Flask, conteneurisée avec Docker, et déployée automatiquement sur Azure Web App via GitHub Actions. Le processus inclut l'intégration continue avec tests unitaires et construction d'images Docker, ainsi qu'un déploiement fluide et sécurisé sur Azure.

Les étapes sont entièrement automatisées, de la construction à la mise en production, garantissant une livraison continue fiable et rapide pour l'application.