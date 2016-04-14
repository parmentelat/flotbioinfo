
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # Traduction d'ADN en ARN

# Dans ce complément nous allons implémenter l'algorithme très simple qui consiste à traduire un brin d'ADN dans le brin d'ARN correspondant, après la cellule habituelles de compatibilité python2/python3&nbsp;:

# In[ ]:

# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division


# ### L'algorithme

# Ce traitement est évidemment très simple; une première version naïve consiste à créer une chaîne vide, et à la remplir au fur et à mesure. Pour faire cela nous allons utiliser l'opérateur `+` sur les chaînes, qui permet de créer une nouvelle chaîne comme on le voit ici&nbsp;:

# In[ ]:

###OFF # à partir de deux chaines
###OFF ch1 = "abc"
###OFF ch2 = "def"
###OFF # en faisant + on obtient la concaténation des deux chaines
###OFF bout_a_bout = ch1 + ch2
###OFF print(bout_a_bout)


# In[ ]:

###OFF # remarquez que les deux chaines de départ sont intactes
###OFF print("ch1:", ch1, "ch2:", ch2)


# Notez également que python propose un raccourci `+=` qui se comporte comme ceci&nbsp;:

# In[ ]:

###OFF # en partant d'une chaine
###OFF chaine = "ATGC"
###OFF # on peut facilement y ajouter à la fin
###OFF chaine += "CGAT"
###OFF # maintenant chaine contient les deux morceaux 
###OFF print(chaine)


# Grâce à cette opération de concaténation sur les chaines on peut procéder simplement comme ceci&nbsp;:

# In[ ]:

def traduction_adn_arn(adn):
    """"
    Traduit un brin d'ADN en ARN en remplaçant toutes
    les occurrences de T en U
    """
    arn = ""
    for nucleo in adn:
        # traduire une Thymine en Uracile
        if nucleo == 'T':
            arn += "U"
        else:
            arn += nucleo
    return arn


# Ainsi par exemple&nbsp;:

# In[ ]:

###OFF adn = "ATTCGATCGGGTATTACG"
###OFF arn = traduction_adn_arn(adn)
###OFF print(arn)


# ### Mesures de performance (avancé)

# Cette section est optionnelle et s'adresse à ceux d'entre vous qui ont des notions de python un peu plus développées que ce que nous avons pu couvrir jusqu'ici. 
# 
# J'attire votre attention sur le module `timeit` qui permet de mesurer les performances d'un fragment de code. Par exemple pour voir le temps que prend cette fonction de traduction nous pourrions écrire&nbsp;:

# In[ ]:

###OFF # importer le module timeit qui fait des mesures de performance
###OFF import timeit
###OFF 
###OFF # un échantillon un peu gros : 400 000 nucléotides
###OFF gros_adn = 10**5 * 'ACGT' 
###OFF 
###OFF print(timeit.timeit('traduction_adn_arn(gros_adn)', 
###OFF                     "from __main__ import traduction_adn_arn, gros_adn",
###OFF                     number=10))


# Ce qui dans mon environnement imprime de l'ordre de `0.5` (en secondes), qui nous dit que pour évaluer 10 fois (c'est le propos de `number=10`) l'appel à `traduction_adn_arn(gros_adn)`, l'interpréteur prend environ une demi-seconde.
# 
# Le deuxième argument à `timeit`, dans notre cas `from __main__ import traduction_adn_arn, gros_adn`, permet de rendre les deux identificateurs dont nous avons besoin (la fonction et l'échantillon) visibles à `timeit`. 
