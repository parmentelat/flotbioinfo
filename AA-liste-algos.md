# MOOC «Bioinformatique : génomes et algorithmes»

Ce document liste les ajouts *notebooks* sur la structure du cours, comparé à la V1.

* **OK** `w1/w1-s04-c1-notebooks.ipynb`
> Introduction aux notebooks
 
* **OK** `w1/w1-s04-c2-rudiments.ipynb` 
> Quelques rudiments de python

  Super rapide car je compte introduire les choses au fur et à mesure, mais il me faut quand même un tout petit peu de matière avant de commencer. Restera peut-être à ajouter:
    * mutable / pas mutable - passage d'une liste à une fonction
    * les tuples et l'affectation a,b = (1, 2)
    * enumerate vs range

* **OK** `w1/w1-s05-c1-frequences.ipynb` 
> Calcul des fréquences des 4 bases

  nombre de A, de C, de G, de T, nombre total et calcul des fréquences

* **OK** `w1/w1-s07-c1-promenade.ipynb` 
> Promenade le long de l'ADN

  tracé type « tortue » dans les 4 directions nord, sud, est, ouest en fonction du nucléotide rencontré. Objectifs secondaires:
    * être capable de jouer sur l'échelle pour accomoder des séquences de longueur variable
    * et pour ça voir si on peut utiliser d'autres librairies

* **OK** `w1/w1-s09-c1-promenade-resume.ipynb` 
> Promenade revisitée
  * un segment tous les n segments élémentaires
  * si possible reproduire le résultat de la vidéo - en attente de l'échantillon d'entrée

* **OK** `w1/w1-s10-c1-comptage-fenetre.ipynb`
> Comptage des nucléotides sur une fenêtre

  Parcourant la séquence, calcul des valeurs du ratio G/C au sein de chaque fenêtre et affichage de la courbe d’évolution de ce ratio le long de la séquence

* **OK** `w2/w2-s02-c1-traduction-adn-arn.ipynb`
> Traduction d'ADN en ARN

* **OK** `w2/w2-s08-c1-arn-acides-amines.ipynb`
> Traduction d'un ARN en acides aminés

* ***TODO*** `w3/w3-s02-c1-regions-codantes.ipynb`
> Recherche de régions codantes

  Identification de régions codantes sur un brin et une phase : deux stops consécutifs en phase, taille > 300, Start le « plus à gauche », enregistrement dans un tableau (position de début, position de fin)

* **OK** `w3/w3-s03-c1-recherche-chaine.ipynb`
> **3.3** Recherches dans une chaine
  * recherche 'naive' 
  * et avec regexps

* Calcul de la séquence reverse complement d’une séquence donnée

* Identification de toutes les régions codantes, sur les 3 phases et sur le brin complémentaire

* **3.6** Algorithme naïf de recherche d’un motif dans une séquence

* **3.6** Recherche de motifs, algorithme de Boyer-Moore

* Confirmation et rectification (position du Start) des prédictions de régions codantes par la recherche des motifs RBS (site de fixation du ribosome)

* **4.3** Calcul de la distance de Hamming entre 2 séquences (nombre de nucléotides différents)

* Algorithme de Needleman et Wunsch :
  *	 **4.8** version récursive
  * **4.9** version itérative

* **5.3** Remplissage du tableau des distances entre n séquences prises 2 à 2

* **5.4** Algorithme UPGMA de reconstruction d’arbre phylogénétique


====
NOTES diverses


Il s'agit donc principalement des algorithmes dont la liste avait été établie par François. Mais j'ajoute également 2 compléments transverses, attachés à la séquence 1.4, pour introduire les choses; pour le reste, j'introduirai les concepts python au fur et à mesure.

* ***ADDITION*** il serait souhaitable de caser quelque part 

  * ~~un mot sur comment se procurer des échantillons d'ADN; google 'NCBI' -> http://www.ncbi.nlm.nih.gov/, et comment lire un fichier de ce genre pour appliquer les algos du cours~~
  * parler de `scikit-bio` ?

* ***abandonné*** **2.5** Traduction triplet -> AA v1 - voir **2.8**

* ***abandonné - groupé avec 3.3*** (was 3.1) Recherche d’un triplet quelconque dans une séquence d’ADN

