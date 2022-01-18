#!/usr/bin/env python
# coding: utf-8

# # Les 'ndarray' : de vrais tableaux en python
# 
# version 2020, PhL.

# Chapitre où sont présentés les vrais tableaux en python : les `ndarray` (tableaux) `numpy`.
# 
# Les sections avec une $\star$ sont de niveau _Objectif 20_. 

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Les-'ndarray'-:-de-vrais-tableaux-en-python" data-toc-modified-id="Les-'ndarray'-:-de-vrais-tableaux-en-python-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Les 'ndarray' : de vrais tableaux en python</a></span><ul class="toc-item"><li><span><a href="#Les-tableaux" data-toc-modified-id="Les-tableaux-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Les tableaux</a></span><ul class="toc-item"><li><span><a href="#La-vision-classique" data-toc-modified-id="La-vision-classique-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>La vision classique</a></span></li><li><span><a href="#En-python" data-toc-modified-id="En-python-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>En python</a></span></li></ul></li><li><span><a href="#Les-ndarray-de-numpy" data-toc-modified-id="Les-ndarray-de-numpy-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Les <code>ndarray</code> de <code>numpy</code></a></span><ul class="toc-item"><li><span><a href="#Préliminaire-nécessaire-à-l'utilisation-de-numpy" data-toc-modified-id="Préliminaire-nécessaire-à-l'utilisation-de-numpy-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Préliminaire nécessaire à l'utilisation de <code>numpy</code></a></span></li><li><span><a href="#Créer-un-ndarray-:-fonctions-de-création" data-toc-modified-id="Créer-un-ndarray-:-fonctions-de-création-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Créer un <code>ndarray</code> : fonctions de création</a></span></li><li><span><a href="#Choisir-le-type-des-valeurs-à-la-création" data-toc-modified-id="Choisir-le-type-des-valeurs-à-la-création-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Choisir le type des valeurs à la création</a></span></li><li><span><a href="#Accéder-aux-éléments-d'un-ndarray" data-toc-modified-id="Accéder-aux-éléments-d'un-ndarray-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Accéder aux éléments d'un <code>ndarray</code></a></span></li><li><span><a href="#Afficher-un-ndarray:-fonction-d'affichage" data-toc-modified-id="Afficher-un-ndarray:-fonction-d'affichage-1.2.5"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>Afficher un <code>ndarray</code>: fonction d'affichage</a></span></li><li><span><a href="#Méthodes-d'introspection" data-toc-modified-id="Méthodes-d'introspection-1.2.6"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>Méthodes d'introspection</a></span></li><li><span><a href="#Fonctions-:-élément-par-élément-vs.-tableau" data-toc-modified-id="Fonctions-:-élément-par-élément-vs.-tableau-1.2.7"><span class="toc-item-num">1.2.7&nbsp;&nbsp;</span>Fonctions : élément-par-élément vs. tableau</a></span></li><li><span><a href="#Définir-des-ndarray-à-partir-de-listes-python-(lst)" data-toc-modified-id="Définir-des-ndarray-à-partir-de-listes-python-(lst)-1.2.8"><span class="toc-item-num">1.2.8&nbsp;&nbsp;</span>Définir des <code>ndarray</code> à partir de listes python (<code>lst</code>)</a></span></li></ul></li><li><span><a href="#Aspects-plus-avancés----($\star$)" data-toc-modified-id="Aspects-plus-avancés----($\star$)-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Aspects plus avancés    ($\star$)</a></span><ul class="toc-item"><li><span><a href="#Autres-constructeurs-et-autres-descripteurs" data-toc-modified-id="Autres-constructeurs-et-autres-descripteurs-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Autres constructeurs et autres descripteurs</a></span></li><li><span><a href="#Autres-fonctions-et-méthodes-utiles" data-toc-modified-id="Autres-fonctions-et-méthodes-utiles-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Autres fonctions et méthodes utiles</a></span></li></ul></li><li><span><a href="#Synthèse" data-toc-modified-id="Synthèse-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Synthèse</a></span></li></ul></li></ul></div>

# ## Les tableaux 
# 
# Les _types scalaires_ permettent de manipuler des valeurs scalaires comme les :  
# - `bool`  
# - `int`  
# - `float`  
# - `complex`  
# - les caractères souvent dénotés de type _char_ (absent en python).   
# 
# Un _type composé_ permet de regrouper plusieurs valeurs, de même type scalaire ou non, dans une seule variable (ou un seul objet).  
# Il y a plusieurs _familles_ de types composés.
# Les tableaux sont l'une d'entre elles.

