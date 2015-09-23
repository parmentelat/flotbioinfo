# MOOC « Bioinformatique : génomes et algorithmes »
## Liste des algorithmes 

* Comptage des nucléotides : nombre de A, de C, de G, de T, nombre total et calcul des fréquences

* Promenade sur l’ADN (DNA walk) : 
  * tracé type « tortue » dans les 4 directions nord, sud, est, ouest en fonction du nucléotide rencontré ;
  * tracé « compressé » : un segment tous les n segments élémentaires

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
