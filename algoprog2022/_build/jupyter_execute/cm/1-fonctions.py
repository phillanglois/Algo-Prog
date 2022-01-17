#!/usr/bin/env python
# coding: utf-8

# # Sous-programmes : fonctions et procédures
# 
# version 2021, PhL. (v2)

# Dans ce premier chapitre, nous abordons la notion importante de __sous-programme__, souvent aussi appelée __fonction__ -- bien que nous verrons que les 2 notions diffèrent. 
# Le cadre de ce chapitre est très générique, c'est-à-dire que les différentes notions introduites et le vocabulaire associé sont présents dans la très grande majorité des _langages de programmation impérative_. 
# Nous utilisons bien sûr la syntaxe python3 en conservant une indépendance maximale par rapport aux spécificités de python afin de mettre en valeur ces notions de la façon la plus générique possible.
# 
# Le chapitre suivant complétera l'apprentissage de la notion de sous-programme avec des aspects plus techniques et leurs traitements en python. 

# <h1>Table des matières<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Objectifs" data-toc-modified-id="Objectifs-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Objectifs</a></span><ul class="toc-item"><li><span><a href="#Ce-qu'il-faut-savoir" data-toc-modified-id="Ce-qu'il-faut-savoir-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Ce qu'il faut savoir</a></span></li><li><span><a href="#Ce-qu'il-faut-savoir-faire" data-toc-modified-id="Ce-qu'il-faut-savoir-faire-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Ce qu'il faut savoir faire</a></span></li><li><span><a href="#Pré-requis-technique" data-toc-modified-id="Pré-requis-technique-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Pré-requis technique</a></span></li></ul></li><li><span><a href="#Vocabulaire-et-généralités" data-toc-modified-id="Vocabulaire-et-généralités-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Vocabulaire et généralités</a></span></li><li><span><a href="#Introduction-avec-des-exemples" data-toc-modified-id="Introduction-avec-des-exemples-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Introduction avec des exemples</a></span><ul class="toc-item"><li><span><a href="#Les-fonctions-numériques-du-collège-lycée." data-toc-modified-id="Les-fonctions-numériques-du-collège-lycée.-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Les fonctions numériques du collège-lycée.</a></span><ul class="toc-item"><li><span><a href="#Ecriture-mathématique-habituelle" data-toc-modified-id="Ecriture-mathématique-habituelle-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Ecriture mathématique habituelle</a></span></li><li><span><a href="#En-python" data-toc-modified-id="En-python-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>En python</a></span></li><li><span><a href="#Premiers-commentaires-et-vocabulaire-important" data-toc-modified-id="Premiers-commentaires-et-vocabulaire-important-3.1.3"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Premiers commentaires et vocabulaire important</a></span></li></ul></li><li><span><a href="#Les-fonctions-mathématiques-prédéfinies" data-toc-modified-id="Les-fonctions-mathématiques-prédéfinies-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Les fonctions mathématiques prédéfinies</a></span><ul class="toc-item"><li><span><a href="#Appel-:-utilisation-de-fonction-prédéfinie-existante" data-toc-modified-id="Appel-:-utilisation-de-fonction-prédéfinie-existante-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Appel : utilisation de fonction prédéfinie existante</a></span></li><li><span><a href="#Vocabulaire-(suite)" data-toc-modified-id="Vocabulaire-(suite)-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Vocabulaire (suite)</a></span></li></ul></li><li><span><a href="#Distinguer-le-Quoi-du-Comment" data-toc-modified-id="Distinguer-le-Quoi-du-Comment-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Distinguer le <em>Quoi</em> du <em>Comment</em></a></span></li><li><span><a href="#Pourquoi-des-sous-programmes-?-(des-fonctions-?)" data-toc-modified-id="Pourquoi-des-sous-programmes-?-(des-fonctions-?)-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Pourquoi des sous-programmes ? (des fonctions ?)</a></span></li></ul></li><li><span><a href="#Les-grands-principes-:-définition,-signature,-corps-et-appels-de-fonction" data-toc-modified-id="Les-grands-principes-:-définition,-signature,-corps-et-appels-de-fonction-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Les grands principes : définition, signature, corps et appels de fonction</a></span><ul class="toc-item"><li><span><a href="#Définition-d'une-fonction" data-toc-modified-id="Définition-d'une-fonction-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Définition d'une fonction</a></span><ul class="toc-item"><li><span><a href="#Syntaxe(s)-python-de-la-définition-de-fonction" data-toc-modified-id="Syntaxe(s)-python-de-la-définition-de-fonction-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Syntaxe(s) python de la définition de fonction</a></span></li></ul></li><li><span><a href="#La-signature-d'une-fonction" data-toc-modified-id="La-signature-d'une-fonction-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>La signature d'une fonction</a></span></li><li><span><a href="#L'appel-d'une-fonction" data-toc-modified-id="L'appel-d'une-fonction-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>L'appel d'une fonction</a></span><ul class="toc-item"><li><span><a href="#Effet-d'un-appel-sur-le-séquencement-des-instructions-exécutées" data-toc-modified-id="Effet-d'un-appel-sur-le-séquencement-des-instructions-exécutées-4.3.1"><span class="toc-item-num">4.3.1&nbsp;&nbsp;</span>Effet d'un appel sur le séquencement des instructions exécutées</a></span></li></ul></li><li><span><a href="#Le-corps-et-le-retour-de-valeur" data-toc-modified-id="Le-corps-et-le-retour-de-valeur-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Le corps et le retour de valeur</a></span><ul class="toc-item"><li><span><a href="#return" data-toc-modified-id="return-4.4.1"><span class="toc-item-num">4.4.1&nbsp;&nbsp;</span><code>return</code></a></span></li><li><span><a href="#return-=-terminaison-de-la-fonction" data-toc-modified-id="return-=-terminaison-de-la-fonction-4.4.2"><span class="toc-item-num">4.4.2&nbsp;&nbsp;</span><code>return</code> = terminaison de la fonction</a></span></li></ul></li><li><span><a href="#Exercice" data-toc-modified-id="Exercice-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice</a></span></li></ul></li><li><span><a href="#Appel-:-appelant--&gt;-appelé-;-return-:-appelé--&gt;-appelant" data-toc-modified-id="Appel-:-appelant-->-appelé-;-return-:-appelé-->-appelant-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Appel : appelant -&gt; appelé ; return : appelé -&gt; appelant</a></span><ul class="toc-item"><li><span><a href="#Exercice" data-toc-modified-id="Exercice-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice</a></span></li></ul></li><li><span><a href="#Variable-locale-vs.-variable-globale,-portée-des-variables" data-toc-modified-id="Variable-locale-vs.-variable-globale,-portée-des-variables-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Variable locale <em>vs.</em> variable globale, portée des variables</a></span><ul class="toc-item"><li><span><a href="#Exercice" data-toc-modified-id="Exercice-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice</a></span></li></ul></li><li><span><a href="#Compléments" data-toc-modified-id="Compléments-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Compléments</a></span><ul class="toc-item"><li><span><a href="#Erreur-fréquente" data-toc-modified-id="Erreur-fréquente-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Erreur fréquente</a></span></li><li><span><a href="#Méthodologie-d'écriture-des-fonctions" data-toc-modified-id="Méthodologie-d'écriture-des-fonctions-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Méthodologie d'écriture des fonctions</a></span></li><li><span><a href="#De-l'intérêt-de-distinguer-fonction-et-procédure" data-toc-modified-id="De-l'intérêt-de-distinguer-fonction-et-procédure-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>De l'intérêt de distinguer <em>fonction</em> et <em>procédure</em></a></span></li><li><span><a href="#help()-et-docstring" data-toc-modified-id="help()-et-docstring-7.4"><span class="toc-item-num">7.4&nbsp;&nbsp;</span><code>help()</code> et <em>docstring</em></a></span></li><li><span><a href="#Plusieurs-paramètres" data-toc-modified-id="Plusieurs-paramètres-7.5"><span class="toc-item-num">7.5&nbsp;&nbsp;</span>Plusieurs paramètres</a></span></li><li><span><a href="#Plusieurs-return-(rappel)" data-toc-modified-id="Plusieurs-return-(rappel)-7.6"><span class="toc-item-num">7.6&nbsp;&nbsp;</span>Plusieurs <code>return</code> (rappel)</a></span></li><li><span><a href="#Fonction-sans-paramètre" data-toc-modified-id="Fonction-sans-paramètre-7.7"><span class="toc-item-num">7.7&nbsp;&nbsp;</span>Fonction sans paramètre</a></span></li><li><span><a href="#Fonction-locale" data-toc-modified-id="Fonction-locale-7.8"><span class="toc-item-num">7.8&nbsp;&nbsp;</span>Fonction locale</a></span></li><li><span><a href="#Exercice" data-toc-modified-id="Exercice-7.9"><span class="toc-item-num">7.9&nbsp;&nbsp;</span>Exercice</a></span></li></ul></li><li><span><a href="#Synthèse" data-toc-modified-id="Synthèse-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Synthèse</a></span><ul class="toc-item"><li><span><a href="#Retenir" data-toc-modified-id="Retenir-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Retenir</a></span></li><li><span><a href="#Ne-pas-confondre" data-toc-modified-id="Ne-pas-confondre-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Ne pas confondre</a></span></li><li><span><a href="#A-venir" data-toc-modified-id="A-venir-8.3"><span class="toc-item-num">8.3&nbsp;&nbsp;</span>A venir</a></span></li></ul></li><li><span><a href="#Exercices-en-démonstration" data-toc-modified-id="Exercices-en-démonstration-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Exercices en démonstration</a></span><ul class="toc-item"><li><span><a href="#Lister-les-notions-vues-jusqu'ici" data-toc-modified-id="Lister-les-notions-vues-jusqu'ici-9.1"><span class="toc-item-num">9.1&nbsp;&nbsp;</span>Lister les notions vues jusqu'ici</a></span></li><li><span><a href="#Différentes-écritures-de-fonctions-min" data-toc-modified-id="Différentes-écritures-de-fonctions-min-9.2"><span class="toc-item-num">9.2&nbsp;&nbsp;</span>Différentes écritures de fonctions min</a></span></li><li><span><a href="#Une-procédure-d'affichage-(E/S)" data-toc-modified-id="Une-procédure-d'affichage-(E/S)-9.3"><span class="toc-item-num">9.3&nbsp;&nbsp;</span>Une procédure d'affichage (E/S)</a></span></li></ul></li></ul></div>

