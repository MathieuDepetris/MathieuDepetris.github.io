# Prérequis
Sous Windows, il faut installer Git-Bash et Anaconda.
Pour tester le bon fonctionnement ouvrir le terminal git-bash et taper :

    bash

On doit ni avoir aucun message.

    git
    conda

Dans les deux cas, on doit voir apparaitre des lignes de commande.

Il faut ensuite lancer via le terminal git-bash : 

    pip install pelican markdown ghp-import

Pour créer le squelette du site la première fois :

    pelican-quickstart

Une aide avec des exemples est disponible à l'adresse suivante : <https://rasor.github.io/using-pelican-blog-on-github-pages.html>

Pour finir, il faut installer la commande make dans le terminal git-bash.  
Pour cela, copier l'ensemble du dossier diverse\make-4.2.1-without-guile-w32-bin dans le repertoire C:\Program Files\Git\mingw64 (à adapter)

# Préparation du git

Créer un répertoire sur les pages GitHub
Copier le .gitignore disponible ici https://github.com/getpelican/pelican-blog/blob/master/.gitignore et le placer dans le répertoire du git
Créer un fichier README.md (il s'agit du document que vous lisez)

Créer une branche pelican afin de stocker les fichiers sources :
    git checkout -b pelican

# Installation des thèmes et plugins pour pelican

Se placer dans le repertoire de python (ci-dessous un exemple de chemin) :

    cd C:\\ProgramData\\Anaconda3\\pkgs\\python-3.7.3-h8c8aaf0_1
    md pelican-addon-clones
    cd pelican-addon-clones
    git clone --recursive https://github.com/getpelican/pelican-plugins
    git clone --recursive https://github.com/getpelican/pelican-themes

Pour installer un thème (ici avec l'exemple du thème pelican-fh5co-marble disponible dans les fichiers sources du site)

    pelican-themes --install E:\\1-BibiCorp\\Travail\\MathieuDepetris.github.io\\themes\\pelican-fh5co-marble
    # Pour verifier les thèmes installés
    pelican-themes -v -l

# Automatisation des tâches

Ouvrir un terminal git-bash puis se déplacer dans le dossier local du git (exemple ci-dessous à adapter) :

    cd D:\\IRD\\4-Developpement\\4-Git\\MathieuDepetris.github.io
    # ou
    cd E:\\1-BibiCorp\\Travail\\MathieuDepetris.github.io

Pour générer le contenu :

    make html

Pour prévisualiser le site (visualisable à l'adresse locale suivante http://localhost:8000/) :

    make serve

Ouvrir un terminal git-bash puis se déplacer dans le dossier local du git, par exemple :

    cd D:\\IRD\\4-Developpement\\4-Git\\MathieuDepetris.github.io
    # ou
    cd E:\\1-BibiCorp\\Travail\\MathieuDepetris.github.io
    ./1_preview_content.bat

Le contenu est visualisable à l'adresse locale suivante http://localhost:8000/

Ouvrir un deuxième git-bash et se déplacer dans le dossier local du git, par exemple :

    cd D:\\IRD\\4-Developpement\\4-Git\\MathieuDepetris.github.io
    # ou
    cd E:\\1-BibiCorp\\Travail\\MathieuDepetris.github.io
    ./2_build.bat
    ./3_publish.bat "add content"