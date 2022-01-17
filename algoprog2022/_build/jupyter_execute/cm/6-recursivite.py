#!/usr/bin/env python
# coding: utf-8

# # Récursivité
# 
# version 2.021 (PhL)

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Récursivité" data-toc-modified-id="Récursivité-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Récursivité</a></span><ul class="toc-item"><li><span><a href="#Définitions-et-premiers-exemples" data-toc-modified-id="Définitions-et-premiers-exemples-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Définitions et premiers exemples</a></span><ul class="toc-item"><li><span><a href="#Définition" data-toc-modified-id="Définition-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Définition</a></span></li><li><span><a href="#Exemples-de-fonctions-récursives" data-toc-modified-id="Exemples-de-fonctions-récursives-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Exemples de fonctions récursives</a></span></li><li><span><a href="#Exemple-de-géométries-récursives" data-toc-modified-id="Exemple-de-géométries-récursives-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Exemple de géométries récursives</a></span><ul class="toc-item"><li><span><a href="#On-les-trace-avec-turtle-!" data-toc-modified-id="On-les-trace-avec-turtle-!-1.1.3.1"><span class="toc-item-num">1.1.3.1&nbsp;&nbsp;</span>On les trace avec turtle !</a></span></li></ul></li><li><span><a href="#Structures-de-données-récursives" data-toc-modified-id="Structures-de-données-récursives-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Structures de données récursives</a></span></li></ul></li><li><span><a href="#Intérêts-de-la-récursion" data-toc-modified-id="Intérêts-de-la-récursion-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Intérêts de la récursion</a></span><ul class="toc-item"><li><span><a href="#Avantage" data-toc-modified-id="Avantage-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Avantage</a></span></li><li><span><a href="#Inconvénient" data-toc-modified-id="Inconvénient-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Inconvénient</a></span></li><li><span><a href="#Paradigme-diviser-pour-régner" data-toc-modified-id="Paradigme-diviser-pour-régner-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Paradigme <strong>diviser pour régner</strong></a></span></li></ul></li><li><span><a href="#Fonctions-numériques-récursives" data-toc-modified-id="Fonctions-numériques-récursives-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Fonctions numériques récursives</a></span><ul class="toc-item"><li><span><a href="#Factorielle-:-forme-itérative" data-toc-modified-id="Factorielle-:-forme-itérative-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Factorielle : forme itérative</a></span><ul class="toc-item"><li><span><a href="#Exercice" data-toc-modified-id="Exercice-1.3.1.1"><span class="toc-item-num">1.3.1.1&nbsp;&nbsp;</span>Exercice</a></span></li></ul></li><li><span><a href="#Factorielle-:-forme-récursive" data-toc-modified-id="Factorielle-:-forme-récursive-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Factorielle : forme récursive</a></span><ul class="toc-item"><li><span><a href="#Premier-essai-(qui-plante-:)" data-toc-modified-id="Premier-essai-(qui-plante-:)-1.3.2.1"><span class="toc-item-num">1.3.2.1&nbsp;&nbsp;</span>Premier essai (qui plante :)</a></span></li><li><span><a href="#Terminaison-:-pour-arrêter-les-appels-récursifs-!!!!" data-toc-modified-id="Terminaison-:-pour-arrêter-les-appels-récursifs-!!!!-1.3.2.2"><span class="toc-item-num">1.3.2.2&nbsp;&nbsp;</span>Terminaison : pour arrêter les appels récursifs !!!!</a></span></li><li><span><a href="#Bien-comprendre-les-appels-récursifs-!" data-toc-modified-id="Bien-comprendre-les-appels-récursifs-!-1.3.2.3"><span class="toc-item-num">1.3.2.3&nbsp;&nbsp;</span>Bien comprendre les appels récursifs !</a></span></li></ul></li></ul></li><li><span><a href="#Exponentiation-entière-rapide" data-toc-modified-id="Exponentiation-entière-rapide-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Exponentiation entière rapide</a></span><ul class="toc-item"><li><span><a href="#Une-première-récursion" data-toc-modified-id="Une-première-récursion-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Une première récursion</a></span></li><li><span><a href="#Une-seconde-récursion-beaucoup-plus-...-rapide" data-toc-modified-id="Une-seconde-récursion-beaucoup-plus-...-rapide-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Une seconde récursion beaucoup plus ... rapide</a></span></li></ul></li><li><span><a href="#Fibonacci-ou-l'inefficacité-de-la-récursion" data-toc-modified-id="Fibonacci-ou-l'inefficacité-de-la-récursion-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Fibonacci ou l'inefficacité de la récursion</a></span><ul class="toc-item"><li><span><a href="#Solution-récursive" data-toc-modified-id="Solution-récursive-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Solution récursive</a></span></li></ul></li><li><span><a href="#Appels-récursifs-:-environnement,--pile-d'exécution,-pile-et-arbre-des-appels" data-toc-modified-id="Appels-récursifs-:-environnement,--pile-d'exécution,-pile-et-arbre-des-appels-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Appels récursifs : environnement,  pile d'exécution, pile et arbre des appels</a></span><ul class="toc-item"><li><span><a href="#Environnement" data-toc-modified-id="Environnement-1.6.1"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Environnement</a></span></li><li><span><a href="#Pile-d'exécution" data-toc-modified-id="Pile-d'exécution-1.6.2"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Pile d'exécution</a></span></li><li><span><a href="#Pile-des-appels" data-toc-modified-id="Pile-des-appels-1.6.3"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>Pile des appels</a></span></li><li><span><a href="#Arbre-des-appels-récursifs" data-toc-modified-id="Arbre-des-appels-récursifs-1.6.4"><span class="toc-item-num">1.6.4&nbsp;&nbsp;</span>Arbre des appels récursifs</a></span></li><li><span><a href="#Illustration-sur-la-factorielle-récursive" data-toc-modified-id="Illustration-sur-la-factorielle-récursive-1.6.5"><span class="toc-item-num">1.6.5&nbsp;&nbsp;</span>Illustration sur la factorielle récursive</a></span><ul class="toc-item"><li><span><a href="#arbre-des-appels" data-toc-modified-id="arbre-des-appels-1.6.5.1"><span class="toc-item-num">1.6.5.1&nbsp;&nbsp;</span>arbre des appels</a></span></li><li><span><a href="#pile-des-appels" data-toc-modified-id="pile-des-appels-1.6.5.2"><span class="toc-item-num">1.6.5.2&nbsp;&nbsp;</span>pile des appels</a></span></li><li><span><a href="#environnements-succcessifs-pour-factorielle(3)" data-toc-modified-id="environnements-succcessifs-pour-factorielle(3)-1.6.5.3"><span class="toc-item-num">1.6.5.3&nbsp;&nbsp;</span>environnements succcessifs pour factorielle(3)</a></span></li></ul></li><li><span><a href="#Illustration-sur-le-calcul-récursif-de-Fibonacci." data-toc-modified-id="Illustration-sur-le-calcul-récursif-de-Fibonacci.-1.6.6"><span class="toc-item-num">1.6.6&nbsp;&nbsp;</span>Illustration sur le calcul récursif de Fibonacci.</a></span><ul class="toc-item"><li><span><a href="#arbre-des-appels" data-toc-modified-id="arbre-des-appels-1.6.6.1"><span class="toc-item-num">1.6.6.1&nbsp;&nbsp;</span>arbre des appels</a></span></li><li><span><a href="#pile-des-appels-récursifs" data-toc-modified-id="pile-des-appels-récursifs-1.6.6.2"><span class="toc-item-num">1.6.6.2&nbsp;&nbsp;</span>pile des appels récursifs</a></span></li></ul></li><li><span><a href="#Retour-sur-l'inefficacité-du-calcul-récursif-de-Fibonacci" data-toc-modified-id="Retour-sur-l'inefficacité-du-calcul-récursif-de-Fibonacci-1.6.7"><span class="toc-item-num">1.6.7&nbsp;&nbsp;</span>Retour sur l'inefficacité du calcul récursif de Fibonacci</a></span><ul class="toc-item"><li><span><a href="#environnements-et-pile-d'exécution" data-toc-modified-id="environnements-et-pile-d'exécution-1.6.7.1"><span class="toc-item-num">1.6.7.1&nbsp;&nbsp;</span>environnements et pile d'exécution</a></span></li></ul></li><li><span><a href="#Solution-itérative" data-toc-modified-id="Solution-itérative-1.6.8"><span class="toc-item-num">1.6.8&nbsp;&nbsp;</span>Solution itérative</a></span></li><li><span><a href="#Exercice" data-toc-modified-id="Exercice-1.6.9"><span class="toc-item-num">1.6.9&nbsp;&nbsp;</span>Exercice</a></span></li></ul></li><li><span><a href="#Les-tours-de-Hanoi" data-toc-modified-id="Les-tours-de-Hanoi-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Les tours de Hanoi</a></span><ul class="toc-item"><li><span><a href="#Objectif" data-toc-modified-id="Objectif-1.7.1"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Objectif</a></span></li><li><span><a href="#Solution-récursive" data-toc-modified-id="Solution-récursive-1.7.2"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>Solution récursive</a></span><ul class="toc-item"><li><span><a href="#Analyse" data-toc-modified-id="Analyse-1.7.2.1"><span class="toc-item-num">1.7.2.1&nbsp;&nbsp;</span>Analyse</a></span></li><li><span><a href="#Codage" data-toc-modified-id="Codage-1.7.2.2"><span class="toc-item-num">1.7.2.2&nbsp;&nbsp;</span>Codage</a></span></li></ul></li><li><span><a href="#Observation-...-inquiétante" data-toc-modified-id="Observation-...-inquiétante-1.7.3"><span class="toc-item-num">1.7.3&nbsp;&nbsp;</span>Observation ... inquiétante</a></span></li></ul></li><li><span><a href="#Compléments" data-toc-modified-id="Compléments-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Compléments</a></span><ul class="toc-item"><li><span><a href="#Compléments" data-toc-modified-id="Compléments-1.8.1"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>Compléments</a></span></li><li><span><a href="#A-venir" data-toc-modified-id="A-venir-1.8.2"><span class="toc-item-num">1.8.2&nbsp;&nbsp;</span>A venir</a></span></li></ul></li></ul></li></ul></div>