# ## Objectifs 

# ### Ce qu'il faut savoir
# 
# - définition et paramètres formels vs. appel et paramètres effectifs
# - spécification, en-tête, signature : spécifier pour utiliser, pour vérifier  vs. corps : implémentation du traitement  
# - appel = changement de contexte : trace de l'exécution vs. séquentialité des instructions écrites 
#     - dynamique vs. statique  
# - appelant vs. appelé : le rôle de l'appel, le rôle du `retur``
# - portée des variables : variables locales vs. variables plus globales  
# - l'effet de bord est indésirable  

# ### Ce qu'il faut savoir faire 
# 
# **Cadre** : en/pour python 
# 
# - définir et écrire la spécification d'une fonction qui réalise un traitement décrit en français, ou qui résoud un problème (simple) décrit en français  
# - définir et écrire des appels simples (tests unitaires) 
# - définir et écrire l'implémentation d'une fonction associée à une spécification 

# ### Pré-requis technique
# 
# Dans/avec un notebook jupyter :
# - savoir mettre en oeuvre de la programmation simple en python (niveau semestre 1) dans un notebook jupyter 
# - savoir documenter cette programmation (énoncés, descriptions, ...) avec markdown

# ## Vocabulaire et généralités
# 
# Le terme **sous-programme** est un (sous-)ensemble de lignes de code, souvent paramétrable, que l'on désigne d'un nom pour ré-utiliser "directement" ces lignes de codes à l'aide de ce nom. On _appelle_ ce nom pour exécuter ces lignes de codes. Cet appel contient aussi la valeur des paramètres à traiter par l'exécution.
# 
# De façon imagée, un sous-programme peut-être vue comme une boîte opaque qui "prends des choses" en entrée (les paramètres), effectue des traitements et fourni un "résultat" en sortie -- dans le cas d'une fonction. 
# La boîte porte le nom du sous-programme.
# Elle est opaque : je peux m'en servir, je connais **ce qu'elle fait**, je n'ai pas besoin de savoir **comment** elle le fait.
# 
# Une analogie facile : je peux me servir d'une voiture sans savoir comment la mécanique ou l'électronique fonctionnent.
# 
# Une **fonction** est un sous-programme qui **calcule et renvoie** une (ou des) valeur(s).  
# - exemple : _je_ calcule le double d'une valeur donnée en entrée et _je_ retourne (ou renvoie) ce résultat comme sortie.
# 
# Une **procédure** est un sous-programme qui**réalise une action** -- sans sans renvoyer quoi que ce soit.
# - exemple : _j_'affiche l'heure du moment. 
# Oui : "afficher" n'est pas "renvoyer".  
# 
# Différencier fonction et procédure aide à la compréhension de ce qu'est exactement le sous-programme en question.

# <div class="alert alert-block alert-info">
#     
# **Spécificité python** : il n'y a que des fonctions (pas de procédure).  
# 
# </div>
# 
# Donc par la suite, on utilisera surtout le terme _fonction_ mais on ne manquera pas d'indiquer lorsqu'une fonction python est une procédure au sens défini ci-dessus.

