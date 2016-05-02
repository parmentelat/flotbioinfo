# À intégrer W3

## regexp

un notebook d'exercice `w3-e2-regexp-serine.ipynb` 

***

# Ongoing : exos

* **TODO** w3-e1-count-stop-codons.ipynb : écrire une fonction qui compte les codons STOP dans une séquence d'ADN
***

# TODO W3

## Séquence 2


Il me semble que l’algorithme de prédiction de gène est incorrect : une fois trouvé un stop, tu recherches le prochain stop en phase et tu testes la distance entre les deux. Si cette distance est trop faible, tu cherches un stop plus loin. Je pense que de ce fait, tu prédis des ORF qui contiennent un ou plusieurs stops, ce qui n’est pas correct. Pour éviter cela, il faudrait prendre ce 2e stop comme nouveau stop initial. Ton implémentation de l’algorithme peut avoir tendance à surprédire par la concaténation de très courtes ORFs.

15000 gènes sur les 6 phases de B. subtilis, c’est 4 fois trop.

> oui en effet on considère des ORF avec possiblement un ou même des STOP dedans; mais si on ne fait pas ça comment on va pouvoir trouver des acides aminés correspondants au STOP ? En tous cas il y a clairement un truc que je n'ai pas compris..

**TODO** ne plus considérer les STOP 
**TODO** publier nouveau nombre de prédictions

# TODO W4

## Séquence 9

**TODO** Ajouter un mot sur les performances; un rapide benchmark montre un ratio **de 1 à 200** entre mon code python et une implémentation en C++