# ## Définitions et premiers exemples
# 
# ### Définition 
# 
# > Une construction est _récursive_ si elle se définit à partir d'elle même

#   
# ### Exemples de fonctions récursives
# 
# * factorielle : $n ! = n \times (n-1)!$
# * somme des $n$ premiers entiers : $s(n) = n + s(n-1)$
# * Fibonaci : $f(n+1) = f(n) + f(n-1)$
# * suites récurrentes : $u_n = f(u_{n-1})$ ou $u_n = f(u_{n-1},u_{n-2},\dots)$

# ### Exemple de géométries récursives
# * segment et flocon de von Koch
# 
# 
# [segments]: fig/cinqsegmentsvk.jpg
# [flocons]: fig/cinqflocons.jpg
# 
# ![][segments]
# ![][flocons]
# 

# #### On les trace avec turtle !
# 
# Turtle utilise un affichage dans une fenêtre extérieure via tcl-tk.  
# Il est possible que cet affichage cohabite mal avec le notebook jupyter.  
# Il est préférable d'exécuter ces séquences de code python hors du notebook (idle, terminal, ...).  

# ```python
# import turtle as t
# """Turtle : mouvements elementaires"""
# 
# # init : taille ecran en pixels, clear ecran, reset des variablesm
# t.screensize(500,500)
# t.reset(
# t.hideturtle() # pour aller plus vite
# t.degrees() # angles en deg
# ```

