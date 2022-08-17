# Prérequis
Sous Windows, il faut installer Git-Bash.
Pour tester le bon fonctionnement ouvrir le terminal git-bash et taper :

    bash

On doit ni avoir aucun message.

    git

On doit voir apparaitre des lignes de commande.

Il faut ensuite lancer via le terminal git-bash : 

    pip install pelican markdown ghp-import

Pour créer le squelette du site la première fois :

    pelican-quickstart

Une aide avec des exemples est disponible à l'adresse suivante : <https://rasor.github.io/using-pelican-blog-on-github-pages.html>

Pour finir, il faut installer la commande make dans le terminal git-bash.  
Pour cela, copier l'ensemble du dossier diverse\make-4.2.1-without-guile-w32-bin dans le repertoire C:\Program Files\Git\mingw64 (à adapter)

# Préparation du git la première fois

Créer un répertoire sur les pages GitHub
Copier le .gitignore disponible ici https://github.com/getpelican/pelican-blog/blob/master/.gitignore et le placer dans le répertoire du git
Créer un fichier README.md (il s'agit du document que vous lisez)

Créer une branche pelican afin de stocker les fichiers sources :

    git checkout -b pelican

Il faut aussi renseigner les indentifiants github :

    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

# Pour récupérer les fichiers source du git

Se placer dans le répertoire ou l'on souhaite copier les fichiers sources 

    git clone --branch pelican https://github.com/MathieuDepetris/MathieuDepetris.github.io.git

# Installation des thèmes et plugins pour pelican

Se placer dans le repertoire de python (ci-dessous un exemple de chemin) :

    cd C:\\"Program Files"\\Python36
    md pelican-addon-clones
    cd pelican-addon-clones
    git clone --recursive https://github.com/getpelican/pelican-plugins
    git clone --recursive https://github.com/getpelican/pelican-themes

Pour installer un thème (ici avec l'exemple du thème pelican-fh5co-marble disponible dans les fichiers sources du site)

    pelican-themes --install D:\\developpement\\MathieuDepetris.github.io\\themes\\pelican-fh5co-marble
    # Pour verifier les thèmes installés
    pelican-themes -v -l
    # Pour supprimer un thème
    pelican-themes --remove theme_name

# Automatisation des tâches

Ouvrir un terminal git-bash puis se déplacer dans le dossier local du git (exemple ci-dessous à adapter) :

    cd D:\\developpement\\git\\MathieuDepetris.github.io
    # ou
    cd R:\\travail\\MathieuDepetris.github.io

Pour générer le contenu et le prévisualiser (http://localhost:8000/) :

    make html && make serve

Pour publier le contenu :

    make publish_github
    