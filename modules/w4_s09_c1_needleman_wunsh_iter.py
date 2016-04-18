
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # Algorithme de Needleman et Wunsch

# ## Version Itérative

# In[34]:

# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division


# ### Les coûts

# Reprenons les fonctions de coûts comme on les avait définies dans la séquence précédente&nbsp;:

# In[35]:

# la fonction d'insertion la plus simple possible
def insertion_cost(base):
    return 1


# In[36]:

# la fonction de substitution la plus simple possible
def substitution_cost(base1, base2):
    return 1 if base1 != base2 else 0


# ### Parcours en diagonale

# Avant de nous lancer, voyons comment on peut implémenter le parcours "en diagonale" tel qu'il est décrit dans la vidéo.
# 
# Pour cela, remarquons que les points qui sont sur une diagonale vérifient tous $i + j = c$, et qu'en augmentant la constante c on balaie les diagonales les unes après les autres.
# 
# ![Parcours en diagonale](media/diagonal.png)

# Ici encore on doit faire un peu attention aux poteaux, la valeur maximale de la constante `c` vaut donc la somme des longueurs des deux chaines en entrée **inclusivement**. Et souvenez-vous que `range(n)` ne couvre que jusqu'à `n-1` inclus, c'est pourquoi nous utilisons deux fois `range(n + 1)` dans ce balayage. 

# On peut donc balayer le tableau rectangulaire correspondant aux couples $(i, j)$ de la vidéo comme ceci&nbsp;:

# In[37]:

# le squelette du balayage diagonal
def sweep(adn1, adn2):
    len1 = len(adn1)
    len2 = len(adn2)
    
    # il nous faut aller jusqu'à len1 + len2 inclus
    for c in range(len1 + len2 + 1):
        print(10*'*', "diagonale c =", c)
        # ici aussi on veut les points sur les deux bords, 
        # il nous faut ajouter 1 à l'appel de range
        for i in range(c + 1):
            # on déduit j de c et i
            j = c - i
            # on ne considère que ceux qui tombent dans le rectangle 
            # ici encore on veut garder les bords, d'où les <=
            if 0 <= i <= len1 and 0 <= j <= len2:
                print(i, j)


# Si on se fixe en entrées respectivement `ABC` et `AC` ![](media/nw-indices.png)

# In[38]:

# un simple balayage des points du rectangle 
###OFF sweep("ABC", "AC")


# ### Tableaux à double entrée

# Pour écrire la première phase, il nous manque seulement un petit point de détail. La première phase de l'algorithme doit élaborer un tableau à double entrée comme résultat de ce balayage. Nous n'avons encore pas manipulé de tel tablea  en python, pour la raison que ceci n'est pas dans le langage, en tous cas pas au sens où on pourrait l'entendredans des langages comme C ou C++.
# 
# Il existe plusieurs solutions pour obtenir un résultat voisin. La première consiste à créer des listes de listes. C'est assez simple, ça se présente comme ceci&nbsp;:

# ##### Une liste de listes

# In[39]:

# créer un tableau double comme une liste de listes
rectangle = [
    [0, 1, 2],
    [10, 11, 12],
]


# Nous savons déjà comment manipuler cet objet puisque en tant que liste de listes, on peut accéder, au premier niveau, à une liste simple&nbsp;:

# In[40]:

# un niveau d'indexation
rectangle[1]


# qui peut être indexé à son tour&nbsp;:

# In[41]:

# deux niveaux d'indexation
rectangle[1][2]


# Cette première méthode fonctionne bien, et elle a l'avantage d'utiliser une syntaxe parlante. Cependant elle demande un peu de soin pour l'initialisation. Voici la bonne façon d'initialiser une telle structure&nbsp;:

# In[42]:

def init_costs(len1, len2):
    """
    Initialise un tableau de len1 + 1 listes
    de chacune len2 + 1 éléments 
    initialisés à 0
    """
    return [ [ 0 for j in range(len2 + 1)] for i in range(len1 + 1)]