# ## Introduction avec des exemples

# ### Les fonctions numériques du collège-lycée.
# 
# #### Ecriture mathématique habituelle
# 
# Un exemple : la fonction affine $f(x) = 2x + 1$ 
# 
# - vous savez calculer (de tête) $f(0)$, $f(1)$, $f(-1)$, ... 
# - vous connaissez sa représentation graphique : une droite de pente 2 et d'ordonnée à l'origine 1.

# #### En python
# 
# On commence par _définir_ `f` et ses paramètres, ici une seul paramètre `x` de type `float`.
# La fonction `f` _retourne_ une valeur de type `float`.
# La partie indentée par rapport à `def` définit le traitement -- on reconnait le calcul de $f(x)$ -- et la valeur retournée par la fonction -- ici la valeur de la variable _locale à la fonction_ `res`.  

# In[1]:


def f(x : float) -> float:
    res = 2 * x + 1
    return res


# On utilise `f` : on _appelle_ `f` pour différentes valeurs de son paramètre `x`.  
# Ces valeurs sont appelées des _arguments_ de l'appel. 
# Il peuvent être des valeurs numériques, des variables, des expressions, des appels à des fonctions ... 
# Bref tout ce qui peut être _évalué_ (_ie._, calculé) et qui _le sera **avant**_ l'exécution de l'appel de la fonction.

# In[2]:


# 3 appels pour des valeurs numériques
a = f(0)
b = f(1)
c = f(-1)
d = f(3)

print(a, b, c, d)


# In[3]:


# 2 appels pour des variables
zero = 0
un = f(zero)
trois = f(un)

print(zero, un, trois)


# In[4]:


# 2 appels dans une expression 
combien = f(zero) + f(un) 

# 2 appels : 1 d'une expression et 1 dans un argument qui est une expression 
et_celui_la = f(zero + f(un)) 

print(combien, et_celui_la)


# In[5]:


# un joli tracé vaut mieux qu'un long discours
import matplotlib.pyplot as plt

x = [i for i in range(-5,5)] # une liste de 10 arguments
y = [f(i) for i in x] # la liste des 10 valeurs de la fonction correspondante

plt.plot(x, y)
plt.title("f(x)=2x+1")
#plt.close()


# #### Premiers commentaires et vocabulaire important
# 
# 1. 
#     - On a **défini** (`def`) la fonction $f$ une fois, au début. 
#     - Puis on l'a utilisée, i.e. **appelée**, plusieurs fois : 
#         - pour calculer des valeurs ponctuelles :
#             - de valeurs numériques,
#             - de l'évaluation d'expressions,
#             - de l'évaluation de (l'appel) de fonction,
#         - effectuer des tracés, ...
# 2. 
#     - La définition a une forme très semblable à l'expression mathématique avec un  (ou des) **paramètre**  ou aussi **paramètre _formel_** $x$, et **des parenthèses** : f(x). 
#     - Elle contient (au moins) un `return` qui correspond à un résultat fourni par la fonction. 
#     - On dit ainsi que ce résultat est **retourné** par la fonction.   
# 3.
#     - Les appels, comme en math, correspondent à "remplacer" `x` par une valeur numérique donnée
#     - cette valeur d'appel est appelée **argument** ou aussi **paramètre _effectif_** (de l'appel).    
# 4. 
#     - **Important.** 
#         - Les **seuls** `print` de ces exemples s'appliquent à des _valeurs retournées_ par la fonction f
#         - **Aucun `print` dans la définition de f**.

# ### Les fonctions mathématiques prédéfinies
# 
# Les fonctions mathématiques connues comme les fonctions trigonométriques, logarithmes, exponentielles, puissances ... sont "fournies avec le langage de programmation" mais sous la forme de _bibliothèques_ de fonctions aussi appelées _modules_ en python.  
#   
# #### Appel : utilisation de fonction prédéfinie existante

# In[6]:


from math import cos, pi
# pour utiliser la fonction cos et la valeur pi définis dans le module math

c = cos(pi/3)
# calcul qui utilise cos et pi, puis affectation du résultat dans la variable c

print(c)
# affichage de la valeur de la variable c


# #### Vocabulaire (suite)
# 
# Cet exemple contient uniquement des _appels de fonction_ ; aucune définition des fonctions utilisées.
# 
# L'appel est caractérisé par :
# 
# * le **nom** de la fonction :  ici `cos(...)`
# * ses **arguments d'entrée** : ici la valeur $\pi$/3
# * une valeur de **retour** (résultat, destination) : 
#     - ici une variable résultat : `c`, 
#     - ou aussi un terme d'une expression : `cos(pi/3)**2 + sin(pi/3)**2`
# * vocabulaire : _argument_ ou _paramètre effectif_
# 
# **Appeler une fonction :** 
# 
# * ici, on _utilise_ le nom `cos` de la fonction trigonométrique _cosinus_ pour obtenir la valeur de cette fonction pour l'argument d'entrée fourni.    
# * on voit bien que cet appel ne nécessite pas de connaitre _comment_ cette fonction calcule le résultat qu'elle renvoie (ou retourne).  Cette fonction est bien vue comme une boîte opaque (une _boîte noire_).
# 
# Cet exemple permet d'introduire deux notions complémentaires (et différentes) :
# 
# * **la spécification**  = ce que ça fait : OK = le QUOI 
# * **une implémentation** = comment ça le fait : ? = le COMMENT  

# **Commentaires**  
# 
# * Ligne 1 : fonction `cos` et valeur `pi` sont disponibles   
# 
# * Ligne 2 : _à droite_ de l'affectation (=) : _appel_ de la fonction `cos(...)` pour l'_argument_ `pi/3`.  
# 
# * Ligne 2 : _à gauche_ de l'affectation  : valeur-résultat affectée dans la variable `c`
# 
# * Ligne 3 : affichage de la valeur _retournée_  
# 
# 
# <div class="alert alert-block alert-info">
#     
# **A retenir** : Les **parenthèses (...)** : c'est à ça qu'on reconnait une fonction !  
# 
# </div>
# 
# 
# <div class="alert alert-block alert-info">
# 
# **A retenir** : la construction `from module import fonction1, fonction2` permet d'utiliser les `fonctions` (1, 2, ...) définies dans la bibliothèque `module`
# 
# </div>

# **Digression** pour les curieuses et les curieux : précision numérique ? 
# 
# On se rassure :

# In[7]:


cos(pi)


# In[8]:


from math import *
# on importe "tout" math

c = cos(pi/3.0)
s = sin(pi/3)

un = c*c + s*s

print("cos, sin, cos*cos + sin*sin = ", c, s, un)


# ### Distinguer le _Quoi_ du _Comment_ 
# 
# Nous savons _ce que calculent_ ces fonctions : le **quoi**.
# Et pourtant la plupart d'entre nous ne savent pas **comment** elles sont calculées. 
# 
# Dans l'exemple de la fonction affine, l'expression $f(x) = 2x + 1$ mélange le _quoi_ et le _comment_.  
# 

# **Question** : Quelles sont les 4 notions définies par le paragraphe précédent ?
# 
# **Question** : Y-a-t'il d'autres façon de calculer la fonction $f$ précédente ? Qu'en déduire ?
# 

# ### Pourquoi des sous-programmes ? (des fonctions ?)
# 
# * Eviter de ré-écrire, de dupliquer, du code --- souvent le code qui correspond au _comment_ du traitement.      
# * Simplifier la lecture donc la compréhension : le _quoi_ suffit pour celà. 
# * Ré-utiliser l'existant
# 
# Les fonctions sont une nouvelle _structure_ en programmation et en algorithmique. 
# Une fonction permet d'écrire les algorithmes/codes de façon plus _modulaire_.
# * _Modularité_ : découper un traitement compliqué en une suite d'étapes plus simples
# * Ce découpage peut être appliqué _récursivement_ : _cad_ appliqué au sein de chaque étape, et ce de façon répétée, jusqu'à que le traitement de l'étape soit assez simple pour être écrit !

# ## Les grands principes : définition, signature, corps et appels de fonction  
# 
# 
# <div class='alert alert-block alert-danger'>
#     
# NE PAS CONFONDRE :  **LA** définition  vs. **LES** appels    
# 
# </div>
# 
# <div class="alert alert-success">
# 
# La définition d'une fonction est constituée de sa _signature_ et de son _corps_.
# 
# </div>
# 
# <div class="alert alert-success">
# 
# La signature "ne fait rien". Elle _décrit_ les paramètres formels_, cad. comment utiliser la fonction (par l'appel) et ce qu'elle fait.
# 
# </div>
# 
# <div class="alert alert-success">
# 
# Le corps est _le traitement qui sera exécuté par l'appel_ de la fonction.
# 
# </div>
# 
# <div class="alert alert-success">
# 
# L'appel définit les _arguments_ (ou _paramètres effectifs_) et _réalise le traitement_ (l'exécution) du corps de la fonction pour ces arguments .
# 
# </div>

# ### Définition d'une fonction
# 
# De façon générale, la définition d'une fonction contient :
# 
# * le _nom_ de la fonction
# * les **paramètres formels** des _entrées_ : leurs nombres, leurs types, l'identificateur de chacun  
# * les _sorties_ : leurs nombres, leurs types, l'identificateur de chacune    
# * le _traitement_ défini avec ces paramètres formels (d'entrée et de sortie) et, souvent, des _variables locales_ (à la fonction)
# 
# signature _vs._ corps pour distinguer le _quoi_ du _comment_ :
# 
# - Le traitement correspond au _comment_. Il est défini dans le _corps_ (ou l'implémentation) de la fonction  
# - Le _quoi_ est décrit par la signature de la fonction
# 

# #### Syntaxe(s) python de la définition de fonction
# 
# 
# <div class='alert alert-block alert-info'>
# 
# RETENIR : Le mot clé `def`, les `()` et le `:`
#     
# </div>    
# 
# Syntaxe Python simple :   
# ```python
# def nom(liste de paramètres formels séparés par des virgules):
#     ... # le corps de la fonction : ce qu'elle fait 
#     return 'sortie'
# ```

# Soyons plus précis en explicitant le _type_ des arguments d'entrée et de sortie.
# 
# https://fr.wikiversity.org/wiki/Python/Les_types_de_base
# 

# Syntaxe Python **améliorée** et **A UTILISER SYSTEMATIQUEMENT** :   
# ```python
# def nom('1er paramètre formel': son type, '2ème paramètre formel': son type, ...) -> type du retour:
#     ... # le corps de la fonction : ce qu'elle fait 
#     return 'sortie'
# ```

# Exemples de définition complète (signature et corps) : 

# In[9]:


def f(x : float) -> float:
    '''Une fonction affine déjà rencontrée'''
    y = 2 * x + 1
    return y

def qui_suis_je(n : int) -> int:
    '''?'''
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


# ### La signature d'une fonction
# 
# La _signature_ d'une fonction permet de connaître le minimum nécessaire et suffisant pour utiliser (appeler) cette fonction, ie. le _quoi_ (que fait la fonction et de quoi a-t-elle besoin pour ça ?)
# 
# On ne garde que le nécessaire de la syntaxe améliorée :

# In[10]:


def f(x : float) -> float:
    '''Fonction affine de coeff directeur 2 et d'ordonnée à l'origine 1'''

def qui_suis_je(n : int) -> int:
    '''Calcule et retourne la factorielle de l'entier positif n''' 


# <div class='alert alert-block alert-warning'>
# 
# Vocabulaire -- selon les langages de programmation : 
# <ul>
#     <li> signature = spécification = en-tête = prototype  </li>
#     <li> corps = implémentation  </li>
# </ul>
#     
# </div>    

# <div class='alert alert-block alert-danger'>
# 
# ATTENTION  : une telle signature n'est pas reconnue telle quelle par python
#   
# EN PRATIQUE : il faudra compléter la signature par le corps pour que la fonction soit correctement définie et reconnue (à suivre) 
# 
# </div>

# **$\star$ Rmq : statique _vs._ dynamique.** 
# Selon les langages de programmation, la signature peut-être séparée et compilée indépendamment de l'implémentation de la fonction. Ainsi (re)connue du compilateur, cette signature peut lui servir pour _vérifier automatiquement la correction_ de l'implémentation de la fonction et aussi des appels à cette fonction : nombre de paramètres effectifs, type de ces paramètres, type du résultat retourné, ... Ces vérifications sont possibles lors de la _compilation_ , cad. avant toute exécution du programme. Ce type de vérification diminue le risque d'erreur lors de l'exécution. 
# 
# On parle d'analyse _statique_ (ou de vérification statique) pour ces _traitements effectués lors de la compilation_. Oui : un compilateur est un programme qui s'exécute ! Il "prend en entrée" un code (dit) source et produit en sortie un code (dit) exécutable. Ce traitement comporte plusieurs étapes dont celle de vérification mentionnée qui s'effectue lors de l'étape (dite) d'analyse syntaxique -- ne pas confondre les termes "syntaxique" et "statique".
# 
# De façon complémentaire, on parle d'analyse _dynamique_ (ou de vérification dynamique) pour les traitements effectués lors de l'exécution du programme.
# 

# ### L'appel d'une fonction
# 
# L'appel de la fonction consiste à exécuter la fonction pour des valeurs fixées des arguments d'entrée.  
# 
# Syntaxiquement : 
# * le _nom_ de la fonction (sans le `def` mais avec les `( )`)
# * les **paramètres effectifs** : les _valeurs_ des arguments d'entrée
# * les _identifiants_ des variables de sortie

# In[11]:


# appel de f pour la valeur 0
ordonnee_a_l_origine =  f(0) 
 
print(ordonnee_a_l_origine)  


# In[12]:


t = 1
r = f(t)
print(r)


# In[13]:


print("n, f(n), n!")
# plusieurs appels de f et de qui_suis_je
for  val in range(3):
    print(val, f(val), qui_suis_je(val))


# On a vu en début de présentation que les paramètres effectifs peuvent être plus généralement la valeur d'une variable, d'une expression (évaluée), d'une fonction (appelée).    

# ####  Effet d'un appel sur le séquencement des instructions exécutées  
# 
# Distinguer _appelant_ et _appelé_ :
# 
# - Le cadre (la zone logique de code) où l'appel est effectué est appelé _l'appelant_.  
# - La définition de la fonction est (le cadre de) _l'appelé_.  
# 
# **L'appel provoque une rupture de l'exécution séquentielle de l'appelant** : un débranchement de l'appelant vers l'appelé.
# 
# - L'appel "passe la main" à l'appelé en même temps qu'il transmet les paramètres effectifs et une information pour que l'appelé puisse, plus tard, revenir dans l'appelant (fournir le résultat, ie. retourner le résultat).  
# - L'exécution revient dans la zone de l'appelant une fois achevée l'exécution de l'appelé  -- en pratique, après l'exécution d'un `return`.
# - Ce `return` déclanche le retour dans l'appelant à l'instruction de l'appel -- car c'est souvent une affectation si l'appelé est une (vraie) fonction -- ou à l'instruction suivante -- si c'est une procédure qui ne renvoie aucun résultat, cad. un appel sans affectation. 

# <div class='alert alert-block alert-warning'>
# 
# NE PAS CONFONDRE :  **paramètre formel** _vs._ **paramètre effectif** (ou argument)
# 
# </div>    
# 
# <div class='alert alert-block alert-danger'>
#     
# CONSIGNE PEDAGOGIQUE : il est interdit d'utiliser l'identifiant de du paramètre formel comme paramètre effectif d'un appel.     
# </div>

# In[14]:


x = 3
# L'appel suivant est interdit pour la fonction affine f(x) définie précédemment
y = f(x)

y = f(3) # ok


val = 3
y = f(val) # ok


# <div class="alert alert-block alert-info">
# 
# **A retenir :** l'appel est situé _après_ la définition  
# 
# </div>  
# 
# - logique : il faut connaitre la fonction pour l'utiliser ! 
# - `python` : se souvenir que `from module import f` permet de connaitre, donc d'utiliser, `f` qui a été définie (par moi ou par une autre) dans la bibliothèque `module`
#    
#     

# ### Le corps et le retour de valeur
# 
# Le corps définit le traitement de la fonction.  
# Il complète la signature.
# Ce traitement manipule les paramètres formels et des variables locales (à la fonction).  
# A l'issue du traitement, la fonction renvoie (ou retourne) une valeur de sortie.
# 
# * Python : le corps est _indenté_ d'un niveau par rapport à celui du `def` (qui finit par un `:`).

# #### `return` 
# 
# * Python : mot-clé `return`
#  * `return` une valeur, une variable, une expression
#  * `return None` : ne retourne rien ... mais le dit !  
#      * spécificité python : comme il n'y a que des fonctions en python, une procédure sera écrite comme une fonction qui retourne `None` 
# 
# * **Termine l'_exécution_ du corps de la fonction**
#  * à la fin de l'écriture du corps, en général ...
#  * mais pas toujours : le `return` n'est pas nécessairement unique (cf. paragraphe suivant)  

# In[15]:


# définition de 3 fonctions
def doubler(u : int) -> int:
    """ retourne le double de u """
    return 2 * u

def tripler(u : int) -> int:
    """ retourne le triple de u    """
    v = 3 * u
    return v

# des appels

d = doubler(2)
t = tripler(2)

print(d, t)


# In[16]:


# un appel -- qui passe en python mais qui "gratte un peu" d'après l'en-tête de doubler ...
doubler(5.5)


# #### `return` = terminaison de la fonction  
# 
# L'exécution d'un `return`, quel qu'il soit, _termine l'exécution de la fonction_ et provoque le retour dans le cadre appelant.
# 
# Plusieurs instructions `return` sont possibles dans une même fonction. 
# Donc pas uniquement comme dernière instruction du corps de la fonction. 
# Le premier `return` exécuté arrête l'exécution : les instructions suivantes du corps de la fonction ne sont pas traitées -- comme dans une branche conditionnelle non prise, _eg._ dans une structure `if: ... elif: ... else: ...`. 
# 
# Nous verrons que les fonctions récursives sont friandes de `return` très tôt écrit dans le corps. 

# In[17]:


def a(u : float) -> float:
    '''calcule la valeur absolue de u'''
    if u > 0:
        res = u
    else:
        res = -u
    return res


# **Rmq**.
# Nous expliquerons bientôt que `res` est une _variable locale_ à la fonction qui est définie pour retourner le résultat du traitement de la fonction. 

# In[18]:


def aa(u : float) -> float:
    '''La même avec 2 return '''
    if u > 0:
        res = u
        return res
    else:
        res = -u
        return res
    
def aaa(u : float) -> float:
    '''La même avec 2 return sans variable locale'''
    if u > 0:
        return u
    else:
        return -u


# In[19]:


# 2 appels
a_x = a(2)
a_y = a(-5)

# affichage
print(a_x, a_y)
#print(a(3))

# intérêt du doc-string
help(a)
help(aa)


# ### Exercice
# 
# * Reprendre les fonctions `a`, `aa` et `aaa` précédentes et identifier leurs signatures, leurs paramètres formels, leurs types, les corps de ces fonctions. Et dans les appels les `return` exécutés, le séquencement des instructions exécutées dans l'appelant et l'appelé.  

# ## Appel : appelant -> appelé ; return : appelé -> appelant 
# 
# Nous illustrons avec [pythontutor](http://pythontutor.com/visualize.html#mode=edit) l'exécution d'un appel de fonction. 
# 
# Cad. :
# 
# - l'appel de fonction provoque une rupture de l'exécution séquentielle, un débranchement de l'appelant vers l'appelé ;
# - le `return` provoque le retour au cadre appelant pour continuer l'exécution séquentielle.
# - Plusieurs `return` ? Oui mais 1 seul exécuté par appel.

# - Fonction affine :
# [visualisation pythontutor](http://pythontutor.com/visualize.html#code=def%20f%28x%20%3A%20float%29%20-%3E%20float%3A%0A%20%20%20%20'''Une%20fonction%20affine%20d%C3%A9j%C3%A0%20rencontr%C3%A9e'''%0A%20%20%20%20y%20%3D%202%20*%20x%20%2B%201%0A%20%20%20%20return%20y%0A%20%20%20%20%0Aordonnee_a_l_origine%20%3D%20f%280%29%0A%0Aprint%28ordonnee_a_l_origine%29%0A%0Aprint%28%22n,%20f%28n%29%22%29%0A%23%20plusieurs%20appels%20de%20f%0Afor%20val%20in%20range%283%29%3A%0A%20%20%20%20print%28val,%20f%28val%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# 

# - Plusieurs return, 1 seul exécuté par appel :
# [visualisation pythontutor](http://pythontutor.com/visualize.html#code=def%20aa%28u%20%3A%20float%29%20-%3E%20float%3A%0A%20%20%20%20'''La%20m%C3%AAme%20avec%202%20return%20'''%0A%20%20%20%20if%20u%20%3E%200%3A%0A%20%20%20%20%20%20%20%20res1%20%3D%20u%0A%20%20%20%20%20%20%20%20return%20res1%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20res2%20%3D%20-u%0A%20%20%20%20%20%20%20%20return%20res2%0A%20%20%20%20%20%20%20%20%0Aun%20%3D%20aa%281.0%29%0Aencore_un%20%3D%20aa%28-1.0%29%0A%0A%23%20Profitons-en%20pour%20montrer%20un%20%60assert%60%20%0Aassert%20un%20%3D%3D%20encore_un&cumulative=false&curInstr=14&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# 

# ### Exercice
# 
# * Reprendre les fonctions `a`, `aa` et `aaa` précédentes et bien identifier le séquencement des instructions exécutées dans l'appelant et l'appelé.  

# ## Variable locale _vs._ variable globale, portée des variables
# 
# Les notions de variable locale (à une fonction) ou de variable globale sont classiques en programmation.  
# 
# > **Variable locale** à une fonction : variable définie dans le _corps_ de la fonction pour permettre le traitement réalisé par la fonction.  
# 
# Par extension, les **paramètres formels de la fonction sont aussi des variables locales**.  

# > Une **variable** est dite  **globale** par rapport à une fonction si elle est définie à l'extérieur de la fonction, et plus particulièrement dans l'appelant de la fonction.  
# 
# Il faut donc introduire la notion de portée d'une variable.  

# > **Portée** : zone où une variable est _accessible_, ou autrement dit : zone où une variable est (re)connue à l'aide de son identifiant.  
# 
# **La portée d'une variable locale est** ... locale, cad. **limitée au corps de la fonction** qui contient sa définition.  
# Une variable locale _n'existe pas à l'extérieur_ de la définition ou du traitement de la fonction.  

# **Exemple.**
# 
# - Reprendre le pythontutor précédent et observer comment `res1` ou `res2` naissent, vivent et meurent.

# Une variable globale est définie dans le cadre _appelant_.  
# Une fois définie, sa portée est globale à ce cadre : cette variable est accessible sur l'ensemble de la zone qui contient sa définition et à partir de cette dernière. 
# 
# Ainsi :
# - la portée d'une variable globale inclut les fonctions, (et leurs corps) définies dans cette zone  
# - les portées d'une variable globale et d'une variable locale (à une fonction) se recouvrent (dans cette fonction); 
# - ce qui nécessitera de clarifier la situation dans le cas où _ces 2 variables ont le même identifiant_.
# 
# Ces trois dernières remarques justifient à l'interdit (à vocation pédagogique) suivant. 

# <div class="alert alert-block alert-danger">
#     
# CONTRAINTE PEDAGOGIQUE :  Dans la définition d'une fonction, il est interdit d'introduire ou d'utiliser des variables globales, excepté si ce sont des **constantes**.
#        
# </div>
# 
# Ainsi, vous ne devez limiter le corps de fonction au traitement de ses paramètres formels et de variables locales.
# 
# <div class="alert alert-block alert-info">
# 
# CONVENTION PYTHON : les identifiants de constantes s'écrivent en MAJUSCULES   
#     
# `ANNEE_EN_COURS = 2020`
# 
# </div>

# Au delà de certaines spécificités de python qui la rendent assez délicate, l'utilisation de variables globale  est à l'origine de la notion _d'effet de bord_ souvent à l'origine de longues phases de debugging. Nous reviendrons sur cet aspect au chapitre suivant.
# 
# Le besoin d'utiliser des variables globales dans des fonctions internes peut être satisfait en ajoutant ces variables comme paramètres de ces fonctions.  
# 

# ### Exercice
# 
# * Reprendre les fonctions `a`, `aa` et `aaa` précédentes et identifier leurs variables locales et leur portée, dans la définition, dans les appels, dans les appelants.   

# ## Compléments

# ### Erreur fréquente
# 
# <div class="alert alert-danger">
# 
# NE PAS CONFONDRE :  `return` _vs._ `print`
# 
# </div>
# 
# <div class="alert alert-info">
# 
# CONSEIL DÉJÀ SOUVENT RAPPELÉ : séparer les E/S des traitements
# 
# </div>
# 
# En pratique, les E/S (`print` et `input`) doivent être limitées :
# - aux programme principal (le `main`) 
# - aux sous-programmes d'entrées-sorties spécifiques à votre application, si il y en a.  
#     - Voir `afficher_pref_dpt()` en fin de chapitre.

# ### Méthodologie d'écriture des fonctions  
# 
# En pratique, vous introduirez des fonctions en respectant **l'ordre d'écriture** suivant :
# 
# 1. écriture de la signature de la fonction  
# 2. écriture d'appels simples : notion de _test unitaire_
#     - appels simples = appels sur des valeurs de tests, cad. dont on connait le résultat attendu de la fonction  
# 3. écriture du corps
# 4. exécution des test unitaires (et correction de l'étape précédente si besoin) 
# 5. écriture des appels voulus  
# 6. exécution des appels voulus
# 
# 
# <div class='alert alert-block alert-danger'>
# 
# CONSIGNE PEDAGOGIQUE : L'écriture de l'appel (simple) est effectuée avant celle du corps, _ie._ en se basant uniquement sur la signature.
# </div>
# 
# Ainsi, il n'est pas possible d'exécuter cet appel avant d'avoir fini l'étape suivante (écriture du corps).

# ### De l'intérêt de distinguer _fonction_ et _procédure_
# 
# <div class="alert alert-block alert-warning">
# 
# CONSEIL : Distinguer les fonctions des procédures oblige à se poser la question du besoin de modifier ou non les arguments du sous-programme.  
# 
# </div>
# 
# Une **fonction** :
# - calcule et retourne un résultat
# - à partir de la __valeur__ de ses paramètres effectifs.  
# - Ce résultat est connu de l'appelant par une affectation (au retour de l'appel).  
# - L'appel de la fonction ne modifie pas les paramètres effectifs. 
# 
# Une **procédure** :
# - effectue une action ou des traitements (dont des lectures et des écritures)
# - avec ses paramètres effectifs
# - et ne retourne pas de résultat.
# - L'appel d'une procédure peut modifier ses paramètres effectifs.
# 
# **Rmq.**
# Ainsi l'appel d'une procédure ne nécessite pas d'affectation dans l'appelant.
# 
# > A la différence d'autres langages, python n'introduit qu'un type de sous-programme : la fonction.  
# > Rappellons qu'une fonction python retourne _toujours_ une valeur, même si cette dernière est `None`.  
# 
# **Exercice.**  Donner un exemple de fonction python (utilisée depuis le début de l'année) qui est en fait une procédure.

# ### `help()` et _docstring_
# 
# `help()` est une fonction python prédéfinie qui affiche l'en-tête (la signature) complet de la fonction passée en paramètre.  
# 
# Elle fournit les informations nécessaires à l'utilisation correcte de la fonction, ainsi que des détails sur son objet et son implémentation -- si le ces aspects ont été décrits par le programmeur dans le `docstring` : la zone de commentaires entre ` ``` ``` ` et indentée sous le `def`.
# 
# Cette fonction est similaire à l'option de commande `--help` sous Unix.

# In[20]:


help(doubler)


# In[21]:


help(f)


# **Exercice**. A quoi reconnait-on que `help` est une fonction ?

# ### Plusieurs paramètres

# In[22]:


def puissance(x : float, n : int) -> float:
    '''calcule x**n de façon itérative pour'''
    # (un) corps de la fonction puissance
    r = 1.0
    for i in range(1, n+1):
        r = r * x
    return r

# appels avec des valeurs  
mille = puissance(10.0, 3)
print("mille =", mille)

vrai_ou_faux = (puissance(3.1,2) == 3.1 * 3.1)
print(vrai_ou_faux)


# In[23]:


# appels avec une variable
n = int(input("n premières puissances de 2.0 pour n = "))
for i in range(n+1):
    print("2 **", i, "=", puissance(2, i))

print("cas particulier")
print(puissance(2.0, 0))

# appels avec des variables
p = float(input("n premières puissances de p pour p = "))
n = int(input("et n = "))

for i in range(n+1):
    print(puissance(p,i))


# ### Plusieurs `return` (rappel)  
# 
# 1. Une fonction qui calcule et renvoie (retourne) la valeur absolue d'un entier
#     * Vue plus haut
# 2. Une fonction `puissance` qui calcule et renvoie $x^n$ pour $n>0$ et $x$ entier
#     * $x^n = x \times x \times x \times x \times \dots \times x$ avec $n-1$ multiplications
#     * $x^0 = 1$ pour $x \neq 0$
#     * pas la peine de perdre trop de temps pour calculer $0^n = 0$ 
#     * faire attention si $n < 0$ : ne rien calculer pour l'instant   
# 
# 

# In[24]:


def puissance2(x : float, n : int) -> float:
    '''calcule x**n de façon itérative : autre version'''
    if x == 0.0:
        return 0.0
    if n == 0:
        return 1
    else:
        r = x
        for i in range(2, n+1):
            print('on est dans la boucle')
            r = r * x
        return r


# appels avec des valeurs 
xx = 10.0
for n in range(0,4):
    val = puissance2(xx, n)
    print(xx, "**", n, "=", val)

#vrai_ou_faux = (puissance(3.1,2) == 3.1 * 3.1)
#print(vrai_ou_faux)


# **Exercice**
# 
# - Simplifier la branche `else` de `puissance2()`.

# ### Fonction sans paramètre 
# 
# Une fonction peut ne pas avoir de paramètre formel. Et donc être appelée sans argument (sans paramètre effectif).

# In[25]:


def tetu() :
    return 1

res = tetu() # appel et affectation du résultat
print('res = ', res)   # affichage

# boucle d'appels à tetu() dans un print()  
for i in range(5):
    print('appel tetu', tetu())
        
# appel sans affectation, ni print. 
# L'interpréteur python affiche sa valeur en Out[..] 
#doubler(1)

tetu()


# ### Fonction locale
# 
# A la manière d'une variable locale, une _fonction locale_ (à une fonction) est :
# 
# - définie dans le corps d'une fonction,
# - puis utilisable par cette fonction (englobante)
# - mais _uniquement par elle_ : elle est inconnue de l'extérieur de la fonction englobante,
# - et ce récursivement.
# 

# In[26]:


def max3(x : int, y : int, z : int) -> int:
    '''
    autre version (1 return) sans fonction locale
    role : calcule et retourne le max de 3 valeurs
    '''
    if x < y:
        if y < z:
            res = z
        else:
            res = y
    else:
        if x < z:
            res = z
        else:
            res = x
    return res


# test exhaustif pour 3 valeurs différentes    
print(max3(1, 4, 2), max3(1, 2, 4), max3(2, 1, 4), max3(2, 4, 1), max3(4, 1, 2), max3(4, 2, 1))


# In[27]:


def max3_f_loc(x : int, y : int, z : int) -> int:
    '''
    role : calcule et retourne le max de 3 valeurs
    avec fonction locale
    '''
    def max2(u, v : int) -> int:
        '''
        fontion locale : 
        calcule et retourne le max de 2 valeurs'''
        if u > v:
            res = u
        else: 
            res = v
        return res
    
    if x < y:
        res = max2(y, z)
    else:
        res = max2(x, z)    
    return res


# In[28]:


m1 = max3(1, 4, 2)
m2 = max3_f_loc(1, 4, 2)

print(m1 == m2)


# ### Exercice
# 
# - Compléter le test unitaire de `max3`.
# - ($\star$) Ecrire une version de `max3` sans variable locale, ni fonction locale.    
# - ($\star$) Ecrire une version de `max3` avec une fonction locale et réduite à _une seule ligne d'instruction_ (pour le traitement de `max3`). 

# **Solution**

# In[29]:


def max3_v2(x : int, y : int, z : int) -> int:
    '''
    role : calcule et retourne le max de 3 valeurs
    version 4 return : sans variable, ni fonction locale 
    '''
    if x < y:
        if y < z:
            return z
        else:
            return y
    if x < z:
        return z
    else:
        return x
    


# In[30]:


def max3_fonctionnelle(x : int, y : int, z : int) -> int:
    '''
    role : calcule et retourne le max de 3 valeurs
    '''
    def max2(u, v : int) -> int:
        '''
        fonction locale : 
        calcule et retourne le max de 2 valeurs'''
        if u > v:
            res = u
        else: 
            res = v
        return res
    
    return max2(x, max2(y, z))

m = max3_fonctionnelle(1, 4, 2)
print(m)


# ## Synthèse
# 
# ### Retenir 
# 
# - __Modularité__ : fonction pour factoriser le traitement, structurer le déroulement d'un algo, faciliter la compréhension du traitement et la maintenance des codes
#     - Tests unitaires de fonction, `assert`  
# - Une fonction se reconnait à :
#     - `def` dans sa définition,
#     - ses parenthèses dans les appels.  
# - Sa _définition_ 
#     - commence par `def`, suivi de près par un `:`, et contient au moins un `return`;
#     - contient entre les parenthèses qui suivent son nom :
#         - la définition des paramètres formels, 
#         - et leur type : annotations `:` et `->`;
#     - contient une _documentation_ entre ` ''' ` qui détaille son rôle (`docstring`). 
# - La _signature_ (ou l'_en-tête_) de la fonction est l'ensemble de ces éléments, `return` excepté.  
#     - `help(nom_de_la_fonction)` affiche la signature de la fonction, cad sa définition, paramètres compris et le `docstring`. 
# - Le _corps_ d'une fonction est la zone indentée par rapport au `def` qui contient le traitement effectué par la fonction, et au moins un `return`.   

# Se souvenir que :
# 
# - l'appel à une fonction génère un _débranchement_ de la séquence d'instructions de l'_appelant_ pour exécuter les instructions de _l'appelé_
# - que le premier `return` exécuté dans l'appelé permet de _revenir_ à l'appelant pour continuer à exécuter la séquence d'instructions qui suit l'appel (dans l'appelant) -- souvent une affectation du résultat de l'appel. 

# ### Ne pas confondre 
# 
# > * __définition__ _vs._ __appel__  
# > * __signature__ _vs._ __corps__  
# > * paramètre __formel__ _vs._ argument ou paramètre __effectif__  
# > * appelé _vs._ appelant  
# > * __return__ _vs._ __print__  

# ### A venir
# 
# Un point important a été passé sous silence dans ce chapitre : 
# - comment s'effectue le passage de paramètres lors de l'appel ?  
# 
# Autrement dit : 
# - comment les paramètres formels de la définition d'une fonction "deviennent" des paramètres effectifs, cad. des valeurs effectivement traités (ou des objets effectivement manipulés) par les instructions du corps de la fonction ? 
# 
# Cette importante question sera traitée dans le chapitre suivant car les réponses diffèrent selon les langages de programmation -- car plus techniques qu'algorithmiques.    

# ## Exercices en démonstration

# ### Lister les notions vues jusqu'ici
# 
# - définition, paramètres formels, sortie  
# - appel, paramètres effectifs  
# - spécification (ce que ça fait) vs. implémentation (comment ça le fait)  
# - `def`, `()`, `return`,  
# - variables locales  
# - fonction, procédure  

# ### Différentes écritures de fonctions min
# 
# - Ecrire la fonction min(a,b) : signature, appels, puis corps ; test unitaires.
# - Proposer plusieurs écritures du corps : avec un seul return, avec deux, ...
# - S'en servir pour écrire la fonction min(x, y, z) : signature, appels, puis corps
# - Proposer plusieurs écritures du corps

# In[31]:


def min(a : int, b : int) -> int:
    '''retourne min(a,b)
    -> version un seul return
    '''
    if a < b:
        m = a
    else:
        m = b
    return m


# In[32]:


def min2(a : int, b : int) -> int:
    '''retourne min(a,b)
    -> version deux return
    '''
    if a < b:
        return a
    else:
        return b


# In[33]:


def min3a(a : int, b : int, c : int) -> int:
    '''retourne min(a,b,c)
    -> version 1 return, 2 appels à min(a,b)
    '''
    if min(a, b) < c:
        m = min(a, b)
    else:
        m = c
    return m


# In[34]:


def min3b(a : int, b : int, c : int) -> int :
    '''retourne min(a,b,c)
    -> version 1 return, 1 appel à min(a,b)
    '''
    m_ab = min(a, b)
    if m_ab < c:
        m = m_ab
    else:
        m = c
    return m


# In[35]:


def min3(a : int, b : int, c : int) -> int:
    '''retourne min(a,b,c)
    -> version fonctionnelle : 2 appels imbriqués 
    '''
    return min(min(a, b), c)


# In[36]:


# des appels
x = 23
y = 44
z = 27
m_xyz = min3a(x, y, z)
print(m_xyz)
m_xyz = min3b(x, y, z)
print(m_xyz)
m_xyz = min3(x, y, z)
print(m_xyz)


# ### Une procédure d'affichage (E/S) 
# 
# Ecrire une fonction qui réalise efficacement l'affichage suivant :
# 
# ```
# Carcassonne est la préfecture du département 11
# ------------------------------------------------
# Perpignan est la préfecture du département 66
# ------------------------------------------------
# Montpellier est la préfecture du département 34
# ------------------------------------------------
# Foix est la préfecture du département 09
# ------------------------------------------------  
# ```

# In[37]:


# Bourrin et pas satisfaisant
print("Carcassonne est la préfecture du département 11")
print("------------------------------------------------")
print("Perpignan est la préfecture du département 66")
print("------------------------------------------------")
print("Montpellier est la préfecture du département 34")
print("------------------------------------------------")
print("Foix est la préfecture du département 09")
print("------------------------------------------------")

# On pourrait bien sûr mettre tout dans un seul print (avec des `\n`)
# ce qui n'est pas satisfaisant non plus ...


# In[38]:


# Synthétique mais un peu pythonesque : une boucle sur des "couples" (tuple) 
for v,d in ("Carca", "11"), ("Perpi","66"), ("Montpel", "34"), ("Foix", "09"):
    print(v, "est la préfecture du département", d)
    print("------------------------------------------------")


# - Le couple entre parenthèses `("Carca", "11")` est un **tuple** python, notion sur laquelle nous reviendrons très vite  
# - En attendant, considérer ce tuple comme une constante composée de 2 valeurs de type string

# In[39]:


# définition d'une fonction qui affiche ce qu'on veut comme on veut
def afficher_pref_dpt(ville : str, num_dpt : str):
    print(ville, "est la préfecture du département", num_dpt)
    print("------------------------------------------------")


 # 4 appels de cette fonction
afficher_pref_dpt("Carca", "11")
afficher_pref_dpt("Perpi", "66")
afficher_pref_dpt("Montpell", "34")
afficher_pref_dpt("Foix", "09")

print()

# 4 appels synthétiques de façon pythonesque  
for (v,d) in ("Carca", "11"), ("Perpi","66"), ("Montpell", "34"), ("Foix", "09"):
    afficher_pref_dpt(v,d)


# **Rmq.** 
# 
# - Pourquoi `afficher_pref_dept()` n'est pas une fonction excepté pour python ?
# 
html généré avec :

jupyter nbconvert --to html_embed --template toc2  1-fonctions.ipynb
slides générés avec :
    
jupyter nbconvert --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --SlidesExporter.reveal_theme=white  1-fonctions.ipynb