# ```python
# '''Utilise le module turtle 
# Ouvre une fenêtre 
# et trace 3 segments de VK
# '''
# import turtle as t
# 
# def segment(d, n, color="black"):
#     """segment de von Koch
#     recursion sur n pour decouper le segment de longueur d et
#     tracer d (longueur du segment) pixels si n==0"""
#     t.pencolor(color)        
# 
#     if n==0:
#         t.forward(d)
#     else:
#         dsur3 = d//3
#         segment(dsur3, n-1)
#         t.left(60)
#         segment(dsur3, n-1)
#         t.right(120)
#         segment(dsur3, n-1)
#         t.left(60)
#         segment(dsur3, n-1)
# 
# # init        
# t.screensize(500,500)
# t.reset()
# t.hideturtle() # pour aller plus vite
# t.degrees() # angles en deg
# 
# # taille
# d = 300
# #nbiter = input("nombre d'iterations = ")
# nbiter = 1
# h = 150 # espace vertical entre 2 traces
# 
# # point de depart
# a = (-200, 400)
# 
# # trace et changement point de depart
# for i in range(nbiter):
#     # deplacement au point de depart
#     t.up()
#     t.goto(a)
#     t.down()
# 
#     # trace 
#     segment(d, i)
#     
#     # maj point de depart
#     a = (a[0], a[1] - h)
# 
# # pour attendre avant d'effacer la fenetre turtle
# v = input("OK ?")
# t.reset()
# 
# # pour que le trace reste a l ecran
# t. mainloop()
# ```

# ```python
# '''trace (nbiter) flocons de VK'''
# def flocon(d, n, color="black"):
#     ''' trace flocon de VK en utilisant segment'''
#     segment(d, n, color)
#     t.right(120)
#     segment(d, n, color)
#     t.right(120)
#     segment(d, n, color)
#     t.right(120)
# 
# #nbiter = input("nombre d'iterations = ")
# nbiter = 3
# h = 150 # espace vertical entre 2 traces
# a = (-200, 200) # point de depart
# d = 84  # taille
# 
# # trace et changement point de depart
# for i in range(nbiter):
#     # deplacement au point de depart
#     t.up()
#     t.goto(a)
#     t.down()
# 
#     # trace 
#     flocon(d, i)
#     
#     # maj point de depart
#     a = (a[0], a[1] - h)
# 
# # pour attendre avant d'effacer la fenetre turtle
# v = input("OK ?")
# t.reset()
#  ```  

# Autre figure géométrique récursive
# 
# * triangle de Sierpinsky
# 
# ![sierpinsky](fig/sierpinsky.png)

# ### Structures de données récursives
# 
# * liste chaînée
# ![liste](fig/listechainee.png)
# 
# * arbre, arbre binaire
# ![arbrebinaire](fig/arbrebinaire.jpg)

# * application : arbre du code Morse (point, tiret)
#   ![codemorse](fig/morse-tree.png)  

#   
# * application : représentation d'une expression
#   ![expression](fig/arbreexpression.jpg)   

# ## Intérêts de la récursion
# 
# ### Avantage
# 
# Une solution _algorithmique récursive_ est souvent plus simple, plus lisible, plus facile à prouver qu'une solution itérative
# 
#   * exemple caractéristique : les tours de Hanoï (voir exercice de td)
#     ![](fig/hanoi1.jpg)

#  Animation de résolution :
#  
#  [Tower of Hanoi 4 par André Karwath (wikimediacommons)](https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif)
#     

# ### Inconvénient
# 
# L'_exécution_ de la solution récursive est plus compliquée
#  * gestion d'une pile d'appels de fonctions : la pile d'exécution
# 
# 
# L'exécution de la solution récursive peut provoquer des débordements de la mémoire
#     

# ### Paradigme **diviser pour régner**
# >  * On divise le problème en des _problèmes similaires_ de taille moindre, 
# >  * et ce récursivement jusqu'à obtenir un problème suffisamment simple (ou petit) pour le résoudre
#   
# Approche qui conduit à une solution naturellement ... récursive !  
#     
#   * exemples caractéristiques car plus efficaces qu'une solution itérative
#     * recherche dichotomique dans un ensemble trié
#     * exponentiation rapide :
#       $$x^{2p} = (x^p)^2$$ et 
#       $$x^{2p+1} = x \cdot (x^p)^2$$

# ## Fonctions numériques récursives
# 
# Une définition, deux écritures équivalentes 
# 
# * **forme itérative**
# $$n ! = 1 \times 2 \times \dots \times (n-1) \times n$$
# 
# * **forme récursive**
# $$n ! = n \times (n-1) ! \text{ avec }  1! = 1$$
# 
# Remarque : ces définitions ont un sens pour $n>0$. La valeur de $0!$ doit être définie de façon supplémentaire. 

# ### Factorielle : forme itérative

# In[1]:


def f(n : int) -> int:
    """Calcul de factorielle n -- version itérative
    entrée : n 
    sortie n!
    """
    res = 1
    for i in range(2,n+1):
        res = res * i
    return res

print("3! =", f(3))
print("1! =", f(1))
 


# In[2]:


# bien que non défini a priori
print("0! =", f(0))
# et même n'importe quoi !
print("-3! =", f(-3))


# <div class="alert alert-danger">
# ATTENTION : il faudrait **vérifier la validité du paramètre effectif**
# </div>

# #### Exercice
# * pourquoi ?
# * comment ?

