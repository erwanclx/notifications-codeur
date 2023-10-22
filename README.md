# Notifications Codeur
## Description
Ce script permet de notifier les utilisateurs de Codeur.com lorsqu'un nouveau message est reçu sur le site.
Les services de notifications suivants sont disponibles :
- Discord
- Webhooks IFTTT (permettant d'envoyer des notifications sur votre téléphone, ou tout autre appareil connecté à IFTTT)  
Pour en savoir plus sur [IFTTT](https://ifttt.com/) | [Webhooks IFTTT](https://ifttt.com/maker_webhooks)
## Installation
### Prérequis
- Python doit être installé sur votre machine
#### Installation des dépendances
``pip install -r requirements.txt``
### Configuration
#### Variables d'environnement
- Renommer le fichier ``.env.example`` à la racine du projet en ``.env``
- Remplir les variables d'environnement dans le fichier ``.env``
#### Cookies
- Renommer le fichier ``cookies.py.example`` en ``cookies.py``
- Remplir les variables dans le fichier ``cookies.py``

## Utilisation
- Cloner le projet avec ``git clone https://github.com/erwanclx/notifications-codeur.git``
- Se placer dans le dossier du projet avec ``cd notifications-codeur``
### Lancement avec Docker
- Lancer le script avec ``docker-compose up -d``
### Manuellement
- Installer les dépendances avec ``pip install -r requirements.txt``
- Lancer le script avec ``python main.py``

## Auteur
- Erwan Cloux
- [Site web](https://erwancloux.fr.fr)
- [GitHub](https://github.com/erwanclx)