# Ainsi, si on se met dans le cas de notre figure, on obtient bien&nbsp;:

# In[43]:

# avec les données de la figure
###OFF len1 = 3
###OFF len2 = 2
###OFF 
###OFF costs = init_costs(len1, len2)
###OFF 
###OFF print(costs)


# ##### Autre méthode

# Pour ceux qui seraient curieux d'en apprendre un peu plus sur python, nous verrons à la fin de ce complément une autre méthode pour représenter de tels tableaux, à base de dictionnaires et de tuples. Mais dans l'immédiat, passons tout de suite à l'implémentation de la première phase.

# ### Première phase

# Nous avons à présent tout ce qu'il nous faut pour écrire la première phase de l'algorithme itératif de Needleman et Wunsch&nbsp;:

# In[44]:

def phase1(adn1, adn2):
    """
    Première phase de Needleman et Wunsch itératif
    Élabore itérativement le tableau des coûts 
      par un parcours en diagonale
    On obtient un tableau de taille 
      [len(adn1) + 1] x [len(adn2) + 1]
    Renvoie le tableau en valeur
    """
    # initialisations
    len1 = len(adn1)
    len2 = len(adn2)
    # le tableau est initialisé à zéro
    costs = init_costs(len1, len2)

    # le parcours en diagonale - cf ci-dessus
    for c in range(len1 + len2 + 1):
        for i in range(c + 1):
            # on déduit j de c et i
            j = c - i
            # on ne considère que ceux qui tombent dans le rectangle 
            if 0 <= i <= len1 and 0 <= j <= len2:
                if j == 0:     # sur un bord : insertion
                    costs[i][j] = sum(insertion_cost(base) for base in adn1[:i])
                elif i == 0:   # l'autre bord : insertion
                    costs[i][j] = sum(insertion_cost(base) for base in adn2[:j])
                else:          # au milieu
                    costs[i][j] = min(
                        # substitution
                        costs[i-1][j-1] + substitution_cost(adn1[i-1], adn2[j-1]),
                        # insertion
                        costs[i][j-1] + insertion_cost(adn2[j-1]),
                       # insertion
                        costs[i-1][j] + insertion_cost(adn1[i-1]))
    # on renvoie le résultat
    return costs


# ### La distance

# Remarquez que le la valeur qui nous intéresse au final, dans un tel tableau de coûts, est le dernier élément de la dernière colonne; pour y accéder on peut tirer profit des indices négatifs en python, et notamment du fait que `liste[-1]` retourne le dernier élément de `liste`&nbsp;:
# 

# In[45]:

# une liste
l = [0, 12, 47]
l[-1]


# In[46]:

# et donc du coup on peut définir 
def distance(adn1, adn2):
    return phase1(adn1, adn2)[-1][-1]


# ### Quelques exemples

# Ce qui nous donne par exemple, pour reprendre d'abord les mêmes exemples qu'avec la version récursive&nbsp;:

# In[47]:

###OFF phase1("ACTG", "ACTC")


# In[48]:

###OFF phase1("ACGTAGC", 
###OFF        "ACTGTAGC")
#          ^           


# In[49]:

###OFF phase1("ACTGCCAAC", "ACTGCGCAAC")


# ### Performances

# Avec cette version itérative on peut maintenant lancer le calcul sur des données sensiblement plus grosses&nbsp;:

# In[50]:

###OFF from samples import sample_week4_sequence9 as original
###OFF print("longueur de sample", len(original))
###OFF print("original[600]=", original[600])


# Si on crée artificiellement de petites différences en insérant et modifiant légèrement l'échantillon&nbsp;:

# In[51]:

# on insére un 'C' à l'indice 300 et on remplace le 'A' à l'indice 6000 par un 'G'
###OFF fake = original[:300] + 'C' + original[300:600] + 'G' + original[601:]

###OFF costs = phase1(original, fake)
###OFF print("On trouve une distance de", costs[-1][-1])


