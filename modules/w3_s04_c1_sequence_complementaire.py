
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # Calcul de la séquence complémentaire inverse

# Commençons comme d'habitude avec ceci&nbsp;:

# In[28]:

# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division


# ### Le  `complement` d'un nucléotide

# Pour calculer la séquence complémentaire inverse, nous commençons par nous définir un dictionnaire `complement` qui renvoie le nucléotide complémentaire&nbsp;:

# In[39]:

# le nucléotide complémentaire
complement = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A',
}


# Ainsi par exemple&nbsp;:

# In[40]:

complement['A']


# ### La logique de notre calcul

# On va maintenant pouvoir calculer la séquence complémentaire inverse. Pour cela on va
# * calculer la **liste** des nucléotides complément, dans l'ordre initial, à l'aide d'une compréhension;
# * retourner la liste en place grâce à la fonction python `reversed`;
# * enfin traduire cette liste en chaine.

# ### Digression: traduire une liste en chaine

# Pour cette dernière étape, nous allons utiliser une astuce très fréquente dans les programmes python. Il s'agit de la méthode `join` qui est disponible sur les chaines. Voyons quelques exemples&nbsp;:

# In[31]:

# la méthode join sur une chaine
"+".join(["spam", "eggs", "bacon"])


# Comme on le voit, la chaine sur laquelle on envoie la méthode `join` est utilisée pour lier (joindre) les différents morceaux, d'où le nom de cette méthode.
# 
# Aussi par extension, si on envoie `join` à une **chaine vide**, on réalise *de facto* une conversion de liste en chaine, comme ceci&nbsp;:

# In[41]:

"".join(["s", "p", "a", "m"])


# ### Tout ensemble

# Tous ces morceaux mis bout à bout nous donnent le code suivant pour calculer la chaine complémentaire inversée d'un brin d'ADN&nbsp;:

# In[33]:

def complementaire_inversee(adn):
    """
    Calcule la séquence complémentaire (A->T, etc...) et
    inversée (les premiers sont les derniers)
    d'un brin d'ADN
    """
    # la liste des nucléotides complémentaires
    liste = [ complement[nucleo] for nucleo in adn]
    # la même liste mais inversée
    liste = reversed(liste)
    # il ne reste plus qu'à retransformer en chaine
    return "".join(liste)

