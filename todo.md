# process

**OK** Utiliser la machine de notebooks de prod et non plus connect

# W1

# Sur le fond

Eviter de donner l’exemple d’une séquence retrouvée avec le mot clé « breast cancer », mais un nom de bactérie. Le mieux est d’appliquer l’algorithme sur Borrelia burdorferi, car on devrait voir la courbe de l’évolution du ration passer de valeurs négatives à des valeurs positives au point de rebroussement visible sur le DNA walk

> le truc c'est que j'ai déjà montré Borrelia juste avant dans ce notebook.
> je voulais juste leur montrer qu'ils pouvaient aller chercher des trucs aux-mêmes, mais avec d'autres données (en + il me semble que borrelia c'est très gros) 

 
 **TODO** 1.7 : montrer fetch sur le + petit des 2 exemples
supprimer breast cancer + pacific...
 
**TODO** 1.10 : reprendre borrelia comme seul exemple
on doit voir d'abord en dessous, puis au dessus
 
**TODO** robustifier le fetch ou l'enlever; 
en attente d'une confirmation de Benjamin sur un firewall éventuel

1-7-1 et 1-10-1

Christelle: J'ai trouvé borrelia burgdorferi : 
http://www.ebi.ac.uk/ena/data/view/ACL34321

* CP001273
longueur 24159 


* ACL34321
fetch OK mais seulement 2031 nucleotides
le fetch depuis la plateforme ne fonctionne pas par contre; firewall ?


 
# W3

## Séquence 2


Il me semble que l’algorithme de prédiction de gène est incorrect : une fois trouvé un stop, tu recherches le prochain stop en phase et tu testes la distance entre les deux. Si cette distance est trop faible, tu cherches un stop plus loin. Je pense que de ce fait, tu prédis des ORF qui contiennent un ou plusieurs stops, ce qui n’est pas correct. Pour éviter cela, il faudrait prendre ce 2e stop comme nouveau stop initial. Ton implémentation de l’algorithme peut avoir tendance à surprédire par la concaténation de très courtes ORFs.

15000 gènes sur les 6 phases de B. subtilis, c’est 4 fois trop.

> oui en effet on considère des ORF avec possiblement un ou même des STOP dedans; mais si on ne fait pas ça comment on va pouvoir trouver des acides aminés correspondants au STOP ? En tous cas il y a clairement un truc que je n'ai pas compris..

**TODO** ne plus considérer les STOP 
**TODO** publier nouveau nombre de prédictions

# W4

## Séquence 9

**TODO** Ajouter un mot sur les performances; un rapide benchmark montre un ratio **de 1 à 200** entre mon code python et une implémentation en C++

# Exos
**TODO** voir si on peut faire un ou deux des exos
* W2 / exo 1
* W3 / exo 1