# Comme vous le voyez l'algorithme est déjà plus efficace, mais comme il est quadratique (on doit calculer en gros $n^2^ valeurs) cette entrée de 800+ bases aboutit déjà à un calcul de quelques secondes. 

# ### Phase 2

# Pour la deuxième phase, nous allons simplement calculer deux chaines de caractères qui vont nous permettre de mettre en évidence les différences entre les deux brins d'ADN en entrée. Comme il n'est pas très simple d'utiliser des couleurs ou autres différences de rendu typographique, nous allons imprimer quelque chose comme ceci&nbsp;:
# 
#     ACCTC-TGTATCT*A*TTCGGCATCGATCAT
#     ACCTCGTGTATCT*C*TTCGGCATC-ATCAT
# 
# Comme on le voit sur cet exemple&nbsp;:
#   * les insertions sont mises en évidence avec un caractère `-` dans la chaine la plus courte,
#   * et les substitutions sont mises en évidence avec deux caractères `*` autour de l'emplacement concerné.

# ON va commencer à écrire une fonction utilitaire qui ajoute les caractères `*` autour d'un caractère lorsque c'est nécessaire (i.e. si le paramètre `same` est faux)&nbsp;:

# In[61]:

# une fonction utilitaire qui ajoute les '*' 
# autour d'un caractère lorsque 'same' est faux
def outline(char, same=True):
    return char if same else "*{}*".format(char)


# Voici à présent le code de la fonction `phase2`, qui retourne les deux chaines à afficher l'une au dessous de l'autre. Pour des raisons d'efficacité on récolte les résultats dans des listes (`r1` et `r2`) qui sont de plus construites à l'envers, du fait du sens du parcours de la fin vers le début, et qui sont remises à l'endroit et traduites en chaines avant d'être retournées à l'appelant&nbsp;:

# In[52]:

# un exemple de phase2
def phase2(adn1, adn2, costs):
    """
    À partir de deux brins d'ADN, et de leur tableau de coûts tels que
    calculé dans la première phase, on retourne deux chaines destinées 
    à être affichées une au dessus de l'autre pour visualiser les différences
    
    Les insertions sont remplacées par le caractère -, et les substitutions
    sont montrées avec des * 
    """
    i = len(adn1)
    j = len(adn2)
    # les résultats, mais sous forme de listes de chaines, et à l'envers
    r1 = []
    r2 = []
    ### le parcours à proprement parler
    # on ne s'arrête que quand i==0 ET j==0
    while i > 0 or j > 0:
        # la valeur courante
        c = costs[i][j]
        # si on est au bord, les formules en i-1 ou j-1 
        # ne vont pas faire ce qu'on veut, il faut traiter 
        # ces cas à part
        if i == 0:                  # bord = insertion
            r1.append("-")
            j -= 1
            r2.append(adn2[j])
        elif j == 0:                # bord = insertion
            i -= 1
            r1.append(adn1[i])
            r2.append("-")
        # dans le milieu du tableau on regarde de quelle direction nous vient le minimum
        elif c == costs[i-1][j-1] + substitution_cost(adn1[i-1], adn2[j-1]):  # substitution
            # s'agit-t-il d'une vraie substitution ? 
            same = adn1[i-1] == adn2[j-1]
            i -= 1
            r1.append(outline(adn1[i], same))
            j -= 1
            r2.append(outline(adn2[j], same))
        elif c == costs[i][j-1] + insertion_cost(adn2[j-1]):    # insertion
            r1.append('-')
            j -= 1
            r2.append(adn2[j])
        elif c == costs[i-1][j] + insertion_cost(adn1[i-1]):    # insertion
            i -= 1
            r1.append(adn1[i])
            r2.append('-')

    # à ce stade il nous reste à retourner les listes, et les transformer en chaines
    s1 = "".join(reversed(r1))
    s2 = "".join(reversed(r2))
    return s1, s2


# In[53]:

# on peut maintenant écrire une fonction de commodité
def needleman_wunsch(adn1, adn2):
    # on calcule les coûts avec la phase1
    costs = phase1(adn1, adn2)
    # on calcule la distance
    d = costs[-1][-1]
    # on passe à la phase 2
    s1, s2 = phase2(adn1, adn2, costs)
    # on affiche le résultat
    print("distance = ", d)
    print(s1)
    print(s2)


# In[54]:

# et sur un exemple cela donne
sample1 = "ACCTCTGTATCTATTCGGCATCGATCAT"
sample2 = "ACCTCGTGTATCTCTTCGGCATCATCAT"

###OFF needleman_wunsch(sample1, sample2)


# ******

# ### Double tableau: un dictionnaire indexé sur des tuples (Supplément avancé)

# Il existe une autre méthode pour modéliser un tableau à double entrée, qui est plus *pythonique*, et qui consiste à utiliser un dictionnaire indexé sur des tuples. Nous avons croisé ici et là la notion de tuple déjà, voici quelques mots pour préciser un peu ce concept.

# ##### Objets mutables et immutables

# Pour rester simple, voyons pour commencer la notion d'objet **mutable**. Un objet en python est dit mutable lorsqu'on peut le modifier; par exemple, une **liste est mutable** dans le sens où on peut modifier **en place** un de ses éléments. Par exemple&nbsp;:

# In[55]:

# une liste est un objet mutable
list1 = [0, 1, 2]
# si une deuxième variable pointe vers la liste
list2 = list1
# et qu'on modifie la première liste
list1[1] = 100
# alors on a modifié les deux variables
###OFF print("list1=", list1, "list2=", list2)


# A contrario, **une chaine** par exemple est un objet **immutable**. Une chaine ne peut pas être modifiée&nbsp;:

# In[56]:

# une chaine est immutable
chaine = "abc"
# si on essaie de changer un caractere on reçoit une exception
###OFF try:
###OFF     chaine[1] = 'Z'
###OFF except Exception as e:
###OFF     print("OOPS", e)


# On pourrait, bien entendu, réaffecter la variable `chaine` à une autre chaine, mais ce n'est pas le même concept.

# ##### Une clé de dictionnaire doit être immutable

# Remarquons pour commencer qu'un dictionnaire ne peut, pour des raisons d'implémentation, utiliser que des clés **immutables**&nbsp;:

# In[57]:

# un dictionnaire vide
d = {}

# on peut insérer une clé qui est une chaine, car la chaine est immutable
d['abc'] = 123

# mais on ne peut pas utiliser une clé qui est une liste
###OFF try:
###OFF     d[ [1, 2] ] = 123
###OFF except Exception as e:
###OFF     print("OOPS", e)
    
# à ce stade d a une seule clé 'abc'
###OFF print(d)


# C'est ici qu'intervient le tuple. C'est une structure qui ressemble beaucoup à une liste, en ce sens qu'on peut y mettre une collection ordonnée d'objets. 

# In[58]:

# un tuple s'écrit avec des virgules - et, si on veut des parenthèses
###OFF t1 = (1, "abc")
###OFF print("t1", t1)

###OFF t2 = 2, "def"
###OFF print("t2", t2)


# Mais le tuple est un objet **immutable**, et du coup on peut s'en servir comme clé dans un dictionnaire&nbsp;:

# In[59]:

# un tableau à double entrée comme un dictionnaire de tuples
###OFF costs = {}
###OFF costs[ (100, 100) ] = 'abc'
###OFF costs[ (1000, 0) ] = [1, 2, 3]
###OFF print("le dictionnaire", costs)


# In[60]:

# on retrouve les données comme un dictionnaire normal
###OFF costs[ (100, 100)]


# Il s'agit d'une structure très pratique, et efficace, pour stocker des tableaux a multiples entrées, notamment dans les cas où c'est difficile de prévoir à l'avance la taille - typiquement lorsque le tableau a plein de trous.

# À titre d'exercice, vous pouvez vous amuser à reprendre le code de ce complément pour utiliser un dictionnaire de tuples plutôt que la liste de listes que nous avons utilisée.
