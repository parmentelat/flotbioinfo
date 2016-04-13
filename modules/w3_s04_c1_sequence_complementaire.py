
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # Calcul de la séquence complémentaire inverse

# Commençons comme d'habitude avec ceci&nbsp;:

# In[ ]:

# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division


# ##### Fonction `complementaire` sur un seul nucléotide

# Pour calculer la séquence complémentaire inverse, nous commençons par nous définir une fonction `complementaire` qui renvoie le nucléotide complémentaire&nbsp;:

# In[ ]:

# le nucleotide complementaire
def complementaire(nucleo):
    if   nucleo == 'A': return 'T'
    elif nucleo == 'C': return 'G'
    elif nucleo == 'G': return 'C'
    elif nucleo == 'T': return 'A'


# Ainsi par exemple&nbsp;:

# In[ ]:

complementaire('A')


# ##### La logique de notre calcul

# On va maintenant pouvoir calculer la séquence complémentaire inverse. Pour cela on va
# * créer une **liste** de nucléotides qui va accumuler le résultat; l'avantage d'une liste est qu'on peut y insérer des éléments où on veut, et donc en partculier au début;
# * balayer la séquence de départ dans le sens "normal", mais insérer le nucléotide complémentaire **au début** de la liste de résultats, de façon à inverser le résultat par rapport à la chaine;
# * enfin traduire la liste en chaine; on pourrait sans doute se passer de cette étape d'ailleurs, car pour l'essentiel ce qu'on peut faire sur une chaine on peut le faire sur une liste de caractères, mais bon soyons homogènes.

# ##### Digression: traduire une liste en chaine

# Pour cette dernière étape, nous allons utiliser une astuce très fréquente dans les programmes python. Il s'agit de la méthode `join` qui est disponible sur les chaines. Voyons quelques exemples&nbsp;:

# In[ ]:

# la méthode join sur une chaine
"+".join(["spam", "eggs", "bacon"])


# Comme on le voit, la chaine sur laquelle on appelle (on dit aussi on envoie) la méthode `join` est utilisée pour lier (joindre) les différents morceaux. 
# 
# Aussi par extension si on envoie `join` à une chaine vide, on réalise *de facto* une conversion de liste en chaine, comme ceci&nbsp;:

# In[ ]:

"".join(["s", "p", "a", "m"])


# ##### Tout ensemble

# Tous ces morceaux mis bout à bout nous donnent le code suivant pour calculer la chaine complémentaire inversée d'un brin d'ADN&nbsp;:

# In[ ]:

def complementaire_inversee(adn):
    """
    Calcule la séquence complémentaire (A->T, etc...) et
    inversée (les premiers sont les derniers)
    d'un brin d'ADN
    """
    # la liste des nucléotides résultats
    liste_resultat = []
    # on parcourt l'entrée dans le *bon* sens
    for nucleo in adn:
        # mais en insérant les bases **au début**
        # du résultat ce qui permet l'inversion
        liste_resultat.insert(0, complementaire(nucleo))
    # il nous reste à transformer la liste en chaine
    return "".join(liste_resultat)


# ##### Exemples

# En partant de l'exemple utilisé dans la vidéo et les transparents&nbsp;:

# In[ ]:

from samples import slide_complement
print(slide_complement)


# In[ ]:

# avec lequel on obtient alors le résultat attendu
complementaire_inversee(slide_complement)


# Ou encore sur un exemple un peu plus court&nbsp;:

# In[ ]:

complementaire_inversee("TAGCATCG")

