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
