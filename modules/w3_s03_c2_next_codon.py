
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # `next_start_codon` et `next_stop_codon`

# Souvenons-nous à présent de l'algorithme de recherche de régions codantes que nous avons vu dans la séquence précédente, et dans lequel nous avions eu besoin de deux fonctions accessoires pour rechercher les codons Start et Stop. Voici le code que nous avions utilisé à ce moment-là, et qui utilise les concepts que nous venons de voir dans le complément sur la recherche de chaines en python.

# Mais n'oublions pas notre cellule usuelle&nbsp;:

# In[ ]:

# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division


# ### L'opérateur `%` pour le calcul des modulos

# Dans le code suivant nous utilisons l'opérateur `%` qui calcule le modulo (ou le reste de la division) entre deux nombres. Par exemple

# In[ ]:

# l'opérateur % permet de calculer le modulo 
print("le reste de la division de 25 par 10 vaut", 25 % 10)


# ### L'instruction `continue`

# Notre code utilise également l'instruction `continue`, qui permet d'interrompre le code de boucle courant (ici nous sommes dans un `while`) et de passer directement à l'itération suivante de la boucle.

# In[ ]:

# un exemple d'instruction `continue`
# une boucle englobante qui itère sur les nombres de 0 à 4
for i in range(5):
    # mais on ignore les multiples de 3
    # et dans ce cas on passe directement au i suivant
    if i % 3 == 0:
        continue
    print("traitement de", i)    


# ### `next_start_codon` et la recherche d'un triplet sur une phase

# Nous pouvons à présent écrire le code de `next_start_codon`&nbsp;:

# In[ ]:

# rappelons quel est le codon START
start_codon = "AUG"


# In[ ]:

# la fonction utilisée dans la recherche de régions codantes
def next_start_codon(adn, indice):
    """
    localise le prochain START en commençant à 
    indice et sur la même phase 
    renvoie None s'il n'y en a plus
    """
    # on commencer à l'indice en question
    courant = indice
    # tant qu'on trouve un START
    while True:
        # on cherche un START à partir de la position
        courant = adn.find(start_codon, courant)
        # il n'y a plus rien à chercher
        if courant == -1:
            return None
        # si on n'est pas sur la même phase que `indice`
        # on ignore cet endroit
        if (courant-indice) % 3 != 0:
            # dans ce cas il faut incrémenter sinon 
            # on reste sur place
            courant += 3
            # et on recherche plus loin
            continue
        # sinon, il y a un match sur la bonne phase
        return courant
    # si on est ici c'est qu'il n'y a plus rien à trouver
    return None


# Pour nous convaincre que cette fonction fait bien ce qu'on attend d'elle, voici un petit test qui devrait couvrir la majorité des cas&nbsp;:

# In[ ]:

adn = "AUGCGAUGUAUGCGUGCAGCUGCUAGCUCGUAAUGUCGUCAUGGAUCAUCGAUCAUGG"

for phase in 0, 1, 2:
    print("PHASE", phase)
    next = phase
    while next is not None:
        next = next_start_codon(adn, next)
        if next is not None:
            print("trouvé à l'indice", next, adn[next:next+3])
            next += 3


# ##### `next_stop_codon` et la recherche de 3 triplets sur une phase

# Sur un modèle très similaire, nous pouvons écrire à présent `next_stop_codon`&nbsp;:

# In[ ]:

import re
# on rappelle la définition de re_stop
# pour chercher 'UAA' ou 'UAG' ou 'UGA', on utilise le ou logique |
re_stop = re.compile("UAA|UAG|UGA")


# In[ ]:

def next_stop_codon(adn, indice):
    """
    localise le prochain START en commençant à 
    indice et sur la même phase 
    renvoie None s'il n'y en a plus
    """
    # on commencer à l'indice en question
    courant = indice
    # tant qu'on trouve un START
    while True:
        # on cherche un STOP à partir de la position
        match = re_stop.search(adn, courant)
        # il n'y a plus rien à chercher
        if match is None:
            return None
        # si on n'est pas sur la même phase que `indice`
        # on ignore cet endroit
        courant = match.start()
        if (courant-indice) % 3 != 0:
            courant += 3
            continue
        # sinon, il y a un match sur la bonne phase
        return courant
    # si on est ici c'est qu'il n'y a plus rien à trouver
    return None


# Et à nouveau on peut tester cette fonction sommairement&nbsp;:

# In[ ]:

print(adn)
for phase in 0, 1, 2:
    print("PHASE", phase)
    next = phase
    while next is not None:
        next = next_stop_codon(adn, next)
        if next is not None:
            print("trouvé à l'indice", next, adn[next:next+3])
            next += 3

