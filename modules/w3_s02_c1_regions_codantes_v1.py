
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # Recherche de régions codantes sur une phase

# Dans ce complément, nous allons écrire en python l'algorithme décrit dans la vidéo, qui recherche une région codante dans un brin d'ADN. Dans cette première version nous nous concentrons sur une seule phase. Souvenez-vous qu'on peut voir trois phases sur un brin d'ADN, selon que l'on regroupe les bases en triplets en commençant à l'indice 0, 1 ou 2.

# Mais comme toujours, commençons par les formules magiques

# In[1]:

# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division


# ### Recherche de marqueurs

# Comme dans la vidéo, nous supposons que nous disposons de fonctions toutes faites pour la recherche de codons **Start** ou **Stop**. Pour l'instant nous les importons d'un autre module, mais rassurez-vous, nous verrons dès la prochaine séquence comment écrire nous-mêmes ces fonctions.

# In[2]:

# on importe les fonctions next_start_codon et next_stop_codon 
# d'une séquence prochaine
from w3_s03_c2_next_codon import next_start_codon, next_stop_codon


# On rappelle que&nbsp;:
#  * les indices en python commencent à 0
#  * le codon **Start** est `ATG`
#  * les codons **Stop** sont `TAA` ou `TAG` ou `TGA`

# On précise par ailleurs que ces deux fonctions&nbsp;:
#   * attendent en argument un brin `adn` et un `indice` de départ,
#   * et retournent, soit l'indice de la prochaine occurrence à partir (y compris) de `indice` **et sur la même phase**, ou `None` s'il n'y a plus de correspondance au delà de `indice`
#  
# Ainsi par exemple&nbsp;:

# In[3]:

# on trouve bien START car on part de l'indice 0 
# et ATG se trouve à l'indice 6, donc sur la même phase
next_start_codon("CGTACGATG", 0)


# In[4]:

# par contre ici on ne trouve rien 
# car l'indice de départ ne correspond pas à la phase 
# sur laquelle se trouve ATG
next_start_codon("CGTACGATG", 1)


# ### L'instruction `break`

# Notre code va utiliser l'instruction `break`, qui permet d'interrompre brutalement une boucle, et donc de passer à l'instruction après la boucle. Cette construction est souvent utilisée en conjonction avec une boucle **sans fin**, comme dans cet exemple&nbsp;:

# In[5]:

# une boucle apparemment sans fin
compteur = 1
###OFF while True:
###OFF     # on mulitplie le compteur par 2
###OFF     compteur += compteur
###OFF     # une fois arrivé à 100 on sort de la boucle
###OFF     if compteur >= 100:
###OFF         break
###OFF     print("compteur = ", compteur)
###OFF print("après la boucle")


# ### L'algorithme à proprement parler

# Une fois tout ceci acquis, nous pouvons écrire une fonction `regions_codantes_une_phase` qui travaille sur un brin d'ADN, et qui va suivre la logique décrite dans la vidéo. Notre fonction va prendre les arguments suivants&nbsp;:
#   * le brin d'ADN
#   * la phase, exprimée comme un entier 0, 1 ou 2
#   * la taille minimale entre 2 deux **Stop**; ce dernier argument sera optionnel, lorsqu'il est omis on prendra comme valeur par défaut 300, comme dans le cours.
#   
# Ce qui nous donne le code suivant&nbsp;:

# In[6]:

# recherche de gènes selon l'heuristique décrite dans la vidéo
# sur une phase seulement
# avec par défaut une longueur minimale de 300
def regions_codantes_une_phase(adn, phase, longueur_minimale=300):
    # on initialise index à la phase; avec next_start_codon
    # et next_stop_codon on reste toujours sur la même phase
    index = phase
    # les résultats sont retournés sous la forme d'une liste 
    # de couples [start_gene, stop_gene]
    genes = []
    # la boucle 
    while True:      # boucle principale
        # on cherche le premier STOP à partir de index
        stop1 = next_stop_codon(adn, index)
        # s'il n'y a plus de stop, on a fini
        if not stop1:
            return genes
        # sinon on cherche un deuxieme stop
        stop2 = stop1 + 3
        # mais il faut qu'il soit assez loin
        while True:  # boucle interne
            stop2 = next_stop_codon(adn, stop2)
            # s'il n'y en a pas on a fini
            if not stop2:
                return genes
            # s'il est assez loin, on peut sortir de la boucle interne
            if stop2 - stop1 >= longueur_minimale:
                break
            # sinon il faut continuer à chercher un STOP
            # pour passer au stop suivant et ne pas retomber a nouveau sur stop2
            stop2 += 3
        # à ce stade on a trouvé un ORF, reste à trouver le bon start
        start = next_start_codon(adn, stop1)
        # s'il n'y en a pas: c'est qu'on ne trouvera plus rien
        # on a fini
        if not start:
            return genes
        # ici c'est un peu subtil
        # tout d'abord rien ne nous dit qu'il y a un codon START entre start1 et start2
        # et même s'il y en a un, rien de nous dit qu'on obtient un gêne assez long
        # donc on reteste la longueur du gêne trouvé et on ne garde que ceux 
        # qui sont assez longs - par rapport à longueur_minimale
        if stop2 - start < longueur_minimale:
            pass
        else:
            # cette fois on a trouvé un genes, on l'ajoute dans les résultats
            genes.append( [start, stop2] )
        # on peut passer à l'ORF suivant
        index = stop2 + 3


