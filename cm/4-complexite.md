

**Complexités**

Complexités en temps, en espace

Complexité asymptotique

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

1





Complexités : plan

[Motivations,](#br3)[ ](#br3)[principes,](#br3)[ ](#br3)[notions](#br3)[ ](#br3)[importantes](#br3)[ ](#br3)[et](#br3)[ ](#br3)[exemples](#br3)

[introductifs](#br3)

[Complexité](#br11)[ ](#br11)[en](#br11)[ ](#br11)[temps](#br11)

[Complexité](#br19)[ ](#br19)[en](#br19)[ ](#br19)[espace](#br19)

[Un](#br22)[ ](#br22)[autre](#br22)[ ](#br22)[exemple](#br22)[ ](#br22)[de](#br22)[ ](#br22)[complexité](#br22)[ ](#br22)[polynomiale](#br22)

[Complexité](#br30)[ ](#br30)[et](#br30)[ ](#br30)[log](#br30)[2](#br30)

[(*)](#br35)[ ](#br35)[Un](#br35)[ ](#br35)[complément](#br35)

[Complexité](#br41)[ ](#br41)[asymptotique](#br41)

[Exprimer](#br48)[ ](#br48)[les](#br48)[ ](#br48)[complexités](#br48)[ ](#br48)[asymptotiques](#br48)[ ](#br48)[des](#br48)[ ](#br48)[itérations](#br48)[ ](#br48)[et](#br48)

[récursions](#br48)

[Synthèse](#br55)

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

2





Motivations

Contexte

un problème à résoudre

\- une question et (au moins) une réponse qui dépend de paramètres : données "en

entrée"

une instance de ce problème qui admet au moins une solution

\- un choix des paramètres, des données d'entrée

un algorithme qui calcule cette solution

\- un algorithme, ou même plusieurs algorithmes

Questions du jour

De **combien de temps** a besoin l'algorithme pour calculer cette solution

?

De **combien d'espace-mémoire** a besoin l'algorithme pour calculer

cette solution ?

Motivations

\- Appuyer sur la touche <enter> ou non ?

\- Appliquer mon algorithme à toute instance de ce problème ?

\- Comment quantifier l’efficacité d’un algorithme ? Mesurer la difficulté de

la résolution d’un problème ?

\- Objectif : choisir, adapter, améliorer, …

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

3





Je calcule la somme de n valeurs

entières

Une instance : un choix de n et des n valeurs du tableau t

Principe d'un algorithme : je parcours le tableau, "du début à la fin",

je lis chaque valeur, je l'accumule dans une variable (initialement

mise à zéro), je retourne cette variable.

def sommer(t : List[int], dim\_t : int) -> int:

res = 0

for i in range(dim\_t):

res = res + t[i]

return res

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

4





Je recherche l’indice d’une valeur parmi

n valeurs stockées dans un tableau

Une instance : un choix de la valeur cherchée, de n et des n valeurs du

tableau t

Principe d'un algorithme : je parcours le tableau à partir de son premier

indice, je compare chaque valeur du tableau à la valeur cherchée, si égalité

je retourne l’indice de cette valeur, sinon je répète ce traitement sur la

valeur suivante. Je renvoie un indice significatif de l’absence si aucune

égalité n’a été satisfaite après le dernier indice du tableau.

def rechercheIterative(val : float, t : List[float], dim\_t: int) -> int:

i = 0

while i < dim\_t:

if val == t[i]:

return i

i = i+1

return -1

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

5





Complexité en temps,

complexité en espace

Quel est le temps nécessaire à la résolution du problème avec un

algorithme ?

Quel est l'espace-mémoire nécessaire à la résolution du problème avec

un algorithme ?

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

6





Complexité ? en temps ? en espace-

mémoire ?

\1. On a **un problème** à résoudre :

\- calculer la somme de n valeurs entières stockées dans un tableau t

\- rechercher (l’indice d’)une valeur dans n valeurs stockées dans un tableau t

\2. On a (au moins) **un algorithme** qui résout ce problème

\- sommer( ) dans sa version itérative codée avec une boucle for

\- rechercheIterative( ) codée avec une boucle while

\3. Combien de **temps** pour calculer la réponse ? Quel est le **coût en temps** de l'algorithme ?

• sommer( )

\- ça **dépend de n** : le nombre de valeurs à sommer

\- a priori, le temps de calcul est une fonction croissante de n

\- OK mais croissante comment ? linéaire ? quadratique ? logarithmique ?

• rechercheIterative( )

\- ça **dépend** de n, de t **et de val** : le nombre de valeurs, de leur ordre et de la valeur à trouver

\- meilleur cas : val est à l’indice 0 et coût indépendant de n

\- pire cas : val est absente de t et coût fonction croissante de n

\4. Combien **d'espace-mémoire** pour calculer la réponse ? Quel est le **coût en espace** de

l'algorithme ?

\- ça **dépend** aussi **de n** : faut déjà réussir à stocker les n valeurs !

\- OK mais quel est l'espace mémoire supplémentaire pour résoudre le problème ?

\- Dépendant ou indépendant de n ? dépendant comment ?

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

7





Paramètres de la complexité

On a un problème à résoudre :

\- calculer la somme de n valeurs entières stockées dans un tableau t

Quels sont les paramètres du coût de sa résolution ?

\1. La taille du problème

\- ce qui caractérise la taille dépend du problème

\- sommer n valeurs entières, rechercher dans n valeurs, trier n valeurs :

taille = n = le nombre de valeurs

\- je calcule l'addition de 2 nombres entiers :

la taille = le nombre de chiffres de chaque opérande, ou le max des 2

\2. Certaines données/entrées du problème : instance du pb

\- je recherche l’indice d’une valeur dans un tableau donné

\- je trie une liste déjà triée vs. je trie une liste « bien mélangée »

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

8





**complexité = f(taille)**

La question : ordre de grandeur pour des très grandes

tailles ?

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

9





**Comment mesurer ce coût ?**

On a (au moins) un algorithme qui résout ce problème

\- sommer dans sa version itérative boucle for

\- rechercheIterative avec sa boucle while

On veut mesurer les coûts en temps d'exécution et en espace-

mémoire.

Mesurer => exécuter l’algorithme pour une **analyse de**

**complexité**

On exécute l'algorithme sur **un modèle de machine**

\- simple : beaucoup de détails d'une véritable exécution sont ignorés

\- mais pas trop simpliste : les résultats et les observations réelles sont

raisonnablement corrélées

\- l'exécution continue a dépendre des données d'entrées : pire cas,

meilleur cas

10

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

\- l’objectif : **dégager des tendances, des ordres de grandeur**





Mener une analyse

de la complexité en temps

Un modèle d’exécution

Analyse du pire temps d'exécution avec le modèle RAM

Modèle vs. pratique ?

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

11





Un modèle de complexité

pour mesurer le coût en temps d'un

algorithme

Toutes les instructions importantes comptent 1 unité de temps :

1 = affectation = comparaison = opération arithmétique = opération

logique

= accès mémoire = entrées/sorties

Les instructions s’exécutent séquentiellement :

si l'instruction p coûte c1 et l'instruction q coûte c2,

alors la suite d'instructions p, q coûte c1+c2

Coût du branchement conditionnel : if... elif ... else …

inférieur ou égal au coût maximum de chaque branche d'instructions

Coût de la répétition : for i in range(n): corps\_de\_boucle

si le coût de p ne dépend pas de i : n x coût(corps\_de\_boucle)

sinon : la somme des coûts de chacune des n répétitions

Coût de la répétition while(condition): corps\_de\_boucle

dépend du nombre de répétitions, inconnu a priori

on peut cependant majorer ce nombre de répétitions

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

12





Je calcule la somme de n valeurs

entières

Somme itérative avec accumulation

\- une boucle for

\- pas de test if …

\- additions entières, affectations d’entiers, accès (lecture)

éléments d’un tableau, retour, contrôle de boucle for

1 def sommer(t : List[int], n : int ) -> int:

n

n

2

3

4

5

res = 0

for i in range(n):

res = res + t[i]

return res

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

13





Mesurer le coût de sommer(t, n) ?

sommer dans sa version itérative avec "boucle for"

On a un modèle de complexité basé sur :

\- chaque instruction compte 1 unité (de temps)

\- 1 = affectation = comparaison = opération arithmétique = op. logique = ...

\- donc on pourrait/devrait **tout compter** ...

Simplification de la mesure :

on identifie **certaines instructions significatives du temps de**

**traitement**

\- Ici on compte "seulement" les additions de la ligne 4 dans sommer

\- on a autant d'affectations dans res que d'additions

\- on ne compte pas ces affectations,

\- ni les additions cachées dans la mise à jour des indices de la boucle for

\- écart : facteur multiplicatif du nombre d’additions comptées

\- conclusion : **complexité(sommer) = f(nombre d'additions du corps de**

**boucle)**

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

14





C(sommer) = f(nombre d'additions des lignes L3-4)

\3. for in in range(n):

\4.

res = res + t[i]

\- Mesure : comptons les additions

\- Paramètre : n est la taille du problème "sommer n valeurs"

\- L'algorithme sommer effectue 1 addition (L4)

à chacune des n répétitions de la boucle pour (L3-4)

\- La complexité de la sommation séquentielle sommer **: C(n) = n**

L'algorithme itératif sommer

a une **complexité linéaire** en la taille du problème à

résoudre

IMPORTANT : Quelle interprétation ? Quelle conséquence ?

**- si on double le nombre de valeurs à sommer, on double le temps de**

**calcul**

\- C'est d'autant plus vrai que n est assez grand pour que le temps de ces

opérations (les additions) constitue la part significative du temps total de

l'exécution de sommer.

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

15





Du modèle pour l'algorithme

à la mesure d'un « vrai » programme

Et en vrai, sur l’ordinateur ?

\- Des différences importantes entre le modèle d'analyse de complexité de

l'algorithme et la chaîne actuelle de calcul : processeur, mémoires

hiérarchiques, options du compilateur, parallélisme, prédiction ...

\- La mesure des performances d'un code est un processus expérimental

assez difficile et qui « ment facilement »

\- Expérience dans le cours de programmation

L'analyse de complexité est cependant significative de la tendance des

mesures

En pratique : un problème donné de grande taille est résolu plus rapidement

par un algorithme en n, que par un algorithme en n2 , et encore plus que par

un algorithme en n3 ...

Exemple pour des algorithmes très calculatoires

on compte le nombre d'opérations arithmétiques

on mesure les temps d'exécution d'un programme (python sur mac-intel)

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

16





Des mesures réelles de sommer

Mesures sur ma machine de la somme codée en C :

sommer est bien **linéaire** en nombre d'additions

Quel sur-coût observe-t-on quand la taille du problème est multipliée par

10 ?

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

17





Recherche itérative

Le coût de cette recherche dépend aussi de la valeur cherchée val

\- meilleur cas vs. pire cas ?

\- on s’intéresse au coût dans le pire cas : majoration du coût de toute

exécution

\- mesure de complexité en temps : nombre de comparaisons

\- paramètre de complexité : le nombre de valeurs n

\- ce nombre de comparaisons est majoré par le nombre de valeurs n

\- Conclusion : complexité au pire linéaire en le nombre de valeurs

def rechercheIterative(val : float, t : List[float], dim\_t: int) -> int:

i = 0

while i < dim\_t:

if val == t[i]:

return i

i = i+1

return -1

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

18





Complexité en espace

Combien de place mémoire pour que l’ago résolve le pb de taille n ?

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

19





Complexité en espace-mémoire

Quelle quantité d'espace-mémoire est nécessaire pour que

l'algorithme trouve la solution du problème ?

Quel espace-mémoire mesurer ?

\- on ne compte pas la place des données d'entrée, ni des résultats :

incompressible quelque soit l'algorithme

\- on compte "juste" **la place mémoire supplémentaire**

Cas facile / moyen / un peu difficile :

\- facile = statique : toutes les variables utilisées sont connues "dans

l'algo"

on compte leurs places selon leurs types : scalaire, tableau 1D, 2D ...

\- moyen = dynamique

on utilise de l'allocation dynamique de mémoire (les `list` python)

\- un peu difficile = appels récursifs

l'algorithme est récursif ... à venir très bientôt !!

la complexité en espace-mémoire peut alors être très, voire trop importante

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

20





Complexité en espace-mémoire de

sommer

def sommer(t : List[int], n : int) -> int :

res = 0

for i in range(n):

res = res + t[i]

return res

Analyse

. on ne compte pas les n places-mémoire pour l'entrée : le tableau d'entiers

t

. on ne compte pas res qui est le résultat retourné

. il suffit de pouvoir stocker l'accumulation des t[i] : ici dans res

. remarque : c'est toujours la même ligne qui compte !

. un seul entier suffit et ce quelque soit la taille du problème !

Conclusion :

. la complexité en espace-mémoire de sommer est constante (et égale à 1).

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

21





Un autre exemple de

complexité polynomiale

Complexité quadratique du produit matrice x vecteur

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

22





Je calcule le produit matrice x vecteur

Définition et analyse de l’expression mathématique

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

23





Je calcule le produit matrice x vecteur

1 def Au(A : List[List[float]], nb\_lignes : int, nb\_cols : int, u : List[float], nb\_cols : int) ->

List[float]:

nb\_lignes \* nb\_cols

nb\_cols,

nb\_lignes

2 for i in range(nb\_lignes):

3

4

5

v[i] = 0

for j in range(nb\_cols):

v[i] = v[i] + A[i][j] \* u[j]

6 return v

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

24





Algo de calcul du produit matrice x

vecteur

1 def Au(A : List[List[float]], nb\_lignes : int, nb\_cols : int, u : List[float], nb\_cols : int) -> List[float]:

nb\_lignes \* nbcols

nb\_cols,

nb\_lignes

2

3

4

5

6

for i in range(nb\_lignes):

v[i] = 0

for j in range(nb\_cols):

v[i] = v[i] + A[i][j] \* u[j]

return v

Appel pour : A[n][n], u[n] -> v[n]: nb\_lignes = nb\_cols = **n**

Deux boucles for imbriquées de taille n chacune

\- boucle extérieure : **n itérations** de

\- ligne 3 : total = n affectations

\- ligne 4 : la boucle for intérieure

\- boucle intérieure : **n itérations** de

\- ligne 5 : 1 \*, 1 +, 1 =

\- total intérieur = 2n opérations, n affectations

Total extérieur-intérieur : **2n2 opérations**, n2 + n affectations

**Asymptotiquement** : C(Ax) ~ n2 : complexité **quadratique** en

temps

Algo 2. L1 math-info. UPVD. (PhL)

14/01/2022

25





Des mesures réelles de A u

Le produit matrice-vecteur A x est quadratique en nombre d'opérations

arithmétiques

Attention : échelle log10 sur les axes

des x et des y !

La pente vaut 2, ce qui représente :

101 sur x à 102 sur y

soit donc x à x2

Autre illustration :

le temps de calcul représenté en

échelle log-log est une droite

parallèle à celle de n2

Conseil : être à l'aise pour choisir le tracé le plus parlant !

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

26





Complexité en mémoire du produit matrice x

vecteur

1 def Au(A, nb\_lignes, nb\_cols, u, n\_nb\_cols):

nb\_lignes x nbcols

nb\_cols,

nb\_cols

2

3

4

5

6

for i in range(nb\_lignes):

v[i] = 0

for j in range(nb\_cols):

v[i] = v[i] + A[i, j] \* x[j]

return v

**Complexité en espace mémoire**

\1. données - résultats

\- entrée : A[n][n], u[n]

\- résultat : v[n]

à n2 + n

à n

\- l’espace mémoire de n2 + n est minimal (sauf matrice ou vecteur

particulier)

\2. algorithme

\- mise à jour de chaque composante : traitement **en place**

\- espace mémoire supplémentaire **constant quelque soit n : O(1)**

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

27





Le produit matrice x vecteur : synthèse

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

28





Des mesures réelles de A u

Le produit matrice-vecteur A u est **quadratique** en nombre d'opérations

arithmétiques

u

Mesures du temps

t(Au) de l'exécution du

produit matrice-vecteur

codé en python sur ma

machine

u

x 100

x 10

[n][n]

u

Attention : échelles logarithmiques sur les 2 axes !

\- se convaincre que la pente de t(Au) vaut 2, ce qui représente k .

n2

\- la droite t(Au )/ n2 est horizontale : ce ratio est constant

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

29





Complexité et log2

Complexité et log

Réduire la complexité

Multiplier 2 entiers, épisode 1

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

30





Pas que des puissances entières de la taille

du pb

Exemple : algorithmes de recherche

Le problème : rechercher si une valeur est présente au non dans un tableau de n valeurs

\- mesure de complexité : nombre de comparaisons

\- paramètre de cette complexité : **n** le nombre de valeurs dans le tabelau

Un algorithme de **complexité linéaire** : recherche itérative (ou séquentielle)

\- je parcours le tableau du début à la fin et je compare chaque valeur du tableau à la valeur

cherchée

\- je m’arrête quand j’ai trouvé ou à la fin du tabelau

\- j'effectue entre 1 et n comparaisons, au plus n, jamais plus que n

\- C

(n) = n ou k x n ou plus tard O(n)

recherche itérative

\- **Nombre** maximal **de comparaisons = nombre d’itérations** du pire cas

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

31





Pas que des puissances entières de la taille

du pb

Exemple : algorithmes de recherche

Le problème : rechercher si une valeur est présente au non dans un tableau de n valeurs

**triées**

La mesure de complexité : nombre de comparaisons

Un algorithme de **complexité logarithmique** : la **recherche dichotomique**

\- je partage le tableau en 2 et je compare la valeur du milieu,

\- selon le résultat de la comparaison je jette la moitié droite (ou gauche) du tableau,

\- je **recommence** sur ce tableau de taille moitié : partage en 2, comparaison milieu,

abandon d'une moitié

\- **et ainsi de suite** jusqu'à

avoir trouvé la valeur et là, je m'arrête

OU obtenir un (sous-)tableau réduit à 0 ou 1 élément et là, je m'arrête ... peut-être sans

l'avoir trouvé

**Nombre de comparaisons = nombre de découpages en 2**

Nombre **maximal** de comparaisons = nombre de découpages en 2 jusqu'à l'arrêt

"avec absence" (pire cas)

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

32





Combien de découpages par 2 de n valeurs

jusqu'à en obtenir 1 seule ?

La réponse : log2(n)

Le principe : partons de **n = 2p**

\- division 1

\- division 2

à

à

2p / 2 = 2p-1

2p-1 / 2 = 2p-2

\- ...

\- division k

à

à

2p-k+1 / 2 = 2p-k

(la propriété à prouver par récurrence)

\- ...

\- division p

2p-p+1 / 2 = 2p-p = 20 = 1

Il faut p divisions par 2 pour passer de 2p à 1

et **p** = log (2p) = **log (n)**

2

**2**

C

(n) = log (n) ou : k x log (n) = k' x log (n) = k" x ln(n), ou plus tard O(log(n))

rech. dichotomique

2

2

10

La recherche dichotomique : exemple de complexité logarithmique

Les algorithmes issus de stratégie "diviser pour régner" (divide and conquer)

introduisent des complexités en log : log(n) ou n.log(n) ou ...

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

33





Réduire la complexité ?

**Diviser pour régner** ou divide and conquer

\- principe général basé sur la **récursivité**

\- réduire le problème en un problème similaire ET de taille réduite ...

... recommencer cette réduction ....

... jusqu'à obtenir un problème suffisamment petit pour pouvoir trouver

solution "immédiatement",

sa

à partir de cette solution, construire la solution du problème plus grand ...

... et ainsi de suite jusqu'à obtenir la solution du problème de départ

\- principe présent dans la recherche dichotomique !

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

34





(\*) Compléments

Produit de deux entiers

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

35





Un petit zoom sur le produit de 2 entiers

Problème : multiplier 2 entiers de n chiffres (en base 10)

Mesure : nombre de multiplications "chiffre à chiffre"

Algorithme (dit) naïf de multiplication :

A la main ... pour sentir la réponse

chaque chiffre d'un opérande (y'en a n) est multiplié par chaque chiffre de

l'autre opérande (y'en a aussi n) donc au total : n x n = n2 multiplications

"chiffre à chiffre"

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

36





La multiplication naïve est quadratique

Décompte des opérations :

\- une multiplication 1 chiffre x 3 chiffres = 3 multiplications (+ 2 additions)

\- on en fait 3, soit 9 multiplications (+ 6 additions)

\- et on somme les 3, soit 9 multiplications (et 8 additions)

et ce pour la multiplication de 2 nombres à 3 chiffres :

**on a bien effectué 32 = 9 multiplications**

Remarque : on ne compte pas les multiplications par les puissances de la base : 1, 10,

100, ...

ni les additions des produits partiels

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

37





Complexité quadratique du produit de 2

entiers

Analyse : formalisons le produit a x b en base 10 ICI : **n+1** chiffres

Com

\- fo

\- a

de a1





Réduire la complexité ?

Problème : multiplier 2 entiers de n chiffres (en base 10)

Mesure : nombre de multiplications "chiffre à chiffre"

Algorithme naïf de multiplication : complexité quadratique

n2 multiplications "chiffre à chiffre"

Existe-t-il un algorithme d'une complexité inférieure à n2 qui calcule

le produit de 2 entiers ?

Algorithme de Karatsuba (1960) : complexité

si n = 1000 :

\- multiplication naïve = 1 000 000 produits

\- multiplication de Karatsuba = 50 000 produits, soit 20 fois plus rapide !!!

à Sera présenté en exercice sur la récursivité !

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

39





Un petit zoom sur le produit de 2 entiers

Remarques pour finir

\- Démarche similaire en base 2

\- Algorithme naïf de multiplicati

produit par la base = décalage d'un chiffre/bit vers la gauche

produit axb : suite d'additions (de prod. ch. à ch.) et de décalages

similaire au produit de polynômes

\- Algorithmes rapide (Karatsuba)

entier sur machine = 64 bits et produit effectué "en" matériel

intérêt de Karatsuba : multiplier des grands entiers : N = n0 + n1 + ...

GMP :

<https://gmplib.org/>

sage (python)

http://www.sagemath.org/fr/

14/01/2022

Algo 2. L1





Complexité asymptotique

Notations de Landau :

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

41





Complexité en temps

Ce qui importe : c'est l'ordre de grandeur du coût mesuré

comme une fonction de la taille du problème, quelque soit

l'instance du pb.

Ce qui parle : c'est le surcoût de temps pour résoudre un

problème deux fois plus gros, dix fois plus gros !

10 fois plus gros avec une complexité :

\- cubique = 1000 fois plus long

\- quadratique = 100 fois plus long

\- linéaire = 10 fois plus long ... à la rigueur

\- racine carrée = environ 3 fois plus long ... oui !

\- logarithmique = 2 fois plus long ... oui : je veux !

\- exponentiel = 1010 fois plus long ... aie aie aie : trop cher pour moi

!!!!

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

42





Complexité **asymptotique**

Formaliser pour pour dégager les tendances asymptotiques

\- au pire **aussi** rapide qu'un algorithme quadratique ?

\- au pire **au moins aussi** rapide qu'un algorithme quadratique ?

\- au pire **au plus aussi** rapide qu'un algorithme quadratique ?

Comparaison asymptotique de fonctions et notations de

Landau

\- équivalent asymptotique

\- minorant asymptotique :

\- **majorant asymptotique** :

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

43





Notations de Landau

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

44





Analyse asymptotique

Vocabulaire

• f = O(g) : f est dominée asymptotiquement par g

Propriétés

• transitivité : f = O(g) et g = O(h) alors f = O(h)

• invariance par multiplication : si f=O(g) alors k.f = O(g) pour k>0

• addition : f = O(g ) et f = O(g ) alors f + f = O(g +g )

1

1

2

2

1

2

1

2

• multiplication : f = O(g ) et f = O(g ) alors f x f = O(g xg )

1

1

2

2

1

2

1

2

Majoration asymptotique O( .) est la plus utile en pratique

• l’analyse de complexité (décompte) conduit généralement à des

majorations

• majoration pertinente pour le pire cas

Attention aux constantes cachées

• ces bornes asymptotiques cachent des constantes multiplicatives qui

peuvent « faire la différence » entre 2 algorithmes de même

complexité asymptotique

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

45





Complexités asymptotiques

**Notation**

**Dénomination**

**Temps**

**pour n = 106 et**

**1GHz**

**Commentaires**

O(1)

temps constant

logarithmique

1 ns

rare

O(log n)

10 ns

instantané ou presque.

il y a une constante cachée

et du log2 en pratique

O(n)

linéaire

1000 ns = 1 ms

sera supérieur à 1 min pour

des tailles de pb

comparables aux taille de

RAM actuelles. Donc pb

prédominant = gestion de la

mémoire

O(n2)

O(nk)

quadratique

polynomiale

¼ h

ne pas dépasser n = 106

k= 3 à 30 ans

et pourtant on en rencontre

souvent

O(2n)

exponentielle

plus de 10300 000

milliards d’années

algorithme inutilisable en

pratique sauf pour des tout

petits problèmes : n < 50

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

46





Graphiquement

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

47





Exprimer les complexités

asymptotiques des itérations

et récursions

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

48





Complexité d’algorithme itératif

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

49





Itérations classiques

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

50





Complexité d’algorithme récursif

Fonction de complexité = relation de récurrence

**Exemples**

• factorielle : C(n) = C(n-1) + 1

• l’appel récursif à fact(n-1) : C(n-1)

• 1 multiplication : 1

• (la comparaison : 1)

• et C(0) = 1

• exponentiation classique : C(n) = C(n-1) + 1 et C(0) = 1

Exprimer **C(n) sous forme non récursive** par éliminations successives :

C(n)

= C(n-1) + 1

C(n-1) = C(n-2) + 1

C(n-2) = …

….

C(2)

C(1)

C(0)

\-----------------------

C(n)

= C(1) + 1

= C(0) + 1

= 1

= 1 + 1 + … + 1 = n + 1

**Conclusion**

\- récurrence : C(n) = C(n-1) + 1 et C(0) = 1 *ó* C(n) = n+1

\- complexité asymptotique : complexité linéaire (déjà vue)

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

51





Complexité d’algorithme récursif

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

52





Complexité d’algorithme récursif

Récursions dichotomiques : **C(n) fonction de C(n/2)** et apparition de

log

2

C(n) = C(**n/2**) + b

• exemples : exponentiation rapide, élimination de la moitié des valeurs

en temps constant, recherche dichotomique

• cas logarithmique : C(n) = C(1) + b x log (n) = O(log(n))

2

C(n) = C(n/2) **+ n**

• exemples : traitement linéaire avant appel récursif dichotomique

• cas linéaire : C(n) = O(n)

C(n) = 2 C(n/2) **+ a x n** + b, a ≠ 1

• exemples : traitement linéaire avant 2 appels récursifs dichotomiques,

tri fusion

• cas semi-logarithmique : C(n) = O(n.log(n))

C(n) = **a x** C(n/2) + b, a ≠ 1

• exemples : répéter a fois l’appel récursif dichotomique

• cas polynomial : C(n) = O(nlog a)

2

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

53





Complexité d’algorithme récursif

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

54





Synthèse

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

55





Analyse de complexité : avoir les idées

claires

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

56





Analyse de complexité : compléments

Pourquoi vouloir réduire la complexité ?

\- pour résoudre des gros problèmes

\- mais aussi des problèmes pas nécessairement gros mais compliqués

**- Il existe de nombreux problèmes qu'on se sait pas résoudre**

**exactement en un temps réaliste, souvent des problèmes**

**d’optimisation : min, max, le plus court, ...**

• complexité exponentielle : 2n à problème du sac à dos (force brute)

• complexité factorielle : n! à problème du voyageur de commerce (naïf)

• en pratique (source wikipedia, temps de base = 10 nanosec)

• exponentielle : pour n = 50, temps T = 130 jours,

pour n= 250 = 1059 ans

• factorielle :

pour n = 50, temps T = 1048 ans

Pertinence pratique du modèle utilisé et de l’analyse menée ?

\- modèle simple vs. exécution machine complexe

\- lecture-écriture mémoire : tout sauf du temps constant, compliqué

\- opération arithmétique : addition vs. division, entier vs. flottant

\- exécution séquentielle des instructions : ça n'existe plus -- ou presque plus

les machines actuelles exécutent plusieurs instructions en parallèle, dans un ordre

différent du programme, elles spéculent sur le résultats de tests ou d'accès mémoire ...

\- **les estimations asymptotiques (grande taille du pb) masquent ces**

**effets**

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

57

\- demain : calcul quantique ?





Analyse de complexité

Une sensibilisation à une première notion d’informatique

théorique

\- nos « petits » objectifs :

\- mieux comprendre l’efficacité d’un algorithme

\- estimer les effets de la taille d'un problème sur le temps de résolution

\- théorie de la complexité : une branche de l'informatique

\- objectif : classer les problèmes selon leurs difficultés de résolution,

(cad. le coût de leur résolution quelque soit l'algorithme utilisé) et les

relations entre ces classes de problèmes

\- modèles d'exécution : RAM (ici, Random Access Memory),

machines de Turing ("dites" déterministes ou non déterministes),

automates, ...

Autres aspects théoriques à voir ce semestre :

\- terminaison, correction et preuves

14/01/2022

Algo 2. L1 math-info. UPVD. (PhL)

58

