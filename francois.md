# W1

# Sur le fond

Eviter de donner l’exemple d’une séquence retrouvée avec le mot clé « breast cancer », mais un nom de bactérie. Le mieux est d’appliquer l’algorithme sur Borrelia burdorferi, car on devrait voir la courbe de l’évolution du ration passer de valeurs négatives à des valeurs positives au point de rebroussement visible sur le DNA walk

> le truc c'est que j'ai déjà montré Borrelia juste avant dans ce notebook.
> je voulais juste leur montrer qu'ils pouvaient aller chercher des trucs aux-mêmes, mais avec d'autres données (en + il me semble que borrelia c'est très gros) 

 
## Semaine 3


## Séquence 2


Il me semble que l’algorithme de prédiction de gène est incorrect : une fois trouvé un stop, tu recherches le prochain stop en phase et tu testes la distance entre les deux. Si cette distance est trop faible, tu cherches un stop plus loin. Je pense que de ce fait, tu prédis des ORF qui contiennent un ou plusieurs stops, ce qui n’est pas correct. Pour éviter cela, il faudrait prendre ce 2e stop comme nouveau stop initial. Ton implémentation de l’algorithme peut avoir tendance à surprédire par la concaténation de très courtes ORFs.

15000 gènes sur les 6 phases de B. subtilis, c’est 4 fois trop.

> oui en effet on considère des ORF avec possiblement un ou même des STOP dedans; mais si on ne fait pas ça comment on va pouvoir trouver des acides aminés correspondants au STOP ? En tous cas il y a clairement un truc que je n'ai pas compris..

# W4



## Séquence 4.9

Remarquez que le la valeur qui nous intéresse au final,