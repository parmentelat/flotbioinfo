# MOOC «Bioinformatique : génomes et algorithmes»

J'essaie de résumer ici l'impact de mes ajouts sur la structure du cours, comparé à la V1.

Il s'agit donc principalement des algorithmes dont la liste avait été établie par François. Mais j'ajoute également 2 compléments transverses, attachés à la séquence 1.4, pour introduire les choses; pour le reste, j'introduirai les concepts python au fur et à mesure.

* ***ADDITION*** il serait souhaitable de caser quelque part 

  * ~~un mot sur comment se procurer des échantillons d'ADN; google 'NCBI' -> http://www.ncbi.nlm.nih.gov/, et comment lire un fichier de ce genre pour appliquer les algos du cours~~
  * parler de `scikit-bio` ?

* ~~**1.4** Introduction aux notebooks~~
 
* ~~**1.4** Quelques notions de base de python~~

  Super rapide car je compte introduire les choses au fur et à mesure, mais il me faut quand même un tout petit peu de matière avant de commencer. Restera peut-être à ajouter:
    * mutable / pas mutable - passage d'une liste à une fonction
    * les tuples et l'affectation a,b = (1, 2)
    * enumerate vs range

* ~~**1.5** Comptage des nucléotides~~

  nombre de A, de C, de G, de T, nombre total et calcul des fréquences

* ~~**1.7** DNA walk~~

  tracé type « tortue » dans les 4 directions nord, sud, est, ouest en fonction du nucléotide rencontré. Objectifs secondaires:
    * être capable de jouer sur l'échelle pour accomoder des séquences de longueur variable
    * et pour ça voir si on peut utiliser d'autres librairies

* ~~**1.9** ditto mais tracé « compressé »~~
  * un segment tous les n segments élémentaires
  * si possible reproduire le résultat de la vidéo - en attente de l'échantillon d'entrée

* ~~**1.10** Comptage des nucléotides dans une fenêtre, glissante et recouvrante~~

  Parcourant la séquence, calcul des valeurs du ratio G/C au sein de chaque fenêtre et affichage de la courbe d’évolution de ce ratio le long de la séquence

* ~~**2.2** Transcription d’une séquence d’ADN en séquence d’ARN~~

* ***abandonné*** **2.5** Traduction triplet -> AA v1 
  * Recherche dans la table du code génétique d’un triplet et renvoi de l’acide aminé correspondant; algo pédestre

* ***abandonné*** **2.7** Traduction triplet -> AA v2 - index calculé

* ***abandonné*** Traduction triplet -> AA v3 ? - utiliser un dictionnaire

* ~~**2.8** Traduction d’une séquence de nucléotides en une séquence d’acides aminés (protéine)~~

* **3.1** Recherche d’un triplet quelconque dans une séquence d’ADN

* **3.3** Recherche du prochain triplet Start/Stop dans une séquence à partir d’une position donnée

* Identification de régions codantes sur un brin et une phase : deux stops consécutifs en phase, taille > 300, Start le « plus à gauche », enregistrement dans un tableau (position de début, position de fin)

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
