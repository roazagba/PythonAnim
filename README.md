# PythonAnim

---

Auteurs:

1. AZAGBA Roméo
2. HONON DADJO Kelvine
3. MAMA Abbas
4. DJEGO Brice

---

## _Projet: Plateforme d'éxécution et d’animation d’Algorithme (Python)_

## Documentation technique Flask

### Installation

**Pré-requis:**: Système d'explotation Windows ou Linux, Python3, pip

1. Accéder au répertoire pythonanim-flask du projet depuis votre terminal / console / invite de commande.
2. Configurer un environnement virtuel

```bash
pip install virtualenv
python -m venv env
source env/bin/activate (Unix)
source env/Scripts/activate (Windows)
```

3. Installer les bibliothèques requises

```bash
pip install -r requirements.txt
```

4. Démarrer le projet back-end flask

```bash
flask --app app run --debug
```

---

## Documentation technique Vue.js

### Installation

**Pré-requis:**: Système d'explotation Windows ou Linux, NodeJs, npm

1. Accéder au répertoire pythonanim-vuejs du projet depuis votre terminal / console / invite de commande.
2. Exécuter la commande suivante pour installer les dépendances du projet:

```bash
npm install
```

3. Créer un fichier .env à la racine du projet qui contiendra ce script :

```bash
VITE_APP_URL="http://127.0.0.1:5000"  # URL de l'API Python
VITE_APP_NAME="PythonAnim"   # Nom de l'application
```

4. Démarrer le projet avec cette commande

```bash
npm run dev
```

## Copyright and License MIT

Copyright (c) 2024 Roméo AZAGBA

L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le « Logiciel »), de traiter le Logiciel sans restriction, y compris sans limitation les droits d'utiliser, de copier, de modifier, de fusionner, de publier, de distribuer, d'accorder des sous-licences et/ou de vendre des copies du Logiciel, et d'autoriser les personnes à qui le Logiciel est fourni à faire de même, sous réserve des conditions suivantes :

L'avis de droit d'auteur ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.

LE LOGICIEL EST FOURNI « TEL QUEL », SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS LES AUTEURS OU LES DÉTENTEURS DES DROITS D'AUTEUR NE PEUVENT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RAPPORT AVEC LE LOGICIEL OU L'UTILISATION OU D'AUTRES OPÉRATIONS LIÉES AU LOGICIEL.
