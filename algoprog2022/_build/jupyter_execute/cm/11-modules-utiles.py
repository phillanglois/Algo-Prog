#!/usr/bin/env python
# coding: utf-8

# # Modules utiles : `random`, `matplotlib` et `time`  pour des expériences de complexité. 
# 
# v 1.21

# Petites expériences qui nous permettent de découvrir des modules bien utiles :   
# - d'introduire **de l'aléatoire** avec `random` 
#     - pour générer des données de test, de débug, ...
# - d'apprendre à **faire des graphiques** avec `matplotlib`  
# - d'utiliser des fonctions de modules importés du module `time` pour **mesurer des temps d'exécution**,  
#     - et ainsi apprécier la validitité et les limites de la notion de complexité algorithmique, 
# 

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Modules-utiles-:-random,-matplotlib-et-time--pour-des-expériences-de-complexité." data-toc-modified-id="Modules-utiles-:-random,-matplotlib-et-time--pour-des-expériences-de-complexité.-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Modules utiles : <code>random</code>, <code>matplotlib</code> et <code>time</code>  pour des expériences de complexité.</a></span><ul class="toc-item"><li><span><a href="#De-l'aléa-avec-le-module-random" data-toc-modified-id="De-l'aléa-avec-le-module-random-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>De l'aléa avec le module <code>random</code></a></span><ul class="toc-item"><li><span><a href="#Principe-d'un-générateur-pseudo-aléatoire" data-toc-modified-id="Principe-d'un-générateur-pseudo-aléatoire-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Principe d'un générateur <strong>pseudo</strong>-aléatoire</a></span></li><li><span><a href="#Fonctions-utiles" data-toc-modified-id="Fonctions-utiles-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Fonctions utiles</a></span></li></ul></li><li><span><a href="#Tracer-avec-matplotlib" data-toc-modified-id="Tracer-avec-matplotlib-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Tracer avec <code>matplotlib</code></a></span><ul class="toc-item"><li><span><a href="#matplotlib-:-qu'est-ce-que-ça-fait-?" data-toc-modified-id="matplotlib-:-qu'est-ce-que-ça-fait-?-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span><code>matplotlib</code> : qu'est ce que ça fait ?</a></span></li><li><span><a href="#matplotlib-:-comment-ça-le-fait-?" data-toc-modified-id="matplotlib-:-comment-ça-le-fait-?-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span><code>matplotlib</code> : comment ça le fait ?</a></span></li><li><span><a href="#Exercice" data-toc-modified-id="Exercice-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Exercice</a></span></li><li><span><a href="#A-vous-maintenant-!" data-toc-modified-id="A-vous-maintenant-!-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>A vous maintenant !</a></span></li></ul></li><li><span><a href="#($\star$)-Mesurer-le-temps-d'exécution-d'un-programme" data-toc-modified-id="($\star$)-Mesurer-le-temps-d'exécution-d'un-programme-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>($\star$) Mesurer le temps d'exécution d'un programme</a></span><ul class="toc-item"><li><span><a href="#Pas-si-simple-..." data-toc-modified-id="Pas-si-simple-...-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Pas si simple ...</a></span></li><li><span><a href="#Mesurer-avec-le-module-time" data-toc-modified-id="Mesurer-avec-le-module-time-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Mesurer avec le module <code>time</code></a></span></li><li><span><a href="#Un-benchmark-en--$\theta(n)$-:-la-somme-itérative" data-toc-modified-id="Un-benchmark-en--$\theta(n)$-:-la-somme-itérative-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>Un <em>benchmark</em> en  $\theta(n)$ : la somme itérative</a></span></li><li><span><a href="#Un-premier-exemple" data-toc-modified-id="Un-premier-exemple-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>Un premier exemple</a></span></li></ul></li><li><span><a href="#Première-mesure-de-complexité" data-toc-modified-id="Première-mesure-de-complexité-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Première mesure de complexité</a></span><ul class="toc-item"><li><span><a href="#Des-données-de-taille-variable" data-toc-modified-id="Des-données-de-taille-variable-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Des données de taille variable</a></span></li></ul></li></ul></li></ul></div>

# ## De l'aléa avec le module `random`

# Commençons par ce module déjà utilisé au semestre 1.  
# 
# Les expérimentations demandent souvent _mais pas systématiquement_ de générer des données aléatoires.  
# Le module `random` permet ça, ou presque car la génération __déterministe__ de valeurs a priori quelconques est un processus __pseudo-aléatoire__ .  

# ### Principe d'un générateur **pseudo**-aléatoire
# 
# - une graine : $u_0$  
# - une récurrence déterministe : $u_n = f(u_{n-1})$ où $f$ définit de l'_aléa_.

# ### Fonctions utiles
# Après un :

# In[1]:


import random


# - `random.seed()` : graine du générateur
#     - fixer la graine permet la _reproductibilité_ de la génération pseudo-aléatoire
# 
# **Lois discrètes (entières)** 
# - `random.randint(a, b)` : uniforme _discrète_ sur [a, b] <-- remarquer l'intervalle fermé !  
# - `random.randrange(a, b, pas)` : uniforme _discrète_ sur [a, a+pas, a+2*pas, ..., b[ (intervalle ouvert à droite) 
# 
# **Lois continues**    
# - `random.random()`  : uniforme sur [0,1]
# - `random.uniform(a, b)` :  uniforme sur [a,b]
# - `random.gauss(moyenne, ecart_type)` : Normal($\mu$, $\sigma$)

# In[2]:


#help(random)

n = 10
t0 = [0 for i in range(n)]
t1 = [0 for i in range(n)]
t2 = [0 for i in range(n)]
t3 = [0 for i in range(n)]

# graine arbitrairement choisie par le système 
random.seed()
for i in range(10):
    t0[i] = random.random()

for i in range(10):
    t1[i] = random.random()

# on bloque la graine
random.seed(12345)
for i in range(10):
    t2[i] = random.random()

# on reprend la même graine 
random.seed(12345)
for i in range(10):
    t3[i] = random.random()

print(t0 == t1)
print(t1 == t2)
print(t2 == t3)
print(t1)
print(t2)


# ## Tracer avec `matplotlib`
# 
# C'est utile ... et pas moche ! 

# ###  `matplotlib` : qu'est ce que ça fait ? 
# 
# Le module python `matplotlib` est un module adapté à tous les types de tracés
# scientifiques : courbes, histogrammes, nuages de points, $\dots$ 
# On verra même qu'il permet d'afficher des images, ds photos, ...  
# 
# * Ses options sont très nombreuses, de même que la documentation en
# ligne ou "livrée avec".
# `matplotlib` est composé de nombreux sous-modules. Parmi ceux-ci, celui qui nous intéresse est `pyplot`.  
# L'instruction suivante est très très classique.

# In[3]:


import matplotlib.pyplot as plt


# * L'utilisation basique de `pyplot` consiste : 
#     * à tracer des courbes $x-y$ 
#     * à partir de listes de points, d'un fichier de valeurs ou d'une expression,   
#     * de choisir les bons axes, les bonnes échelles,  
#     * d'indiquer les noms des courbes et des axes, 
#     * de visualiser les tracés à l'écran 
#     * et de les sauvegarder dans des fichiers (pdf ou png).   
# 
# * En pratique, chaque action _modifie l'état de la figure_ en cours d'élaboration.   
# Une action est un appel de fonction `plt`.   
# Il peut être utile de tracer plusieurs "sous-figures" au sein d'une
# même figure. 
# 
# Le module python `numpy` est le compagnon naturel de `matplotlib`.   

# ### `matplotlib` : comment ça le fait ?
# 
# Une première prise en main est très bien décrite par :  
# - [cette présentation](http://www.labri.fr/perso/nrougier/teaching/matplotlib/)  
# - ou le chapitre 3 du [_user guide_](https://matplotlib.org/contents.html) (qui comporte plus de 2500 pages). 
#     

# On va montrer quelques commandes de base :  
# * afficher de courbes : __`plot`__, `figure`, `title`, `legend` ;
# * gérer les axes : `xticks`, `xlim`, `loglog`, `semilogx` ; 
# * gérer les affichages : `show`, `savefig`, `close`.

# ### Exercice  
# Obtenir le tracé des principales classes de complexités : $log_2n$, $n$, $n\ \log_2(n)$, $n^2$, $n^3$, $2^n$ 
# pour les premières puissances de 2 -- par exemple de 2 à 128.   
# 
# A votre avis, pourquoi des échelles logarithmiques sont adaptées ?  
# 
# **Rmq.** 
# - La solution intègre en commentaires quelques commandes utiles au traitement hors des notebook, cad. dans un programme python écrit sous l'idle par exemple.  
# - ligne 45 : elle suppose l'existence d'un répertoire `./tmp` (à adapter si besoin)  

# In[4]:


# complexites.py
"""Trace des principales classes de complexites avec matplotlib"""
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages # cf. à la fin du code

# la figure
plt.figure(figsize=(10,8), dpi = 80)  # size est en pouce...

# son titre
plt.title("Principales fonctions de complexité")

# ses axes en log2
plt.loglog(basex=2, basey=2)

# valeurs affichees sur l axe des x
n = [2**i for i in range(1,8)]  # les premieres puissances de 2  

label_x = [str(val) for val in n]
plt.xticks(n, label_x)

# valeurs affichees sur l axe des y
y_val = [np.power(2, j) for j in range(0, 15, 2)]
 
label_y = [str(val) for val in y_val]
#plt.yticks(y_val, label_y)

# on limite les valeurs de y trop grandes
plt.ylim(1.0, np.power(2,14))
#


# In[ ]:


# tracer
plt.plot(n, np.power(2.0, n), label="$2^n$")
plt.plot(n, np.power(n, 3), label="$n^3$")
plt.plot(n, np.power(n, 2), label="$n^2$")
plt.plot(n, n*np.log2(n), label="$n\ \log_2(n)$")
plt.plot(n, n, label="$n$")
plt.plot(n, np.log2(n), label="$\log_2(n)$")

# afficher la légende à cette position
plt.legend(loc="upper left")

# sortie ecran (inutile sous notebook)
#plt.show()


# In[4]:


#ou fichier pdf : suppose l'existence d'un repertoire ./tmp
pp = PdfPages('./tmp/plt-complexites.pdf')
pp.savefig()
pp.close()


# ### A vous maintenant !
# 
# ##### Le flocon de Von Koch
# 
#  Le flocon de Von Koch (1906) est une courbe fractale
# (continue partout et dérivable nulle part) obtenue comme la limite
# de la transformation suivante appliquée récursivement à un segment
# de départ.
# * le segment est découpée en 3 parties égales,
# * le segment intermédiaire est remplacé par deux segments formant un triangle équilatéral avec le segment supprimé, 
# * et ainsi de suite sur les 4 segments ainsi obtenus.  
# 
# Voici les cinq premières courbes obtenues à partir d'un segment droit
# ou d'un triangle équilatéral : le flocon de Von Koch.  
# On parle aussi de courbe de Von Koch d'ordre $n$ pour la courbe de la
# $n$-ième récursion -- les tracés suivants correspondent aux segments
# de Von Koch d'ordres $0, \cdots, 4$. 

# In[5]:


from IPython.display import Image 
Image(filename='./fig/cinqsegmentsvk.jpg')


# In[6]:


Image(filename='./fig/cinqflocons.jpg')


# ** Traçons-le !**
# 
# On va se limiter à celui avec un segment de départ.  
# Avec `matplotlib`, on choisit de calculer les coordonnées des sommets des
# transformés successifs du segment de départ, puis de les tracer comme
# une courbe. 
# 
# 1. Écrire la fonction `segvk()` qui à partir  des
#   extrémités d'un segment  $[a, b]$, par exemple définies par ses
#   affixes complexes,  calcule et retourne la liste  (des affixes)
#   des points significatifs d'une itération de Von Koch de $[a, b]$.
# 
# 2.  Écrire la fonction `listevk()` qui applique une itération de Von
#   Koch  à une liste de segments.
# 
# 3. Apliquer ces fonctions pour obtenir le tracé `matplotlib` des
#   premières itérations du segment $[-1, 1]$.   
#   
#   Il est agréable d'obtenir ces tracés sous la forme de sous-figures comme présenté ci-dessus.  
#   

# In[7]:


Image(filename='./fig/plt-segvk.png', width=520 )


# ## ($\star$) Mesurer le temps d'exécution d'un programme 

# ### Pas si simple ...
# 
# Mesurer le temps d'exécution d'un programme sur une machine actuelle
# est une une tâche beaucoup plus ardue qu'il n'y parait.
# En effet, l'impression que l'__exécution__ de votre programme
# __mobilise à elle seule les ressources__ de votre ordinateur est une
# __illusion__.

# Le __temps__ que vous attendez pour obtenir votre résultat, même si cela
# vous parait instantané, est en fait __partagé__ : pendant ce même temps,
# votre ordinateur  effectue certainement de nombreuses autres tâches,
# par exemple liées au système d'exploitation, aux périphériques, à
# d'autres utilisateurs si votre machine gère plusieurs sessions, ...  

# Par ailleurs, les unités de calculs et l'organisation (des niveaux) de
# la mémoire compliquent très fortement la mesure fiable des temps
# d'exécution et leur analyse.
# 
# En pratique, __plus ce que vous voulez mesurer est court, plus la mesure
# sera incertaine et non reproductible__.  

# Pour ce qui nous intéresse,
# l'obtention d'une mesure significative consistera à :
# 1.  répéter l'exécution dans une boucle, 
# 1.  mesurer le temps d'excution de __cette boucle__ et
# 1.  en retenir la moyenne. 
# Il n'est pas inutile de répéter ce type de mesures et le cas échéant
# de traiter l'échantillon obtenu.

# Les "gros problèmes" sont aussi sujets à remarque.  
# * Des tailles de données importantes nécessitent un volume important de
# transferts entre la mémoire et les unités de calcul. 
# * Ces transferts mémoire sont complexes ;
# * leurs temps est :
#     * d'une part non linéaire par rapport à la taille des données, 
#     * et d'autre part beaucoup plus important que les temps de calcul souvent associés. 
#       
# A titre indicatif, il y a __un facteur 10 entre ce temps de transfert
# et le temps d'un calcul arithmétique élémentaire__.  
# - ce qui veut dire qu'il faut 10 fois plus de temps pour lire deux valeurs en mémoire que pour faire leur addition, par exemple.  
# 
# Ainsi, les mesures peuvent être surprenantes lorsqu'elles deviennent
# "dominées" par ces temps de transfert.    
# Le modèle de nos analyses de la complexité des algorithmes ne prend
# pas en compte cet aspect vite technique. 

# Pour finir, ceci illustre la différence entre les propriétés d'un
# algorithme et celles de ses mises en oeuvre et, par la même occasion,
# confirme l'intérêt des notations asymptotiques $\cal{O}$, $\theta$,
#   $\Omega$ dont on a souvent signalé qu'elle masquent pas mal de
# détails. 
#   

# ### Mesurer avec le module `time`
# 
# Ce module python fournit beaucoup de fonctions en rapport avec le temps :
# gestions de calendriers, des systèmes horaires, d'horloges ...  
# 
# Il permet aussi une estimation des temps d'exécution des programmes
# python (et autres). 
# La qualité de cette estimation dépend des mises en oeuvre de ce
# module et des machines visées.
# Vous pouvez __être relativement confiant sur vos PC-linux ou mac__.

# * La fonction  `time()` est annoncée avec une précision de la
# seconde, sans que ce soit garanti pour toutes les machines.   
# _Une seconde : c'est beaucoup !_ C'est en effet suffisamment long pour
# effectuer 2 giga = 2 $\cdot 10^9$ opérations ...   
# `time()`  peut donc être utile pour des __mesures grossières__ ou des 
# exécutions __de très gros volumes__.

# * La fonction `perf_counter()` est définie depuis python3.3.  
# Lorsqu'elle est disponible, elle permet les mesures les plus fines
# possibles adaptées à la mesure des temps d'exécution de programmes
# (sans être pour autant exacte, ni reproductible).    
# Elle utilise des fonctions spécifiques aux architectures des machines
# qui exploitent les __compteurs matériels__.  

# Ces fonctions sont __très simples à utiliser__  
# On procède en deux appels qui encadrent la portion de code à mesurer.  
# 
# * `t0 = time.perf_counter()`: le premier appel initialise une valeur initiale
# `t0`;  
# 
# * `t = time.perf_counter()`: le second appel  mesure `t` à l'issue de
#   l'exécution de la portion de code  
#   
# * __`t - t0`__ est la mesure de ce temps d'exécution (moyennant les
# réserves précédentes).  
# 
# Ne pas oublier de _boucler autour_ de la portion à analyser et de _mesurer à l'extérieur_ de cette boucle.  

# ### Un _benchmark_ en  $\theta(n)$ : la somme itérative
# 
# `sommer()` : l'algorithme classique par accumulation itérative.

# In[8]:


def sommer(t, dim_t):
    '''somme itérative de n valeurs entières stockées dans un tableau
    entrées. t : tab d'int de longueur n
    retourne. res : int
    '''
    res = 0
    for i in range(dim_t):
        res = res + t[i]
    return res

# les 10 premiers entiers
tab10 = [i for i in range(1, 10)]

# somme itérative
s1 = sommer(tab10, len(tab10))

# somme des n premiers entiers
n = len(tab10)
s2 = n * (n+1) //2

print(s1, ' = ', s2)


# ### Un premier exemple
# 
# où on compare `time.time()` et `time.perf_counter()` 

# In[9]:


# pour afficher les sorties matplotlib dans le notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


import time
from random import *
import numpy as np
import matplotlib.pyplot as plt

# formats affichage : fx.format(val)
fint = "{:0=8}" #entier sur 7 digits complete avec 0 a gauche
fexp = "{:7.3e}"#float en notation e sur 7 digits dont 3 apres le .
ffl = "{:5.1f}" #float sur 5 digits dont au plus 1 apres le .

# timings operations en O(n) 
dim = 10000
dimmax = dim

# 1. avec des listes python
a = [random() for i in range(dimmax)]
b = [random() for i in range(dimmax)]


# In[11]:


# nb repetititions de chaque mesure
nbrepet = 20

# time : timings operations en O(n) 
# les mesures sont à l'intérieur de la répétition
# car on veut évaluer la sensibilité de ces bestiolles

t_time = [] # les mesures
for repet in range(nbrepet): 
    # la mesure
    t0 = time.time()
    r = sommer(a, dimmax)
    t = time.time()
    #
    t_time.append(t-t0)

# perf_counter
t_tsc = [] # les mesures
for repet in range(nbrepet):
    # la mesure
    t0 = time.perf_counter()
    r = sommer(a, dimmax)
    t = time.perf_counter()
    #
    t_tsc.append(t-t0)


# In[12]:


# aff mesures    
for r in range(nbrepet):
    print(fexp.format(t_time[r]) , fexp.format(t_tsc[r]))


# In[13]:


### trace
#plt.figure()
plt.semilogy(basey=10)
plt.plot(t_time, 'ro-', label="time")
plt.plot(t_tsc, 'b+-', label="perf_counter")
#
plt.legend(loc='upper right')
plt.title('20 mesures répétées')
plt.show()
#plt.close()


# ## Première mesure de complexité 
# 
# ### Des données de taille variable
# 
# L'analyse de complexité dépend de la taille des entrées : $n$.  
# Allons-y pour des mesures comme _fonction de cette taille_.  
# 
# On fait ça avec `time.time()`.  

# In[14]:


# timings operations en O(n) 

# 1. créer des données
dim = [10**i for i in range(2,8)]
dimmax = dim[len(dim)-1]
a = [random() for i in range(dimmax)]

### plus tard :  avec des ndarray et boucle sommer
# creation de ndarray numpy a partir de liste python (conversion)
#aa = np.array(a)

timings_array = []  # les mesures
ratio_array = []    # les ratios

# 2. mesurer
nbrepet = 10
for n in dim: # on parcours les différentes tailles
    t0 = time.time()
    for repet in range(nbrepet): # répéter les exécutions
            sommer(a, n)
    t = time.time()
    
    # timing moyen pour chaque dimension
    tmoy = (t-t0)/nbrepet
    timings_array.append(tmoy)
    ratio_array.append(tmoy/n)

# 3. aff de controle
for n in range(len(dim)):
    print(fint.format(dim[n]), fexp.format(timings_array[n]), fexp.format(ratio_array[n]))

# 4. tracer
plt.loglog(basex=10, basey=10)
plt.plot(dim, timings_array, 'ro-', label="sommer")
plt.xlabel("n : nombre de valeurs à sommer")
plt.ylabel("temps d'exécution (en sec) ou ratio temps/taille")
plt.plot(dim, ratio_array, 'go-', label="sommer / n ")
plt.legend(loc='upper left')


# **Conclusion**  
# - on observe bien un comportement linéaire, ie. en $\theta(n)$.
# 

# ```
# jupyter nbconvert --to html_embed --template toc2 11-modules-utiles.ipynb
# ```

# ```
# jupyter nbconvert 11-modules-utiles.ipynb --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --SlidesExporter.reveal_theme=solarized
# ```