# 
# ### La vision classique  
# 
# **Les tableaux**  sont définis comme des ensembles :  
# - de valeurs _de même type_  
# - en nombre connu et fixé "une fois pour toute" lors de leur définition  
# - et dont les valeurs sont _stockées de façon contigüe en mémoire_.  
# 
# Le nombre de valeurs stockées dans un tableau est la _taille_ ou la _dimension_ de ce tableau. 
# 
# - Un tableau peut être 1D (linéaire) ou multidimensionnel : 2D (matrice), 3D, ...  
# - Les valeurs du tableau sont repérées par un ou des _indices_ , entiers et consécutifs.  
# - Il y a autant d'indices que de dimensions du tableau : 
#     - 1D = 1 indice `i` : le numéro `i` de la case qui contient la valeur  
#     - 2D = 2 indices `i` et `j` : les numéros de _ligne_ et de _colonne_ de la case qui contient la valeur  
#     - et ainsi de suite ...

# ### En python 
# 
# Nous verrons au chapitre suivant des tas de types composés proposés par python.  
# Au semestre 1, les **listes python** (vous) ont été présentées comme une façon de représenter des tableaux.  
# Nous verrons qu'une liste python est très différente de la définition -- la vision classique -- des tableaux.  
# 
# Voilà pourquoi nous allons étudier les `ndarray`, qui définissent un type composé fourni par le module `numpy` et qui correspondent aux tableaux classiques.
#     

# ## Les `ndarray` de `numpy`
# 
# Les `ndarray` de `numpy` sont ainsi appelés car :
# - `array` : tableau in english,  
# - `nd` : $n$-dimension.  
# 
# **ATTENTION** : il existe des `array` dans la bibliothèque standard de python.  

# ### Préliminaire nécessaire à l'utilisation de `numpy`
# Ce qui suit concerne les `ndarray` du module `numpy` utilisables après un `import numpy` ou le classique :  

# In[1]:


import numpy as np


# ### Créer un `ndarray` : fonctions de création 
# 
# La création d'un `ndarray` est un peu pénible au début.
# Il faut utiliser un des _constructeurs_ définis dans le tableau ci-dessous.
# Le choix d'un constructeur dépend de la connaissance ou non des valeurs du `ndarray`. Bien sûr, le nombre d'éléments de `ndarray`, ou de façon équivalente le produit de ses dimensions, doit être connu avant la création du `ndarray`. 
# 
# identifiant | Argument | Famille |Rôle  
# ------------| ---------|---------|----  
# `zeros()` | `tuple` d'`int`| **constructeur** | créé un tableau rempli de _zéros_ et de dimension et de tailles définies comme argument  
# `ones()` | `tuple` d'`int`| constructeur | créé un tableau rempli de _1_ et de dimension et de tailles définies comme argument  
# `arange()` | range d'`int` ou de `float`| constructeur | créé un tableau 1D rempli des valeurs du _range_ défini comme argument   
# 
# 
# On verra aussi un peu plus loin un autre constructeur qui permet de définir un `ndarray` à partir de la liste python `lst` de ses valeurs.  

# In[2]:


t0 = np.zeros(3)
t1 = np.ones(5)
t2 = np.arange(10)

print("Créations de ndarray :")
print(t0)
print("t1 =", t1)
print("t2 =", t2)

t34 = np.ones( (3, 4) )
print("t2D de 3 lignes et 4 colonnes : \n", t34)

t23 = np.arange(10)
print(t23)

#help(np.arange)


# ### Choisir le type des valeurs à la création
# 
# Le paramètre `dtype` (_data-type_) permet de définir type des valeurs du `ndarray` lors de sa création.
# 
# `dtype` :  
# * est utilisé comme paramètre nommé de certaines fonctions pour définir le type numérique des valeurs  
# * les valeurs de `dtype` dépendent de l'environnement; les plus classiques sont :   
#     - ceux de python : `int`, `float`, `complex`  
#     - et `numpy` en propose d'autres : `uint8`, `int16`, `int32`, `int64`, `float32`, `float64`, ...   

# In[3]:


t0 = np.zeros(3, dtype = int)
t1 = np.ones(5, dtype = float)
t11 = np.ones(5, dtype = np.float32)
t2 = np.arange(10, dtype = complex)

