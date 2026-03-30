(td:td3-corr)=
# Feuille 3 : complexité

- Le symbole $\blacksquare$ indique les exercices ou questions obligatoires. Commencez pas ceux-là.
- Les symboles $\star$ et $\star \star$ indiquent les exercices ou questions de difficulté relative plus importante.


**Focus**

-   complexité : analyses et approches expérimentales

**Compétences**

_Avoir les idées claires_

- Connaitre le principes de l'analyse de la complexité en temps : modèle de calcul, mesure et paramètre de la complexité, meilleur et pire cas
- Savoir exprimer et exploiter une complexité asymptotique : principales complexités, interprétation pratique de ces complexités
- ($\star$) Savoir établir la complexité d'algorithmes itératifs simples ou récursifs terminaux (algorithmes étudiés en cours)

_Savoir-faire_

- Connaitre des exemples significatifs d'algorithmes de complexité polynomiale et logarithmique (complexité, pires et meilleurs cas)  
- Savoir identifier (sans nécessairement le prouver) la complexité, les meilleur-pire cas d'un algorithme  

## Objectif 10

### $\blacksquare$ QCM (Extrait de CC)
  
  Dans les questions de cet exercice, le terme ''complexité''
  (seul) désigne la complexité en temps.     
Dans les questions de cet exercice, le terme "complexité" (seul) désigne
la complexité en temps. On précise "complexité en espace" si on
s'intéresse à cette notion.

1.  Une analyse de complexité en temps mesure le temps d'exécution d'un
    programme sur les ordinateurs des salles info. (Vrai/Faux)

    ::: sverbat
    Faux
    :::

2.  Dans une analyse de complexité en temps, le coût d'une
    multiplication de 2 entiers codés sur 32 bits est de 1 unité tandis
    que celui de la multiplication de 2 nombres flottants codés sur 64
    bits est de 2 unités. (Vrai/Faux)

    ::: sverbat
    Faux
    :::

3.  Lors d'une analyse de complexité en temps, le coût d'une répétition
    `while` est égal à trois fois celui du `for` à cause du compteur
    géré de manière explicite : incrémentation et comparaison.
    (Vrai/Faux)

    ::: sverbat
    Faux
    :::

4.  Citer un exemple d'algorithme avec une complexité constante dans le
    meilleur cas et linéaire dans le pire cas.

    ::: sverbat
    Recherche séquentielle
    :::

5.  Citer un exemple d'algorithme avec une complexité quadratique dans
    le pire cas.

    ::: sverbat
    Produit matrice-vecteur, tri naïf
    :::

