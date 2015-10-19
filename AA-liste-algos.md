# MOOC « Bioinformatique : génomes et algorithmes »

##

J'envisage d'ajouter également 2 compléments transverses, à voir où ça peut se caser

* **?.?** Explication de comment utiliser les notebooks
  * En tous cas on peut s'inspirer du notebook de python2

* **?.?**  Rapide introduction à python
  * Je ne sais pas encore combien de compléments il faut
  * Au minimum, introduire quelque part

* **-- OR --** on peut aussi envisager d'introduire les trucs au fur et à mesure

Le mieux, il me semble, est de faire d'abord tous les algos pour voir quel est le meilleur angle pour cette intro

## Liste des Suppléments

J'essaie de résumer ici l'impact sur la structure du cours, comparé à la V1.

Il s'agit donc principalement les algorithmes dont la liste avait été établie par François, mais j'ajoute également quelques chapitres d'intro à python, et aux notebooks eux-mêmes. 

* **1.4** Introduction aux notebooks 

  * Voir avec Jean-Marc s'il pense qu'on peut mettre la vidéo de Python2 telle quelle ou bien ?
  * Je compte reprendre un notebook que j'avais rédigé pour python2, et idéalement en faire une version totalement neutre par rapport au MOOC pour réutilisation possible le cas échéant.
 
* **1.4** Quelques notions de base de python

 Super rapide car je compte introduire les choses au fur et à mesure, mais il me faut quand même un tout petit peu de matière avant de commencer.
    * les chaines de caracteres et `for`
    * les listes pour dessiner
    * les tuples et l'affectation a,b = (1, 2)
    * print()

* **1.5** Comptage des nucléotides : nombre de A, de C, de G, de T, nombre total et calcul des fréquences

* Promenade sur l’ADN (DNA walk) : 
  * **1.7** tracé type « tortue » dans les 4 directions nord, sud, est, ouest en fonction du nucléotide rencontré ;
  * **1.8** tracé « compressé » : un segment tous les n segments élémentaires

* Comptage des nucléotides dans une fenêtre, glissante et recouvrante, parcourant la séquence, calcul des valeurs du ratio G/C au sein de chaque fenêtre et affichage de la courbe d’évolution de ce ratio le long de la séquence

* Transcription d’une séquence d’ADN en séquence d’ARN

* Recherche dans la table du code génétique d’un triplet et renvoi de l’acide aminé correspondant : plusieurs versions selon l’implémentation de la table

* Traduction d’une séquence de nucléotides en une séquence d’acides aminés (protéine)

* Recherche d’un triplet quelconque dans une séquence d’ADN

* Recherche du prochain triplet Start/Stop dans une séquence à partir d’une position donnée

* Identification de régions codantes sur un brin et une phase : deux stops consécutifs en phase, taille > 300, Start le « plus à gauche », enregistrement dans un tableau (position de début, position de fin)

* Calcul de la séquence reverse complement d’une séquence donnée

* Identification de toutes les régions codantes, sur les 3 phases et sur le brin complémentaire

* Algorithme naïf de recherche d’un motif dans une séquence

* Recherche de motifs, algorithme de Boyer-Moore

* Confirmation et rectification (position du Start) des prédictions de régions codantes par la recherche des motifs RBS (site de fixation du ribosome)

* Calcul de la distance de Hamming entre 2 séquences (nombre de nucléotides différents)

* Algorithme de Needleman et Wunsch :
  *	version récursive
  * version itérative

* Remplissage du tableau des distances entre n séquences prises 2 à 2

* Algorithme UPGMA de reconstruction d’arbre phylogénétique