print("Création de ndarray :")
print("t0 = ", t0)
print("t1 =", t1)
print("t11 =", t11)
print("t2 =", t2)


# In[4]:


help(np.zeros)


# ### Accéder aux éléments d'un `ndarray`
# 
# On manipule les élements, les tranches de tableau avec la même syntaxe que les `str` ou les `lst`:   
# - `t[5]`  
# - `tab[0:3, :]`  
# - ...  
# 
# <div class="alert alert-block alert-info">
# 
# **Indices de tableaux multi-dimentionnels :** les deux écritures suivantes sont possibles.   
# - dans `t` un tableau 2D (matrice), l'élément à la ligne i et à la colonne j s'écrit : `t[i, j]` _ou_ `t[i][j]`  
# 
# On pourra préférer `t[i, j]` qui permet de bien distinguer les `ndarray` des listes (de listes).  
# </div>

# In[5]:


print(t34[1, 2] == t34[1][2])


# ### Afficher un `ndarray`: fonction d'affichage
# 
# On aura remarqué que la fonction `print()` accepte et traite correctement un argument de type `ndarray`.  
# Et même sans avoir à préciser :  
# - les dimensions et les tailles de l'argument  
# - le type de ces valeurs.  
# 
# `numpy` propose ainsi une fonction d'affichage d'une utilisation identique au `print()`de python.  
# Comprendre qu'il y a en fait plusieurs fonctions `print()` mais qu'elles partagent le même nom.
# 
# **Quizz**
# - Quelle est la limitation d'une telle fonction `print()`?

# ### Méthodes d'introspection    
# 
# Les méthodes d'introspection sont des fonctions qui retournent des caractéristiques des variables (objets) auxquelles elles s'appliquent.  
# Ce sont des _méthodes de description_.
# 
# identifiant | Argument | Famille |Rôle  
# ------------|----------|---------|-----  
# `.ndim` | `array`| **descripteur** | retourne le nombre de dimensions du tableau argument  
# `.shape`| `array`| descripteur | retourne, sous la forme d'un t-uple, les dimensions du tableau argument  
# `.size` | `array`| descripteur | retourne le nombre d'éléments du tableau argument  
# `.dtype`| `array`| descripteur | retourne le type des éléments du tableau argument  
# 
# <div class="alert alert-block alert-info">
#     
# La **notation pointée** agit comme les parenthèses d'une fonction : elle permet de nommer la variable (l'objet) à laquelle l'introspection s'applique.  
#     
# </div>

# In[6]:


print("Plus de détails : tableau 1D")
i = 3
print(type(i))
print(type(t0)) # type() est une fonction python
print()

print("Plus de détails sur le tableau 1D avec des méthodes : ")
print("t.dim avec t un nd-array:", t0.ndim, t1.ndim, t2.ndim)
print("t.shape avec t un nd-array:", t0.shape, t1.shape, t2.shape)
print("t.size avec t un nd-array:", t0.size, t2.size, t2.size)
print()

print("Et des détails sur les valeurs du tableau 1D :")
print(t0.dtype)
print(t0.itemsize)
print()


# In[7]:


print("Plus de détails avec tableau 2D :")
print(type(t34)) 

print("t.dim:", t34.ndim)
print("t.shape:", t34.shape)
print("t.size:", t34.size)

print("Et des détails sur les valeurs du tableau : dtype, itemsize", t34.dtype, t34.itemsize)
print()


# In[8]:


v = np.ones(17)
t1 = np.ones((2,3))
print(v, t1)
print("np.ones((2,3)):", t1.ndim, t1.shape, t1.size)
print() 


# In[9]:


t2 = np.arange(2,11,0.5)
print("t2=",t2)
print("size :", t2.size)
print()

t2f = np.arange(6.0)
print("t2f=",t2f)
print("size :", t2f.size)
print()


# ### Fonctions : élément-par-élément vs. tableau
# 
# Les `ndarray`bénéficient d'opérations vectorielles et matricielles ainsi que des traitements d'algèbre linéaire :  
# * `dot()`: produit scalaire (aussi `vdot`),  
# * `dot()` ou `@` : produit matriciel,   
# * `transpose()`ou méthode `.T` : transposition   

# **ATTENTION**  Les autres fonctions travaillent __élément-par-élement__ (_element-wise_) en utilisant la _surcharge_ des opérateurs.
# 
# Ainsi ces fonctions retournent des `ndarray` de forme induite par celles des opérandes.  
# 
# * opérateurs arithmétiques (surchargés et s'appliquant element-wise)  : `+`, `-`, `*`, `/`,  `//`, `%`, `divmod()`, `**`, `pow()`  
# * opérateurs logiques : `&`, `^, `|`, `~`   
# * comparaisons : `==`, `<`, `>`, `<=`, `>=`, `!=`    
# * fonctions : `sqrt()`, `exp()`, ...    

# <div class="alert alert-block alert-danger">
# 
# **ATTENTION :** Le produit matriciel classique est `A @ B` tandis que `A * B` est le produit élément-par-élement.
# 
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# **ATTENTION :** La mise en garde précédente s'appuie sur le fait que __seul__ le type __ndarray__ de numpy a été introduit dans ce cours.  
# En particulier, le terme suivant est utilisé une et une seule fois, ici : matrix!
# 
# </div>

# ### Définir des `ndarray` à partir de listes python (`lst`)  
# 
# L'exemple suivant utilise un autre constructeur, dénoté `np.array()` qui définit un tableau `ndarray` à partir de la _liste_ de ses valeurs (cf. paragraphe suivant).

# In[10]:


vi = np.array([1,0,0])
print(vi)
print()

m23 = np.array([[1,1,1], [2,2,2]])
print(m23)


# In[11]:


vi = np.array([1,0,0])
vj = np.array([0,1,0])
vk = np.array([0,0,1])
print(vi, vj, vk) 

zero = np.dot(vi, vj)
autre_zero = np.vdot(vi, vj)
print("comparaison scalaire:", zero == autre_zero)
print()

print("égalité élement-élément:", vi == vj)
print("comparaison élement-élément:", vi > vj)
un_autre_vecteur = vi * vj
print(un_autre_vecteur)
print("comparaison élément-élement:", zero == un_autre_vecteur)
print()

I3 = np.array([vi, vj, vk])
print("I3="); print(I3)
I2 = I3[0:2, 0:2]
print("I2="); print(I2)
print()

K = I3[2, :]
print("tranche de tableau:", K)
print(vk == K)


# <div class="alert alert-block alert-warning">
#     
# Les opérations composées (avec affectation) `+=` ou `*=` effectuent un traitement _en place_, c-a-d sans créer un nouvel objet.
# 
# </div>

# ## Aspects plus avancés    ($\star$)
# 
# ### Autres constructeurs et autres descripteurs 
# 
# 
# identifiant | Fonction ou Méthode| Argument | Famille |Rôle
# ------------|--------------------|----------|---------|----
# `array()`| F | `lst` | **constructeur** | créé un tableau à partir d'un argument `lst` python  
# `reshape()` | F | `ndarray`et `tuple`d'`int`| **constructeur** | redimensionne aux dimensions définies dans le tuple argument, un tableau existant (et compatible) passé comme argument 
# `.strides` | M | `array`| descripteur | retourne l'espace, mesuré en octets, entre 2 éléments consécutifs _dans une direction donnée_ de chaque élément du tableau argument ; ces valeurs sont retournées sous la forme d'un tuple
# `.itemsize` | M | `array`| descripteur | retourne la taille en octets de chaque élément du tableau argument  

# In[12]:


t12 = np.zeros(12).reshape(4,3)
print("t12=",t12)
print()

t12.reshape(6,2)
print("Attention au (no-)reshape : t12.reshape(6,2)")
print(t12.shape); print("t12=", t12)
print()

t12bis = np.reshape(t12,(6,2))
print("t12bis = t12.reshape(6,2)")
print(t12bis.shape); print("t12bis=", t12bis)
print()

print("t12 et t12bis : même tableau en mémoire ?", id(t12) == id(t12bis))


# **Attention :** La forme (shape) du tableau est fixée une fois pour toute à sa définition.  
# `reshape()`, vu comme une fonction, ne modifie pas la forme d'un tableau existant mais permet de construire si besoin un _nouveau_ tableau structuré différemment d'un tableau existant.   
# Ce nouveau tableau est obtenu lors de l'affectation du résultat (de la fonction) constructeur `reshape()`  
# 
# 
# **Difficile :** En pratique, cette "remise en forme" d'un tableau pose des questions quant à son stockage _contigu_ en mémoire. En effet, la mémoire est linéaire (1D) et ré-organiser un tableau n-D de façon contigue dans un espace 1D peut s'effectuer de façons diverses : ligne après ligne _vs._ colonne après colonne pour un tableau 2D par exemple, ...    

# In[13]:


print("comparaison :", t12 == t12bis)
print("shapes :", t12.shape, t12bis.shape)
print("id :", id(t12), id(t12bis))


# In[14]:


t = np.array([1,0])
print(t)
print(type(t))
print(t.dtype)
print(t.strides)


# In[15]:


Id = np.array([[1,0],[0,1]])
A = np.arange(5,9).reshape(2,2)
print(Id)
print(A)
print()

reA = np.dot(Id, A)
B = Id * A
print(reA)
print(B)


# In[16]:


import numpy as np 

tc = np.array( [complex(1,2), complex(3,4)] , dtype=complex )
tc2 = np.array( [ [1,2], [3,4]] , dtype=complex )
tc3 = np.array( [ 1+2.j, 3+4.j ] , dtype=complex )

t_2d = np.array( [ [1,2], [3,4] ])

print(tc, tc.dtype)
print(tc2, tc2.dtype)
print(tc3, tc3.dtype)

print(t_2d, t_2d.dtype)


# <div class="alert alert-block alert-warning">
# 
# **Création $\neq$ affectation.**   
# 
# L'affectation entre `ndarray` :`tab2 = tab1` ne créé pas un nouvel `ndarray` `tab2`. 
#     
# On retrouvera ce comportement avec **types mutables** python : `list` et `dict`.
# 
# En revanche, les précédentes fonctions de création produisent l'effet attendu. 
# 
# </div>

# ### Autres fonctions et méthodes utiles
# 
# En vrac des fonctions et des méthodes qui manipulent (en entrée et sortie) des `ndarray` :  
# 
# *  `linspace(a,b,nb)` : fonction qui génère et retourne un tableau `ndarray` de `nb` valeurs régulièrement espacées entre `a` et `b`  
# * `empty(shape)` génère et retourne un tableau `ndarray` _non initialisé_ et de dimension `shape`   
#     * *Rmq.* mentionné pour insister sur l'intérêt des constructeurs `zeros()` et `ones()`!!!  
# * `axis` : notion d'axe   
#     * `axis= 0, 1, ...` désignent les première, deuxième, ... dimensions du `ndarray`  
#     * est utilisé comme paramètre nommé de certaines méthodes pour désigner _où s'applique_ le traitement   
#     * exemple : `a23.sum(x)` retourne les sommes `[ a[0,0]+a[1,0], a[0,1]+a[1,1], a[0,2]+a[1,2] ]`  
#     * concerne aussi les méthodes :  `.min()`, `.argmin()`, ...,  `.mean()`, `.var()`, `.std()`  
# 
# Plus de détails [l'initiation](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) et la documentation de [numpy](https://docs.scipy.org/doc/numpy-dev/reference/index.html).
# 

# In[17]:


a23 = np.empty((2,3), dtype="float32")
print(a23, "\n on vous aura prévenu !")
print(a23.dtype)
print()

i33 = np.empty((3,3), dtype="int16")
print(i33, "\n on vous aura bien prévenu !")
print(i33[0,0].dtype)
print() 

for i in range(len(i33[:, 0])):
    i33[i, :] = 2*i
print(i33)
print(i33.mean(axis=0))
print(i33.mean(axis=1))


# ## Synthèse 
# * `ndarray` de `numpy` : des vrais tableaux nD  
#     - L'espace de stockage en mémoire d'un _vrai_ tableau est _fixé une fois pour toute_ à la création du tableau.   
#     - Ainsi, la taille d'un tableau ne peut pas changer après sa création. Il faut donc connaitre le nombre maximal de valeurs qu'il doit contenir dès cette création.   
# * Quand les choisir ?  
#     - les `ndarray` pour du calcul numérique type algèbre linéaire   
#     - les `ndarray` pour des tableaux multi-dim plein de valeurs numériques  
#     - Dans ces deux cas, les préférer aux `lst` python    
# * `numpy` propose de multiples autres fonctions pour manipuler efficacement des tableaux.   
# * Se référer à [quickstart numpy](https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html)  (en anglais).  

# ```
# jupyter nbconvert 3p-ndarray.ipynb --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --SlidesExporter.reveal_theme=solarized
# ```
