# Pré-requis
Sous windows, il faut installer Git-Bash et Anaconda.
Pour tester le bon fonctionnement ouvrir le terminal git-bash et taper :

    bash

On doit avoir aucun message

    git
    conda

Dans les deux cas on doit voir apparaitre des lignes de commande.

Il faut ensuite lancer via le terminal git-bash : 

    pip install pelican markdown ghp-import

Pour créer le squelette du site la première fois :

    pelican-quickstart

Une aide avec des exemples est disponible à l'adresse suivante : <https://rasor.github.io/using-pelican-blog-on-github-pages.html>

# Automatisation des tâches
Ouvrir un terminal git-bash puis se déplacer dans le dossier local du git, par exemple :

    cd D:\\IRD\\4-Developpement\\4-Git\\MathieuDepetris.github.io
    ./1_preview_content.bat

Le contenu est visualisable à l'adresse locale suivante http://localhost:8000/
Pour rafraîchir la page, après insertion de contenu et lancement du bat 2_build ci-dessous, appuyer sur F5.

Ouvrir un deuxième git-bash et se déplacer dans le dossier local du git, par exemple :

    cd D:\\IRD\\4-Developpement\\4-Git\\MathieuDepetris.github.io
    ./2_build.bat
    ./3_publish.bat "add content"