# ### Factorielle : forme récursive
# 
# On applique la définition récursive :
# $n ! = n \times (n-1) !$
# 
# Oui, oui ! On a oublié de définir $0 !$.
# 
# On l'écrit quand même ...

# #### Premier essai (qui plante :)

# In[3]:


def f(n : int) -> int:
    """Calcul de factorielle n -- version récursive
    entrée : n 
    sortie n!
    """
    return n * f(n-1) # récursion

print("1! =", f(1))


# <div class="alert alert-warning"> 
# INFO: python limite à 1000 le nombre  d'appels récursifs 
# </div>
# 
#  Heureusement ... ce qui nous sauve ici ! 

# #### Terminaison : pour arrêter les appels récursifs !!!!

# In[ ]:


def f(n : int) -> int:
    """Calcul de factorielle n -- version récursive
    entrée : n 
    sortie n!
    """
    if n == 1:          # terminaison
        return 1
    else:
        return n * f(n-1) # récursion

print("3! =", f(3))
print("1! =", f(1))
#print(f(0))


# <div class="alert alert-warning">
# ATTENTION : pourquoi ne pas demander de calculer `f(0)`?
# </div>

# 2 instructions `return` :
# * la première retourne une valeur terminale
# * la seconde provoque un appel récursif (à elle-même) avant d'effectuer un quelconque calcul !  
#   . en effet le second opérande de la multiplication n'est pas encore connu ...
# 
# Autre écriture avec 1 seul `return` :

# In[ ]:


def f(n : int) -> int:
    """Calcul de factorielle n -- version récursive avec un seul return
    entrée : n 
    sortie n!
    """
    if n == 1:          # terminaison
        res = 1
    else:
        res = n * f(n-1) # récursion
    return res

print("3! =", f(3))
print("10! =", f(10))  


# #### Bien comprendre les appels récursifs !
# 
# Deux solutions :
# 
# 1. Facile : utilisons http://pythontutor.com/live.html#mode=edit pour calculer $5 !$
# 
# 2. Plus lourd : on va, de **façon exceptionnelle**, mettre des affichages dans le corps de la fonctions récursive pour bien comprendre.
# Pour cela, on décortique bien la fonction.

# In[ ]:


def f(n: int) -> int:
    """Calcul de factorielle n -- version récursive
    entrée : n 
    sortie n!
    """
    # pour voir les imbrications des appels
    global nb
    # on met a jour indent avant chaque return
    
    nb = nb + 1 # on ajoute .... à chaque appel
    indent = nb * "...."
    print(indent, "entrée dans f(", n, ")")
    
    if n == 1:     
        print(indent, "terminaison : on renvoit 1 pour n = ", n)
        nb = nb - 1 # on enleve .. avant un return
        return 1
    
    else:
        print(indent, n,"* f(", n-1,") = ?")
    
        print(indent, "appel de f(", n-1,")")
        r = f(n-1)
        print(indent, "on a calculé f(", n-1, ")")

        p = n * r
        print(indent, "on a fait le produit ", n,"* f(", n-1,")")
        print(indent, "Retour de la valeur", p)

        nb = nb - 1 # on enleve .. avant un return
        return p # récursion

nb = 0
f(4)
print(nb)


# <div class="alert alert-warning">
# 
# CONSEIL : bien regarder le moment où on effectue la **première** multiplication
# 
# </div>

# Exercice :
# 
# * Combien de variables _locales_ `r` et `p` ont été utilisées ?
# 

# Réponse :
# 
# * Chaque appel à `f()` introduit une nouvelle paire `r` et `p`
# * Ces variables sont _locales_ à l'appel concerné :
#     - elles sont introduites et évaluées dans l'_environnement_ (le contexte) de l'appel concerné 
# 
# Ces notions seront approfondies plus loin.

# ## Exponentiation entière rapide
# 
# 
# Objectif : calculer $x^n$ où $x$ est un réel et $n$ un entier positif.
# 
# ### Une première récursion
# 
# Elle est basée sur la relation récursive : $x^n = x \times x^{n-1}$ et $x^0 = 1$, pour $n > 0$.

# In[ ]:


def expo(x: float, n: int) ->float:
    '''calcule x**n : version récursive naturelle 
    entrées : x (float), n (int)'''
    if n == 0:
        return 1
    else:
        return x * expo(x, n-1)
    
expo(2,1000)


# **Exercice :**
# 
# * Ecrire une autre  version avec 1 seul `return`
# * Ecrire une version itérative 

# ### Une seconde récursion beaucoup plus ... rapide
# 
# 
# Autre écriture de $x^n$ avec des airs de dichotomie :) 
# * $x^{2p} = (x^p)^2$ -- c'est simple et récursif, non ?
# * $x^{2p+1} = x \times (x^p)^2$ --  c'est simple et aussi récursif, non ?

# In[ ]:


def expo_rapide0(x: float, n: integer):
    '''calcule x**n : version récursive rapide 
    entrées : x (float), n (int)'''
    if n == 0:
        return 1
    else:
        r =  expo_rapide(x, n//2)
        if (n % 2 == 0): # n est pair
            res = r * r
        else:            # n est impair
            res = x * r * r
        return res
    
expo_rapide(2,1000)  


# In[ ]:


def expo_rapide(x: float,n: integer):
    '''calcule x**n : version récursive rapide 
    entrées : x (float), n (int)'''
    if n == 0:
        print("terminaison")
        return 1
    else:
        print("appel pour n =", n)
        r =  expo_rapide(x, n//2)
        print("retour de n//2 :", r )
        if (n % 2 == 0): # n est pair
            res = r * r
            print("cas pair et res =", res)
        else:            # n est impair
            res = x * r * r
            print("cas impair et res =", res)
        return res
    
expo_rapide(2,5)  


# **Exercice**
# 
# Exhibons que `expo_rapide()`est effectivement plus rapide que `expo`  
# 
# * python permet de mesurer facilement le temps d'exécution d'un script  
# * ipython le permet avec des "magic functions" : elles commencent avec un %

# In[ ]:


# %time mesure le temps d'exécution d'une script
get_ipython().run_line_magic('time', 'expo(2,200)')
get_ipython().run_line_magic('time', 'expo_rapide(2,200)')


# Mesurer _de façon fiable_ des temps d'exécution  est plus difficile qu'il parait : l'ordinateur est rusé ...
# 
# On utilise `timeit` 
# * on répéter dans une boucle la partie qu'on veut mesurer (si elle prend très peu de temps) --> option `-n`
# * on peut répéter les mesures et les analyser : garder la meilleure, regarder la moyenne ... --> option `r`
# 

# In[ ]:


# timeit plus fiable : répète plusieurs mesures
get_ipython().run_line_magic('timeit', 'expo(3,20)')
get_ipython().run_line_magic('timeit', 'expo_rapide(3,20)')
print()

get_ipython().run_line_magic('timeit', '-n 100 expo(3,20)')
get_ipython().run_line_magic('timeit', '-n 100 expo_rapide(3,20)')
print()


get_ipython().run_line_magic('timeit', '-r 5 expo(3,20)')
get_ipython().run_line_magic('timeit', '-r 5 expo_rapide(3,20)')


# ## Fibonacci ou l'inefficacité de la récursion
# 
# La suite de Fibonaci est définie par une récurrence _d'ordre 2_ :
# 
# $$F(n+1) = F(n) + F(n-1);$$
# 
# ce qui nécessite de connaître 2 valeurs de départ :
# $$F(0) = F(1) = 1.$$

# ### Solution récursive
# 
# L'expression est naturellement récursive donc ...

# In[ ]:


def fibo(n):
    '''Fibonacci : solution récursive classique '''
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
for i in range(10):
    print(i,":", fibo(i))


# <div class="alert alert-warning">
# La suite va nous permettre de mieux voir l'inefficacité de cette solution récursive !
# </div>

# ## Appels récursifs : environnement,  pile d'exécution, pile et arbre des appels
# 
# On présente maintenant des notions liées _à la mise en oeuvre_ des appels de fonction dans le cadre récursif.  
# On en restera surtout aux principes, aux _abstractions algorithmiques_.  
# Les aspects plus détaillés de la mise en oeuvre (implantation du mécanisme d'appel de fonction) sont étudiés en deuxième année.  

# ### Environnement
# 
# Chaque appel récursif nécessite de construire **dynamiquement** un nouvel **environnement** :
# * où retourner le résultat de l'appel : une adresse de retour (ou des adresses)
# * les paramètres effectifs de l'appel
# * les variables locales nécessaire au traitement demandé
# 
# En pratique, on ne connaît pas le nombre de fois où une/des fonctions sont appelées.  
# Toutes ces informations sont donc  stockées dans une  _pile d'exécution_ ou _pile des appels_.  
# Une pile est une structure de donnée adaptée au stockage et à une certain type de traitements : empiler et dépiler.

# ### Pile d'exécution
# 
# La **pile d'exécution** est la mémoire associée nécessaire au stockage des paramètres d'appel, des adresses de retour, des variables locales
# - gérée par le langage de programmation : une pile LIFO de taille préfixée
# - mais risque de débordement mémoire si appels imbriqués (sans libération de la place occupée) trop nombreux
# 
# En python : 1000 appels au maximum ou trop volumineux
# 
# * Imaginons un paramètre tableau de grande taille réduit récursivement de 1 élément par 1 élément ...  
# exemple : sommer récursivement les n valeurs d'un tableau  
# qui plus est si la récursion est multiple comme la suite de Fibonacci : $f(n+1) = f(n) + f(n-1)$

# <DIV class="alert alert-danger">
# 
# En pratique : `stack overflow !` est le message classique quand ... ça ne va pas : 
# 
# </DIV>

# ### Pile des appels
# 
# La **pile des appels** est une _abstraction algorithmique_ qui représente la logique de la pile d'exécution **en se limitant à l'identifiant de chaque appel**.  
# On ne détaille pas l'environnement de chaque appel.

# ### Arbre des appels récursifs
# 
# L'**arbre des appels récursifs** est une autre _abstraction algorithmique_ de l'ensemble des appels d'un traitement récursif.  
# Le parcours des noeuds d'un arbre se représente aussi avec une pile ... d'où la connexion entre ces deux abstractions du traitement de la récursion.  

# ### Illustration sur la factorielle récursive
# 
# Calcul de `fact(4)` 
# 
# ![factorielle(4)](./fig/fact4.jpg)

# **Rmq.** 
# On a régulièrement besoin de dessiner des graphes. Il existe de nombreux outils à cet effet.
# Nous montrons par exemple comment utiliser depuis des petits codes python, le langage `dot`et le module `graphviz` -- tous les deux très classiques en la matière.
# 
# Bien sûr, **ces aspects sont hors du programme de ce chapitre.**

# In[6]:


''' arbre des appels du calcul de fact(4) : construction simple'''
import graphviz as gvz
import functools
fact4 = gvz.Digraph(format='jpg')
fact4.node('f4', label='fact(4)')
fact4.node('f3', label='fact(3)')
fact4.node('f2', label='fact(2)')
fact4.node('f1', label='fact(1)', color='red')
fact4.edge('f4', 'f3')
fact4.edge('f3', 'f2')
fact4.edge('f2', 'f1')

file_out = fact4.render('fig/fact4_dot')


# In[9]:


'''Affichage arbre construit avec le code précédent'''
from IPython.display import display, Image
print(__doc__)
#display(Image('fig/fact4_dot.jpg'), width=30)
#display(Image('fig/fact4_dot.jpg'))


# #### arbre des appels
# 
# La représentation suivante exhibe l'_arbre des appels_ récursif de `f`
# 
# ![](./fig/fact4_dot.jpg)

# In[10]:


''' arbre des appels du calcul de fact(4) : construction plus complète'''
import graphviz as gvz
import functools

digraph = functools.partial(gvz.Digraph, format='jpg')

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

''' arbre complet de l'évaluation fact(4)'''
fact4_complet = add_edges(
    add_nodes(digraph(), [
        ('4'), ('3'), ('2'),
        ('f4', {'label': 'fact(4)'}),
        ('f3', {'label': 'fact(3)'}),
        ('f2', {'label': 'fact(2)'}),
        ('f1', {'label': 'fact(1)', 'color':'red'}),
    ]),
    [
        ('f4', '4'),
        ('f3', '3'),
        ('f2', '2'),
        ('f4', 'f3'),
        ('f3', 'f2'),
        ('f2', 'f1')
    ]
).render('fig/fact4_complet')


# In[11]:


'''Affichage arbre'''
from IPython.display import display, Image
print(__doc__)
#display(Image('fig/fact4_complet.jpg'))


# Ici, les calculs intermédiaires sont simples (1 multiplication) et on peut compléter cet arbre des appels en exhibant les opérandes de ces calculs. 
# 
# ![](./fig/fact4_complet.jpg)

# #### pile des appels
# 
# L'évolution de la pile des appels lors du calcule de $4!$ s'obtient en parcourant l'arbre des appels "en profondeur d'abord".  
# On note `fact( )` par `f( )`.  
# 
# On représente **l'évolution de la pile des appels sur un axe _horizontal_ qui décrit le temps** (de la gauche vers la droite).  
# La pile est représentée à chacun de ces changements d'_état_ :  
# - la pile est  vide avant l'appel récursif principal  
# - chaque appel récursif _empile_ son contexte : on le note par l'appel lui-même 
#     - exemple : `f(4)` est l'appel principal du calcul de $4!$ et dénote aussi l'environnement de cet appel  
# - chaque retour de valeur à l'appelant a pour effet de _dépiler_ l'environnement de l'appelé  
# Ainsi la pile redevient vide après le traitement complet de l'appel principal.
# 
# Dans les affichages successifs, chaque colonne (verticale) représente l'état de la pile à un instant donné de l'exécution récursive -- comme une suite de photographies de cette pile.  La bas de la pile est le bas de la colonne.  

# **Construction de la pile des appels du calcul de $4!$ :**
# 
# - avant l'appel principal :  la pile est vide  
#         . 
#   

# - l'appel principal : on empile f(4)  
#         . f(4)  

# - dans f(4), l'appel de f(3) : on empile f(3)  
#                f(3) 
#         . f(4) f(4)   

# - dans f(3), l'appel de f(2) : on empile f(2)  
#                   f(2) 
#              f(3) f(3) 
#       . f(4) f(4) f(4)   

# - dans f(2), l'appel de f(1) : on empile f(1) 
#                        f(1)
#                   f(2) f(2) 
#              f(3) f(3) f(3) 
#       . f(4) f(4) f(4) f(4)   

# - f(1) est terminal (cet appel renvoie une valeur (1)) : on dépile f(1)
#                        f(1)
#                   f(2) f(2) f(2)
#              f(3) f(3) f(3) f(3)
#       . f(4) f(4) f(4) f(4) f(4)  
#   

# - f(2) est calculé et cet appel renvoie la valeur 1x2 : on dépile f(2)
#                        f(1)
#                   f(2) f(2) f(2)
#              f(3) f(3) f(3) f(3) f(3)
#       . f(4) f(4) f(4) f(4) f(4) f(4)  
#   

# - f(3) est calculé et cet appel renvoit la valeur 1x2x3 : on dépile f(3)
#                        f(1)
#                   f(2) f(2) f(2)
#              f(3) f(3) f(3) f(3) f(3)
#       . f(4) f(4) f(4) f(4) f(4) f(4) f(4)  
#   

# - f(4) est calculé et cet appel renvoie la valeur 1x2x3x4 : on dépile f(4)
#                        f(1)
#                   f(2) f(2) f(2)
#              f(3) f(3) f(3) f(3) f(3)
#       . f(4) f(4) f(4) f(4) f(4) f(4) f(4)  
#    

# - la pile est vide et on a bien obtenu le résultat attendu (24)
#                        f(1)
#                   f(2) f(2) f(2)
#              f(3) f(3) f(3) f(3) f(3)
#       . f(4) f(4) f(4) f(4) f(4) f(4) f(4) .   

# ####  environnements successifs pour factorielle(3) 
# 
# On peut le détailler un peu plus dans ce cas simple.
# 
# appel = f(3)
# 
# ```python
# def f(n):
#     """Calcul de factorielle n -- version récursive
#     entrée : n 
#     sortie n!
#     """
#     if n == 1:     
#         return 1   
#     else:
#         r = f(n-1)
#         p = n * r
#         return p # récursion
# 
# ```

# L'environnement de chaque appel est décrit par une colonne du tableau suivant.
# 
#    . |   0   |  1    |  2    |   3        
# -----|-------|-------|-------|--------  
# 1    | r=f(3)| n=3   |       |          
# 2    |       | r=f(2)| n=2   |          
# 3    |       |       | r=f(1)| n=1      
# 4    |       |       |       | return 1  
# 5    |       |       | p=2\*1 |  
# 6    |       |       | return 2|   
# 7    |       | p=3\*2|       |  
# 8    |       | return 6|     |  
# 9    | r = 6 |       |       | 
#   
#     

# ### Illustration sur le calcul récursif de Fibonacci.
# 
# #### arbre des appels
# 
# * Le calcul de `fibo(4)` correspond à un parcours "en profondeur d'abord" de l'**arbre des appels** suivant.
# 
# ![arbre appels fibo(4)](./fig/arbre-fibo4.jpg)

# #### pile des appels récursifs
# 
# On note `fibo()` par `f()`  
# Les appels récursifs sont empilés (avec leur environnement) dans une _pile d'appels_  
# Les appels avec terminaison permettent de dépiler l'appelant  
# L'appel principal est exécuté une fois la pile vidée
# 
# 
#                    f(1) f(0)
#               f(2) f(2) f(2) f(2)      f(1)                f(1) f(0)
#          f(3) f(3) f(3) f(3) f(3) f(3) f(3) f(3)      f(2) f(2) f(2) f(2)
#     f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4) f(4)
# 

# ### Retour sur l'inefficacité du calcul récursif de Fibonacci
# 
# Exercice : comptons le nombre d'appels à `fibo()` dans l'évaluation de `fibo(4)`.
# 
#  fibo(4) | #appels 
# ---------|:-------:
#  fibo(0) |  2
#  fibo(1) |  3
#  fibo(2) |  2
#  fibo(3) |  1 
#  _total_ |  _8_
#  
#  Ces évaluations intermédiaires répétées engendrent des _sur-coûts_ en mémoire et en calcul qui dégradent l'efficacité de l'évaluation récursive de `fibo( )`.  

# 
# #### environnements et pile d'exécution 
# 
# Profitons du python tutor pour visualiser l'enchaînement des appels et l'évolution de l'environnement :
# 
# https://goo.gl/mHi50H

# ### Solution itérative
# 
# Analyse : 
# 
# * pour calculer $F(n)$, il faut avoir calculé les 2 précédents : $F(n-1)$ et $F(n-2)$
# * et ainsi de suite ... 
# * donc on part de $F(0)$ et $F(1)$ 
# * et on avance dans l'itération en stockant
#     * les 2 dernières valeurs calculées
#     * toutes les valeurs déjà calculées
# 
# La solution itérative est plus efficace car elle évite de re-calculer les termes déjà calculés.  
# 

# ### Exercice
# 
# Reprendre ça sous http://pythontutor.com/live.html#mode=edit

# ## Les tours de Hanoï
# 
# ### Objectif
# 
# Déplacer l'empilement de disques du piquet gauche au piquet droit en respectant les règles suivantes :  
# * déplacer un seul disque à la fois
# * un disque ne peut être posé que sur un disque de diamètre supérieur
# On doit utiliser le piquet du milieu.
# 
# début -> fin 
# ![hanoi_debut](fig/hanoi1.jpg) ![hanoi_fin](fig/hanoi2.jpg)
# 

# ### Solution récursive
# 
# #### Analyse
# * On  note les piquets A, B, C de la gauche vers la droite.  Départ = A, objectif = C
# * On note $n$ le nombre de disques à déplacer ; ici $n=4$
# * On veut donc **résoudre le problème des tours de Hoanoi de taille 4 en allant de A vers C grâce à l'utilisation de B**
#     - notons la résolution de ce problème `Hanoi(4, A, C, B)` 
#     - plus généralement : **Hanoi(n, départ, arrivée, intermédiaire)**
#     

# **Récursion**  
# Si on déplace _l'empilement complet avec les 3 disques supérieurs_ de A vers B en utilisant C (dur), ensuite on déplace le dernier (plus grand) disque de A vers C (facile), il ne reste qu'à déplacer l'empilement complet de 3 disques de B vers C en utilisant A (moins dur vu qu'on pu le faire à l'étape 1)
# * déplacer un empilement complet de 3 disques de A vers B (en utilisant C) = `Hanoi(3, A, B, C)`
# * déplacer le disque qui reste sur A vers C = `Hanoi(1, A, C, B)` ... oui: B ne sert à rien
# * déplacer un empilement complet de 3 disques de B vers C (en utilisant A) = `Hanoi(3, B, C, A)`
# 
# 
# <div class="alert alert-success">
#     
# On tient la récursion ! 3 appels à `Hanoi` pour calculer `Hanoi` !!
# 
# </div>

# **Avec un graphique**
# 
# * On part de là : avec un empilement de 4 disques sur A à déplacer vers C
# ![hanoi_rec0](fig/resized/hanoi_rec0.png)

# * On identifie un empilement de taille inférieure : 3 disques regroupés en rose
# ![hanoi_rec1](fig/resized/hanoi_rec1.png)

# * On suppose qu'on est capable de déplacer _correctement_ l'empilement rose de A vers B (en utilisant C)
# ![hanoi_rec2](fig/resized/hanoi_rec2.png)

# * On déplace le dernier disque restant sur A vers C : il est à sa bonne place
# ![hanoi_rec3](fig/resized/hanoi_rec3.png)

# * Comme deux étapes avant, on suppose qu'on est capable de déplacer _correctement_ l'empilement rose de B vers C (en utilisant A). L'empilement rose est bien placé maintenant
# ![hanoi_rec4](fig/resized/hanoi_rec4.png)

# * et le problème initial est bien résolu !
# ![hanoi_rec5](fig/resized/hanoi_rec5.png)

# **Terminaison pour la récursion**
# * on termine quand on sait résoudre le problème car il est suffisamment simple :
#     - on déplace **un disque** 
#     - c'est `Hanoi(1, ...)`
# 
#     
# _Remarque :_ pour une solution itérative, une terminaison naturelle serait "quand tous les disques ont été déplacés", i.e. quand le piquet de départ est vide
# 
# **Déplacer $(n-1)$ disques : étape dure ?**  
# * NON : on "retombe" sur la résolution de Hanoi pour un nombre de disque diminué de 1 ...  
# * ce qui devrait à un moment ne plus laisser aucun disque à déplacer :)
# On formalisera plus tard cette analyse de la _terminaison_ de la solution récursive. 

# #### Codage 
# 
# Yapluka !
# 
# On commence avec `hanoi0` pour exhiber un détail technique

# In[ ]:


def hanoi0(n, depart, arrivee, interm):
    '''tours de hanoi :  déplacer n disques de 
    depart vers arrivee en utilisant interm 
    (et en respectant les règles de déplacement du pb des tours de Hanoi)
    '''
    if n > 0:
        hanoi0(n-1, depart, interm, arrivee)
        hanoi0(1, depart, arrivee, interm)
        hanoi0(n-1, interm, arrivee, depart)        
        


# In[ ]:


''' resolution : appel '''
hanoi0(4, A, C, B)


# Les piquets `A, B, C' n'existent pas en tant qu'objet (variable) python.
# 
# Pour rendre effectif un traitement, 
# * les piquets sont les _caractères_ : `'A'`, `'B'`, `'C'`  
# * il suffit alors d'indiquer le déplacement `(Hanoi(1, ...)` par un `print`:
#     -  `hanoi(1, depart, arrivee, interm)` devient  `print(depart -> arrivee)`
#     - ce qui montre bien qu'interm est inutile quand le nb de disques égal 1
#     
# L'exécution de l'algo va donner tous les déplacements _d'1 disque_ à appliquer au pb pour le résoudre  

# In[ ]:


def hanoi(n, depart, arrivee, interm):
    '''affiche les déplacements pour déplacer n disques de 
    depart vers arrivee en utilisant interm 
    (et en respectant les règles de déplacement du pb des tours de Hanoi)
    '''
    if n > 0:
        hanoi(n-1, depart, interm, arrivee)
        print(depart, '-->', arrivee)
        hanoi(n-1, interm, arrivee, depart)        
        
'''appel'''
hanoi(4, 'A', 'C', 'B')


# <div class="alert alert-danger">
# 
# ATTENTION : il y a 0 `return` et 1 `print` ... et pourtant l'algorithme termine et (semble) donner les déplacements qui résolvent le pb ... C'est un biais pédagogique introduit par la _modélisation_ des piquets par des caractères (difficile de faire autre chose que des `print` sur des caractères). Vous reprendrez cette résolution lorsque vous saurez représenter les empilements de disques par ... des piles.
# 
# </div>

# In[ ]:


''' appels simples pour se convaincre que ça marche et ...'''
#hanoi(1, 'A', 'C', 'B')
print("---------")
hanoi(2, 'A', 'C', 'B')
print("---------")
hanoi(3, 'A', 'C', 'B')


# **Exercice**  
# Exécuter "à la main" les déplacements de `hanoi(3)`et `hanoi(4)` en numérotant les disques (1,2,3,...) et les piquets (A,B,C)  
# et vérifier que les problèmes sont effectivement résolus !

# ### Observation ... inquiétante
# 
# \# disques | \# déplacements
# :----------:|:--------------:
# 2 | 3
# 3 | 7
# 4 | 15
# 
# Normal ?
# * $n=1$ : OK pour hanoi(1) = 1 seul déplacement
# * $n=2$ : 3 appels à hanoi(1) donc $3\times1 = 3$ 
# * $n=3$ : 2 hanoi(2) + 1 hanoi(1) = $2\times 3 + 1 \times 1 = 7$
# * $n=4$ : 2 hanoi(3) + 1 hanoi(1) = $2\times 7 + 1 \times 1 = 15$
# 
# et ainsi de suite ... 
# * ca augmente assez vite 
# * on formalisera cette analyse de _complexité_ dans un prochain chapitre.
# 
# **Exercices**
# * Coder un algo qui calcule le nombre de déplacements pour $n = 2, 3, \dots, 12$ et pour plus ensuite 
# * Modifier `hanoi()` pour compter le nombre de déplacements total 
# 
# 
# 

# In[ ]:


a = 1
for i in range(1, 13):
    c = 2*a + 1
    print(i+1, 'disques  -> ', c, 'déplacements')
    a = c
print("Ca vous fait penser à quelque chose :) ?")


# ## Compléments
# 
# ### Compléments 
# 
# Des ressources utiles :
# 
# *  sur interstices.info : [hanoi_interstices](https://interstices.info/jcms/p_82121/les-tours-de-hanoi-un-probleme-classique-de-recursion)
# * un mooc sur la récursivité (UPMC)
# * ...

# ### A venir
# 
# 1. Autres algorithmes récursifs importants
#     - recherche séquentielle et dichotomique : voir chapitre "Rechercher"    
#     - trier : tri fusion, tri rapide : voir chapitre "Trier"  
# 2. Etablir la complexité d'algos récursifs
#     - La fonction de complexité est une suite récursive : la complexité de la résolution récursive d'un problème de taille n est fonction de la complexité de la résolution (récursive) du problème de taille réduite.
#     - exemple : $C(n) = 2 \times C(n/2) + 1$ et $C(1) = 1$
#     - autre exemple : $C(n) = p \times C(n/p) + f(p)$ et $C(1) = 1$
#     - ...
#     - est traité en dernière partie du chapitre "Complexités"  
# 3. Prouver la terminaison et la correction de ces algos récursifs
#     - est traité dans le chapitre "Prouver"  
# 4. Dé-récursifier : récursif -> itératif (quand on peut)
#     - voir les slides du cours de 2016 : http://perso.univ-perp.fr/langlois/images/pdf/ens/L1/s7-sl4.pdf 
jupyter nbconvert --to html_embed --template toc2 6-recursivite.ipynbjupyter nbconvert 6-recursivite.ipynb --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --SlidesExporter.reveal_theme=solarized
# In[ ]:




