#!/usr/bin/env python
# coding: utf-8

# version 2021, PhL.

# In[1]:


# -*- coding : utf8 -*-
from typing import List


# <h1>Table des matières<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Des-QCM-et-autres-sites-à-exploiter" data-toc-modified-id="Des-QCM-et-autres-sites-à-exploiter-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Des QCM et autres sites à exploiter</a></span></li><li><span><a href="#Examen-CT2-2020" data-toc-modified-id="Examen-CT2-2020-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Examen CT2 2020</a></span><ul class="toc-item"><li><span><a href="#Exercice-7" data-toc-modified-id="Exercice-7-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 7</a></span><ul class="toc-item"><li><span><a href="#Écrire-une-programme-qui" data-toc-modified-id="Écrire-une-programme-qui-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Écrire une programme qui</a></span></li></ul></li></ul></li><li><span><a href="#Fonctions" data-toc-modified-id="Fonctions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Fonctions</a></span><ul class="toc-item"><li><span><a href="#Ce-qu'il-faut-savoir" data-toc-modified-id="Ce-qu'il-faut-savoir-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Ce qu'il faut savoir</a></span></li><li><span><a href="#Ce-qu'il-faut-savoir-faire" data-toc-modified-id="Ce-qu'il-faut-savoir-faire-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Ce qu'il faut savoir faire</a></span></li><li><span><a href="#Pré-requis-technique" data-toc-modified-id="Pré-requis-technique-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Pré-requis technique</a></span></li><li><span><a href="#QCM-fonctions" data-toc-modified-id="QCM-fonctions-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>QCM fonctions</a></span></li><li><span><a href="#Compléments-de-séance" data-toc-modified-id="Compléments-de-séance-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Compléments de séance</a></span></li></ul></li><li><span><a href="#Boucles-avancées" data-toc-modified-id="Boucles-avancées-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Boucles avancées</a></span><ul class="toc-item"><li><span><a href="#Ce-qu'il-faut-savoir" data-toc-modified-id="Ce-qu'il-faut-savoir-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Ce qu'il faut savoir</a></span></li><li><span><a href="#Ce-qu'il-faut-savoir-faire" data-toc-modified-id="Ce-qu'il-faut-savoir-faire-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Ce qu'il faut savoir faire</a></span></li><li><span><a href="#Compléments-en-séance" data-toc-modified-id="Compléments-en-séance-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Compléments en séance</a></span></li></ul></li><li><span><a href="#Complexité" data-toc-modified-id="Complexité-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Complexité</a></span><ul class="toc-item"><li><span><a href="#Avoir-les-idées-claires" data-toc-modified-id="Avoir-les-idées-claires-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Avoir les idées claires</a></span></li><li><span><a href="#Savoir-faire" data-toc-modified-id="Savoir-faire-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Savoir-faire</a></span></li></ul></li><li><span><a href="#(P)-Entrées-Sorties-:-fichiers" data-toc-modified-id="(P)-Entrées-Sorties-:-fichiers-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>(P) Entrées-Sorties : fichiers</a></span><ul class="toc-item"><li><span><a href="#Compléments" data-toc-modified-id="Compléments-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Compléments</a></span><ul class="toc-item"><li><span><a href="#Fonction-avec-paramètre-fichier" data-toc-modified-id="Fonction-avec-paramètre-fichier-6.1.1"><span class="toc-item-num">6.1.1&nbsp;&nbsp;</span>Fonction avec paramètre fichier</a></span><ul class="toc-item"><li><span><a href="#Cas-du-fichier-physique" data-toc-modified-id="Cas-du-fichier-physique-6.1.1.1"><span class="toc-item-num">6.1.1.1&nbsp;&nbsp;</span>Cas du fichier physique</a></span></li><li><span><a href="#Cas-du-fichier-logique" data-toc-modified-id="Cas-du-fichier-logique-6.1.1.2"><span class="toc-item-num">6.1.1.2&nbsp;&nbsp;</span>Cas du fichier logique</a></span></li></ul></li></ul></li><li><span><a href="#Avoir-les-idées-claires" data-toc-modified-id="Avoir-les-idées-claires-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Avoir les idées claires</a></span></li><li><span><a href="#Savoir-faire" data-toc-modified-id="Savoir-faire-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Savoir-faire</a></span></li></ul></li><li><span><a href="#Types-composés-(P),-structures-de-données" data-toc-modified-id="Types-composés-(P),-structures-de-données-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Types composés (P), structures de données</a></span><ul class="toc-item"><li><span><a href="#Tableau" data-toc-modified-id="Tableau-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Tableau</a></span></li><li><span><a href="#Liste" data-toc-modified-id="Liste-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Liste</a></span></li><li><span><a href="#Dictionnaire" data-toc-modified-id="Dictionnaire-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Dictionnaire</a></span></li><li><span><a href="#Spécification-de-fonctions-et-types-composés" data-toc-modified-id="Spécification-de-fonctions-et-types-composés-7.4"><span class="toc-item-num">7.4&nbsp;&nbsp;</span>Spécification de fonctions et types composés</a></span></li><li><span><a href="#Avoir-les-idées-claires" data-toc-modified-id="Avoir-les-idées-claires-7.5"><span class="toc-item-num">7.5&nbsp;&nbsp;</span>Avoir les idées claires</a></span></li><li><span><a href="#Savoir-faire" data-toc-modified-id="Savoir-faire-7.6"><span class="toc-item-num">7.6&nbsp;&nbsp;</span>Savoir-faire</a></span></li></ul></li><li><span><a href="#(P)-Entrées-Sorties-:-aspects-avancés" data-toc-modified-id="(P)-Entrées-Sorties-:-aspects-avancés-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>(P) Entrées-Sorties : aspects avancés</a></span><ul class="toc-item"><li><span><a href="#Avoir-les-idées-claires" data-toc-modified-id="Avoir-les-idées-claires-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Avoir les idées claires</a></span></li><li><span><a href="#Savoir-faire" data-toc-modified-id="Savoir-faire-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Savoir-faire</a></span></li></ul></li></ul></div>

# # Des QCM et autres sites à exploiter
# 
# Le net est riche de ressources à exploiter. 
# En voici quelques-unes sélectionnées et à exploiter en plus de ceux proposés à chaque fin de chapitre.
# 
# - [Site](https://www.bernon.fr/index.php?page=exercice-banque-e3c-thème-a) de M. Bernon : QCMs interactifs issus de la banque de données des E3C  
# 
# - [Site](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python_function) de Fabrice Sincere (lien sur le qcm sur les fonctions) 
# 
# - Objectif 20 : [France IOI]
# (http://www.france-ioi.org/algo/chapter.php?idChapter=509)

# # Examen CT2 2020
# 
# ## Exercice 7
# 
# Soit T un tableau de n valeurs réelles. On souhaite normaliser les valeurs de T , c’est-à-dire, remplacer T [i] par (T [i] − min)/(max − min), où min et max sont la plus petite et plus grande valeur de T , respectivement.
# 􏰀
# 
# ### Écrire une programme qui
# — lit la taille n et la valeur des éléments de T ,  
# — affiche le contenu de T,  
# — normalise les valeurs de T,  
# — et affiche à nouveau le contenu de T .

# In[2]:


# entrées
n = int(input("n:"))
T = [0 for i in range(n)]
for i in range(n):
    T[i] = float(input("T()"))
    
#afficher T
print(T)

# normaliser T
min = T[0]
max = T[0]
for i in range(1, len(T)):
    if T[i] < min:
        min = T[i]      
    if T[i] > max:
        max = T[i]

for i in range(len(T)):      
    T[i] = (T[i] - min) / (max - min)    
        
        
print(min)
print(max) 


#afficher T
print(T)


# # Fonctions

# ## Ce qu'il faut savoir
# 
# - définition et paramètres formels vs. appel et paramètres effectifs
# - spécification, en-tête, signature : spécifier pour utiliser, pour vérifier  vs. corps : implémentation du traitement  
# - appel = changement de contexte : trace de l'exécution vs. séquentialité des instructions écrites 
#     - dynamique vs. statique  
# - appelant vs. appelé : le rôle de l'appel, le rôle du return
# - portée des variables : variables locales vs. variables plus globales  
# - l'effet de bord est indésirable  
# 
# 
# ## Ce qu'il faut savoir faire 
# 
# **Cadre** : en/pour python 
# 
# - définir et écrire la spécification d'une fonction qui réalise un traitement décrit en français, ou qui résoud un problème (simple) décrit en français  
# - définir et écrire des appels simples (tests unitaires) 
# - définir et écrire l'implémentation d'une fonction associée à une spécification 
# 
# ## Pré-requis technique
# 
# Dans/avec un notebook jupyter :
# - savoir mettre en oeuvre de la programmation simple en python (niveau semestre 1) dans un notebook jupyter 
# - savoir documenter cette programmation (énoncés, descriptions, ...) avec markdown
# 
# 
# ## QCM fonctions
# 
# - [Site](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python_function) de Fabrice Sincere 
# 
# - Objectif 20 : [France IOI](http://www.france-ioi.org/algo/chapter.php?idChapter=509)

# ## Compléments de séance 

# In[ ]:


def puissance(x : float, n : int) -> float:
    '''calcule x**n pour :
    x, n : int (entrées) 
    retourne res : int
    - traite les cas particulier : x==0, n==0, n<0 '''
    if x == 0:
        return 0
    if n == 0:
        return 1
    elif n > 0:
        res = 1
        for i in range(n):
            res = res * x
        return res
    else: # n < 0 
        return None

#des appels 
r1 = puissance(0, 1)
print("r1=", r1)

un = 1
encore_un = puissance(un, 3)
print("encore_un=", encore_un)

for i in range(10):
    r = puissance(2, i)
    print("2 **", i, "=", r)

bof = puissance(3, -1)
print(bof)


# In[ ]:


def perm(a : int, b : int) -> None:
    '''procedure de permutation
    avec variable supplémentaire'''
    t = a
    a = b
    b = t
    return None

def perm2(a : int, b : int) -> None:
    '''procedure de permutation
    solution avec des entiers et sans variable intermédiaire'''
    a = a + b
    b = a - b
    a = a - b
    return None

x = 5
y = 10
print(x, y)
perm(x, y)
print(x, y)
perm2(x, y)
print(x, y)


# In[ ]:


def f(n : int) -> int:
    '''je vais vite'''
    return n + 2


# In[ ]:


help(f)


# In[ ]:


z = f(3)
print(z)


# In[ ]:


f(3)


# # Boucles avancées

# ## Ce qu'il faut savoir
# 
# - Structure de données : représentation d'un tableau multidimensionnel comme une liste de listes  
# - Structure de contrôle de type boucles imbriquées indépendantes et dépendantes : 
#     - intérêt et exemples simples, 
#     - dénombrer les itérations de ces constructions.

# ## Ce qu'il faut savoir faire 
# 
# **Cadre** : en/pour python 
# 
# - Définir et écrire un traitement classique de tableau multidimensionnel  : parcours simple, parcours conditionnel 
# - Ecrire une initialisation de tableau multidimensionnel en python (représenté par des listes)
# - Définir et écrire une spécification de fonction avec des paramètres de type tableau  
# - Identifier les cas particuliers liés à la structure de tableau : tableau de dimension 0, tableau vide

# ## Compléments en séance

# In[ ]:


def exemple(t : int):
    '''exemple de docstring'''
    return None

exemple(3)

help(exemple)


# In[ ]:


l = [0 for _ in range(3)]
print(l)


# In[ ]:


c = ''
type(c)


# In[ ]:


for i in range(0):
    print("XX")
    


# In[ ]:


for i in range(-1):
    print("XX")    


# # Complexité

# ## Avoir les idées claires
# 
# - Principes de l'analyse de la complexité en temps : modèle de calcul RAM, paramètres de complexité, meilleur et pire cas
# - Complexité asymptotique : notations de Landau, principales classes de complexité des algorithmes, interprétation pratique de ces classes
# - Complexité, pire-meilleurs cas des algorithmes vus ce semestre
# - Savoir établir la complexité d'algorithmes itératifs simples ou récursifs terminaux.
# 

# ## Savoir-faire
# 
# - Exemples d'algorithme des principales classes de complexité 
# - Savoir identifier (sans nécessairement le prouver) la complexité, les meilleur-pire cas d'un algorithme  

# # (P) Entrées-Sorties : fichiers

# ## Compléments
# 
# ### Fonction avec paramètre fichier
# 
# Comment spécifier fonctions qui manipulent des fichiers de texte arbitraire via un (ou des) paramètre d'entrée ?
# 
# Plusieurs solutions:
# 1. se limiter au passage de paramètre du fichier physique. dans ce cas, le type du paramètre est `str`. 
# 2. TODO : utiliser le type des fichiers logiques défini par python
#     - on l'identifie grace à la fonction `type()`.

# In[ ]:


get_ipython().system(' ls ./tmp')


# #### Cas du fichier physique

# In[ ]:


def f_avec_fichier_physique(file : str) -> None:
    with open("./tmp/exemple.txt", "r", encoding = "utf8") as f:
        for val in f:
            print(val)
        f.close()


# In[ ]:


f_avec_fichier_physique("./tmp/fichier_entrees.txt")


# #### Cas du fichier logique

# In[ ]:


with open("./tmp/exemple.txt", "r", encoding = "utf8") as f:
    print(type(f))
    f.close()


# In[ ]:


def f_avec_fichier_logique(file : _io.TextIOWrapper) -> None:
    assert f.open == True 
    for val in f:
        print(val)
        


# In[ ]:





# ## Avoir les idées claires
# 
# - Distinguer fichier logique _vs._ physique, texte _vs._ binaire, mode lecture _vs._ écriture (_vs._ lecture-écriture) 
# - Connaître les étapes de manipulation d'un fichier : association/ouverture/lecture-écriture/fermeture
# - Distinguer valeur (numérique) et sa représentation textuelle 
# 
# ## Savoir-faire
# 
# - Savoir écrire les lectures-écritures simples de fichier texte avec les instructions python adaptées  
# - Comprendre et gérer l'effet des caractères spéciaux 

# # Types composés (P), structures de données
# 
# Bien comprendre l'intérêt de telle ou telle autre type composé python, ou la structure de données sous-jacente (algorithmique).
# 
# ## Tableau
# 
# Tableau = valeurs de même type, en nombre connu, stockées de façon consécutives en mémoire
# 
# **Conséquences**
# - taille _statique_ : risque de dépassement de la taille maximale    
# - temps d'accès en lecture = constant vs. taille du tableau, position de la valeur dans le tableau
# 
# - temps d'accès en écriture (modification/ajout) de valeur = constant
# 

# ## Liste
# 
# Liste = valeurs de type quelconque, en nombre quelconque
# 
# **Conséquences.**
# - taille _dynamique_     
# - temps d'accès en lecture = ?
# - temps d'accès en écriture = ?
# 

# In[1]:


i = 3
j = 5
tab = [17.0, 12.0]
liste = [1, 2]
k = 7
j = k
l = 9
liste.append(5)


# **Une représentation :**
# > liste :  (valeur, -> suivante), (valeur, -> suivante), (valeur, -> suivante), (valeur, fin)
# 
# - temps accès en lecture dépend de la position de la valeur cherchée, ie. longueur de la liste
#     - pire cas = dernière valeur, 
#     - **linéaire** en la taille de la liste.
# - temps accès en écriture ou ajout/suppression de valeur : 
#     - même raison : **linéaire** en la taille de la liste.  
#     
# **Rmq** . Temps accès d'ajout **constant** en stockant aussi la position du dernier élément de la liste.
# > liste : (dernière position) + (valeur, -> suivante), (valeur, -> suivante), (valeur, -> suivante), (valeur, fin)
# 
#     

# ## Dictionnaire
# 
# Dictionnaire
# - valeurs de type quelconque, en nombre quelconque, 
# - **clé** -> valeur
# 
# La donnée de cette **clé** permet **une représentation** telle que :
# - temps d'accès en lecture = (presque) constant vs. taille du tableau, position de la valeur dans le tableau 
# - temps d'accès en écriture ou ajout/suppression = (presque) constant
# 
# Une telle représentation s'appuie sur une fonction (dite fonction de hashage) qui transforme une clé en une position unique (en mémoire). 
# 
# **Rmq.**
# - "presque" car : risque de collision et temps de calcul de la fonction de hashage (pour une clé donnée)

# ## Spécification de fonctions et types composés

# In[ ]:


'''
Ceci fonctionne en python 3.9 !!!

# list[int] n'est pas reconnu
# TypeError: 'type' object is not subscriptable
def f(l : list[int], n: int) -> int:
    l = [i for i in range(n)]
    return len(l)
    
# idem pour dict[]    
def f(d : dict[str, int], n: int) -> int:
    d = [i for i in range(n)]
    return len(l)
    
vector = list[float]
def somme(v : vector) -> flaot:
    s = 0
    for val in v:
        s = s + val
        return s
'''


# In[ ]:


from typing import List, Dict

def f(l : List[int], n: int) -> int:
    ll = l[:n]
    return len(ll)

def f(d : Dict[str, int], n: int) -> int:
    d = [i for i in range(n)]
return len(l)


# In[10]:





# ## Avoir les idées claires
# 
# voir cours 
# 
# ## Savoir-faire
# 
# voir cours

# # (P) Entrées-Sorties : aspects avancés

# ## Avoir les idées claires
# 
# - Connaitre les principes du formatage des données pour pouvoir retrouver rapidement dans la documentation (de cours ou de référence) les commandes pour effectuer ce traitement.
# 
# ## Savoir-faire
# 
# - Utiliser les formatages de base des types `int` et `float` de python
# - En s'appuyant sur les documents de cours ou de référence, définir et appliquer des formatages évolués et adaptés aux données manipulées avec python

# In[ ]:




