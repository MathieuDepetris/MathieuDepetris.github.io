title: Redressement statistique d'un échantillon
image: /pictures/portfolio/redressement_statistique_2015.jpg
summary: Élaboration d’une fonction de redressement statistique.
Author: Depetris M.
date: 2020-01-30
lang: fr

## Redressement statistique d'un échantillon

<font color="#238896"><strong>Structure :</strong></font> Station Ifremer de Brest
<br><font color="#238896"><strong>Date :</strong></font> 2015

### Principes et objectifs

<p style="text-align: justify">
Le redressement d’échantillons (ou calage sur marges) a pour objectif d’améliorer la représentativité de l’échantillon, sur un certain nombre de critères de qualification aussi appelés variables auxiliaires. Le principe sous-jacent est que seul un échantillon ayant la même structure que la population-mère sur les critères que l’on connaît de cette population, permet de généraliser les réponses obtenues sur les autres critères, à l’ensemble de cette population. Le redressement cherche donc à appliquer des pondérations aux individus pour augmenter le poids de ceux appartenant à des groupes sous-représentés dans l’échantillon interrogé par rapport à la population-mère, et à réduire parallèlement le poids de ceux qui sont sur-représentés.
</p>

<p style="text-align: justify">
Concrètement, on cherche à obtenir des répartitions comparables entre la population et l’échantillon. On va donc associer à chaque donnée un poids de redressement (par défaut le poids de chaque donnée est identique et égal au taux de sondage : n échantillon / N population).
</p>

### Programmation de la fonction

<p style="text-align: justify">
Lors de mon passage au Laboratoire de Biologie Halieutique de l’Ifremer de Brest, j’ai élaboré en collaboration avec Sébastien Demanèche (LBH Ifremer Brest) une fonction sous R permettant de calculer les poids de redressement d’un échantillon. Elle utilise le package « survey » développé par le professeur Thomas Lumley, et plus précisément la fonction « calibrate ».
</p>

### Perspectives et évolutions futures

<p style="text-align: justify">
Les premiers essais se sont montrés concluant et ont permis d’observer une nette amélioration dans les calculs dérivants de l’échantillon redressé, par rapport à l’échantillon non redressé. Cependant, l’objectif principal de la fonction (sa généralisation à n’importe quel « type » d’échantillon) pose de nombreuses questions. Par exemple, il sera nécessaire de regrouper certaines modalités au sein des variables, afin d’éviter la non convergence de la fonction (dans les cas où l’on a très peu d’occurrence pour certaines modalités). De plus, la sélection des variables auxiliaires devra être approfondie. Les limites du redressement, dont la variable « précision », dépendent beaucoup des variables auxiliaires utilisées.
</p>
