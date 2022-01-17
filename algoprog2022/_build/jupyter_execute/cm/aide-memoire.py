#!/usr/bin/env python
# coding: utf-8

# # Sections et interactions ajoutées en séance
# 
# version 2021, PhL.

# <h1>Table des matières<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Sections-et-interactions-ajoutées-en-séance" data-toc-modified-id="Sections-et-interactions-ajoutées-en-séance-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Sections et interactions ajoutées en séance</a></span><ul class="toc-item"><li><span><a href="#Aide-mémoire" data-toc-modified-id="Aide-mémoire-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Aide-mémoire</a></span></li></ul></li><li><span><a href="#Examen-semestre-1-(2019)" data-toc-modified-id="Examen-semestre-1-(2019)-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Examen semestre 1 (2019)</a></span></li><li><span><a href="#Fonctions" data-toc-modified-id="Fonctions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Fonctions</a></span><ul class="toc-item"><li><span><a href="#Exercice-7" data-toc-modified-id="Exercice-7-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Exercice 7</a></span><ul class="toc-item"><li><span><a href="#Écrire-une-programme-qui" data-toc-modified-id="Écrire-une-programme-qui-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Écrire une programme qui</a></span></li></ul></li></ul></li></ul></div>

# ## Aide-mémoire

# <div class="alert alert-block alert-info">
#     
# Un <b>bloc</b> d'items reconnu par `nbconvert to html`:
#     
# <ul>
# <li> item1 </li>
# <li> item 2 </li>
# </ul>    
# 
# </div>

# # Examen semestre 1 (2019)

# In[1]:


def darts2(x, y):
    '''calcule le nb de points
    version avec plusieurs return
    entrées : x, y (float) : coordonnées flechette
    sortie : nb_points (int)'''
    # centre
    if x == 0 and y == 0:
        return 50
    
    # dans la cible
    rayon2 = x*x + y*y
    for r in range(1, 11):
        if rayon2 <= r*r:
            return 20 - r
    
    # hors de la cible    
    return 0

def darts(x, y):
    '''calcule le nb de points
    version avec 1 seul return
    entrées : x, y (float) : coordonnées flechette
    sortie : nb_points (int)'''
    
    if x == 0 and y == 0:
        nb_points = 50
    else:
        rayon2 = x*x + y*y
        if rayon2 > 10*10:
            nb_points = 0
        else:
            for r in range(10, 0, -1):
                if rayon2 <= r*r:
                    nb_points = 20 - r
        
    return nb_points

    
# Entrées
abs = float(input("abscisse flechette : "))
ord = float(input("ordonnée flechette : "))

# traitement
points = darts(abs, ord)

# Affichage
print("tu gagnes ", points, "points")


# # Fonctions

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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