6.  Quel est le meilleur cas dans une recherche dichotomique dans $n$
    valeurs triées ?

    ::: sverbat
    chercher t\[n//2\]
    :::

7.  Un algorithme a une complexité temporelle cubique en la taille de
    son entrée, que peut-on dire de son temps d'exécution si l'on double
    la taille de l'entrée ?

    ::: sverbat
    x8
    :::

8.  La fonction de complexité $C(n) = 4n^3 + 25n^2 + 10^2$ est
    asymptotiquement linéaire? quadratique ? ou cubique ? Pourquoi?

    ::: sverbat
    Cubique, équivalence d'un polynôme à son terme de plus haut degré
    :::

9.  Les complexités asymptotiques des programmes $P1$ et $P2$ sont
    égales à $\theta(n)$ donc leurs fonctions de complexité $C_1(n)$ et
    $C_2(n)$ sont égales. (Vrai/Faux)

    ::: sverbat
    faux ( égal à des constantes multiplicatives près)
    :::

10. Un algorithme a une complexité en espace quadratique en son
    paramètre $n$. Pour $n = 100$, il requiert 1Mo d'espace mémoire pour
    pouvoir s'exécuter. De quelle quantité de mémoire aura-t-il
    *approximativement* besoin pour s'exécuter avec $n = 1000$ ?

    ::: sverbat
    100 Mo (*approximativement* permet de s'affranchir de l'effet de
    l'augmentation de la taille de l'espace pour les données et le
    résultat qui est d'un facteur 10 par rapport au facteur 100 de
    l'algorithme)
    :::



(exo:doubleboucle-corr)=
### $\blacksquare$ Exercice

1.  Dérouler l'algorithme suivant en explicitant les valeurs de
    l'ensemble de ses variables.

    ```{code-block} python
    ---
    linenos: true
    ---
    for i in range (4): 
        for j in range(i,4): 
            k = i + j
    ```

    ::: sverbat

    i | j | \#add
    :--:|:--:|:--:|
    0 | [0..4[ | 4
    1 | [1..4[ | 3
    2 | [2..4[ | 2
    3 | [3..4[ | 1
    
    :::    
    
3.  Même question en remplaçant la ligne 2 par :

    ```{code-block} python
     for j in range(i+1,4):
    ```


    ::: sverbat

    i | j | \#add
    :--:|:--:|:--:|
    1 | [1..4[ | 3
    2 | [2..4[ | 2
    3 | [3..4[ | 1

    :::

5.  Compter le nombre d'additions dans chacun des deux cas.

::: sverbat
- 4 + 3 + 2 + 1 = 10 additions
- 3 + 2 + 1 = 6 additions
:::
 
5.  Coder une vérification de ces deux questions.

::: sverbat
On ajoute un compteur `c` dans la boucle la plus interne : 

    ```{code-block} python
    ---
    linenos: true
    ---
    c = 0
    for i in range (4): 
        for j in range(i,4): 
            k = i + j
            c = c + 1
    ```
:::

### $\blacksquare $ Exercice

On reprend l'exercice précédent en introduisant un nombre arbitraire  $n$ d'itérations de chaque boucle.

1.  Quelle est une mesure naturelle de la complexité de cet algorithme ?
    Quel est le paramètre de cette complexité ?

::: sverbat
- mesure de complexité : le nombre d'additions
- paramètre de complexité : n
:::

3.  Pour chacun des cas suivants : compter le nombre d'additions
    effectuées à chaque itération de la boucle intérieure. En déduire le
    nombre total d'additions. Quelle est la complexité asymptotique de
    cet algorithme ?

	a.  On modifie la ligne 1 :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(n): 
		for j in range(i,4):
	```

    ::: sverbat

    - C(n) = 10
    - complexité constante
    - Si n est multiplié par 10, le nbre d'additions n'est pas modifié

    :::

    b.  on modifie maintenant la ligne 2 :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(4): 
		for j in range(n):
	```
::: sverbat
- 4 répétitions (boucle en i) de n additions (boucle en j)
- C(n) = 4n
- complexité linéaire
- Si n est multiplié par 10, le nbre d'additions est multiplié par 10
:::

	c.  ou aussi :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(4): 
		for j in range(i,n):
	```

    ::: sverbat

  - répétitions (boucle en i) de n, puis n-1, puis n-2 puis n-3 additions (boucle en j)
  - C(n) = 4n -10
  - complexité linéaire
  - Si n est multiplié par 10, le nbre d'additions est (asymptotiquement) multiplié par 10
    :::

	d.  Avec les lignes 1 et 2 suivantes :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(n): 
		for j in range(n):
	```

    ::: sverbat

  - n répétitions (boucle en i) de n additions (boucle en j)
  - C(n) = n x n = n^2
  - complexité quadratique
  - Si n est multiplié par 10, le nbre d'additions est (asymptotiquement) multiplié par 100

    :::

	e.  ou aussi les lignes 1 et 2 suivantes :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(n): 
		for j in range(i,n):
    ```

    ::: sverbat

  - répétition en i :
      - i = 0 -> n additions (boucle en j)
      - i = 1 -> n-1 additions (boucle en j)
      - i = 1 -> n-2 additions (boucle en j)
      - ...
      - i = n-2 -> 2 additions
      - i = n-1 -> 1 addition
  - Donc C(n) = n + (n-1) + (n-1) + ... + 2 + 1 = n(n+1)/2
  - C(n) quadratique
  - Si n est multiplié par 10, le nbre d'additions est (asymptotiquement) multiplié par 100

    :::

### $\blacksquare $ Exercice 

On rappelle la spécification des fonctions `est_egal()`  et `nb_communs()` d'abord sur des tableaux de dimension 1 (vecteurs) (cf. feuille 2).

- La fonction `est_egal()`  compare  deux tableaux de dimension 1 et retourne le booléen correspondant. 
On convient que deux tableaux sont égaux si leurs tailles sont égales et si leurs valeurs sont égales deux à deux.
- La fonction `nb_communs()` retourne le nombre de valeurs communes entre deux tableaux de dimension 1. Ici aussi la comparaison s'effectue "deux à deux" (valeurs de même indice).

1. Effectuer l'analyse de la complexité de ces fonctions.

::: sverbat

- param de complexité : n la taille du tableau
- mesure de complexité : le nombre de comparaisons

- `est_egal` :

  - C(n) = n dans le pire cas (deux tableaux identiques ou qui diffèrent par leur dernière valeur),
  - complexité linéaire du pire cas
  - meilleur cas : une comparaison

- `nb_communs()`

  - C(n) = n, pire cas = meilleur cas : on doit comparer deux à deux les n valeurs de chaque tableau
  - complexité linéaire 

:::

1. Ces fonctions s'étendent à des tableaux 2D ou de façon plus générale à des tableaux multi-dimensionnels.
L’égalité entre tableaux multi-dimensionnels suppose l’égalité des dimensions, des tailles deux à deux dans chaque dimension, et des valeurs deux à deux pour toutes les valeurs du tableau.
Effectuer l'analyse de la complexité de ces fonctions pour des tableaux 2D.

::: sverbat

   - Pour des tableaux 2D, le paramètre de complexité reste `n` le nombre de lignes et le nombre de colonnes 
   - On mesure toujours le nombre de comparaisons
   - L'analyse est similaire à celle des tableau 1D en remplaçant `n` par `n x n`. 

:::

### Exercice (palindrome ... toujours) extrait d'examen

Cet exercice reprend l'exercice sur les palindromes des feuilles 1 et 2.

1. Effectuer l'analyse de complexité en temps de la version itérative de la vérification qu'un mot est ou non un palindrome (feuille 1).

Veillez bien à répondre aux points suivants : para-mètre et mesure de la complexité, meilleur cas et pire cas, expression de cette complexité, comportement asymptotique, effet sur temps de traitement si le paramètre de complexité est doublé.


::: sverbat

- mesure de la complexité : nbre de comparaisons
- param. de complexité : n = longueur du mot
- meilleur cas : dépend de l'algorithme, première comparaison : échec -> non palindrome C(n) = 1, constante
- pire cas : dépend de l'algorithme, on effectue n//2 comparaisons pour conclure que c'est un palindrome ou non (dernière comparaison) : C(n) = n//2, complexité linéaire
- si est n est doublé, on double le nbre de comparaisons dans le pire cas.

:::

2. Même question pour la version récursive vue dans la feuille 2.

::: sverbat

- mesure de la complexité : nbre de comparaisons
- param. de complexité : n = longueur du mot
- on effectue 1 comp par appel récursif
- chaque appel récursif réduit la longueur du mot de 2 caractères :  n, n-2, n-4 ..., 2 ou 1
    - Donc C(n) = 1 + C(n-2) 
- l'arrêt de la récursion est qd g >= d, cad un mot de longueur 0
    - Donc C(0) = 1
- Par simplification, on trouve : C(n) = 1 + 1 + ... + 1 = n/2 
- Complexité linéaire et identique (*) à celle de la version itérative

(*) Rmq. En toute rigueur, C(n) = n//2 + 1. Ce décompte dépend de la parité de n. Le "+1" vient de la condition d'arrêt (mot de longueur 0). On aurait pu terminer la récursion avec un appel de moins dès que le mot est de longueur 2 (comparaison de deux caractères) ou de longueur 1 (pas de comparaison nécessaire).

:::

### Exercice (extrait d'examen)

On s'intéresse à la complexité en temps de la fonction suivante.

        def mystere(n: int) -> int:
           m = 0
           for i in range(n):
              for j in range(i):
                 m = m + i + j
           return m 


1.  Quel est le paramètre de cette complexité ?

    ::: sverbat
    - n
    :::

2.  Quelles sont les instructions significatives de cette complexité ?

    ::: sverbat
    - l'affectation du corps de boucle (mieux) et les 2 add du membre de droite (moins bien)
    :::

3.  Quelle est une mesure de sa complexité ?

    ::: sverbat
    - le nombre d'affectations (mieux que le nbre d'op. arithm)
    :::

4.  Donner l'expression de cette complexité.

    ::: sverbat
    - c(n) = n(n-1)/2
    :::

5.  Combien y a-t-il d'opérations arithmétiques dans l'exécution de
    cette fonction pour un paramètre effectif $N$ donné. ?

    ::: sverbat
    - 2 fois plus que d'affectations : N(N-1)
    :::

6.  Expliciter sa complexité asymptotique avec les notations de Landau.

    ::: sverbat
    - quadratique, ie $\Theta(n\^2)$
    :::

