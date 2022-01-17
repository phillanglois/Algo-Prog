#!/usr/bin/env python
# coding: utf-8

# # Les entrées-sorties avec des fichiers
# 
# **Partie Programmation**    
# version 2021, v2. PhL.

# Chapitre où on étudie comment manipuler les fichiers pour effectuer des entrées-sorties (E/S).
# 
# Jusqu'à présent les entrées-sorties ont été générées à grands coups de `print()` et d'` input()` pour interagir avec l'écran ou le clavier.
# Les entrées-sorties ne sont pas limitées au couple écran-clavier.
# Bien au contraire, ces derniers ne sont que des cas particuliers d'une notion plus générale : celle de _fichier_.   
# 

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Les-entrées-sorties-avec-des-fichiers" data-toc-modified-id="Les-entrées-sorties-avec-des-fichiers-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Les entrées-sorties avec des fichiers</a></span><ul class="toc-item"><li><span><a href="#Les-fichiers" data-toc-modified-id="Les-fichiers-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Les fichiers</a></span><ul class="toc-item"><li><span><a href="#Programmer-avec-des-fichier-:-principes" data-toc-modified-id="Programmer-avec-des-fichier-:-principes-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Programmer avec des fichier : principes</a></span></li></ul></li><li><span><a href="#Allons-y-en-python-!" data-toc-modified-id="Allons-y-en-python-!-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Allons-y en python !</a></span><ul class="toc-item"><li><span><a href="#Les-fonctions-et-les-méthodes" data-toc-modified-id="Les-fonctions-et-les-méthodes-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Les fonctions et les méthodes</a></span></li><li><span><a href="#La-plus-simple-des-lectures-:-read()" data-toc-modified-id="La-plus-simple-des-lectures-:-read()-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>La plus simple des lectures : <code>read()</code></a></span></li><li><span><a href="#Une-autre-lecture-simple-:-readlines()" data-toc-modified-id="Une-autre-lecture-simple-:-readlines()-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Une autre lecture simple : <code>readlines()</code></a></span></li><li><span><a href="#Une-lecture-ligne-à-ligne-avec-readline()et-avec-conversion-de-type" data-toc-modified-id="Une-lecture-ligne-à-ligne-avec-readline()et-avec-conversion-de-type-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Une lecture ligne à ligne avec <code>readline()</code>et avec conversion de type</a></span></li><li><span><a href="#Une-lecture-et-une-écriture-(ou-deux)" data-toc-modified-id="Une-lecture-et-une-écriture-(ou-deux)-1.2.5"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>Une lecture et une écriture (ou deux)</a></span></li><li><span><a href="#La-syntaxe-classique-avec-with" data-toc-modified-id="La-syntaxe-classique-avec-with-1.2.6"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>La syntaxe classique avec <code>with</code></a></span></li><li><span><a href="#$(\star)$-Approfondissements" data-toc-modified-id="$(\star)$-Approfondissements-1.2.7"><span class="toc-item-num">1.2.7&nbsp;&nbsp;</span>$(\star)$ Approfondissements</a></span><ul class="toc-item"><li><span><a href="#Origine-des-problèmes-classiques" data-toc-modified-id="Origine-des-problèmes-classiques-1.2.7.1"><span class="toc-item-num">1.2.7.1&nbsp;&nbsp;</span>Origine des problèmes classiques</a></span></li><li><span><a href="#Bien-contrôler-ses-print()" data-toc-modified-id="Bien-contrôler-ses-print()-1.2.7.2"><span class="toc-item-num">1.2.7.2&nbsp;&nbsp;</span>Bien contrôler ses <code>print()</code></a></span></li><li><span><a href="#Retour-sur-le-.read()" data-toc-modified-id="Retour-sur-le-.read()-1.2.7.3"><span class="toc-item-num">1.2.7.3&nbsp;&nbsp;</span>Retour sur le <code>.read()</code></a></span></li><li><span><a href="#read()-vs.-readline()-(sans-s)" data-toc-modified-id="read()-vs.-readline()-(sans-s)-1.2.7.4"><span class="toc-item-num">1.2.7.4&nbsp;&nbsp;</span><code>read()</code> <em>vs.</em> <code>readline()</code> (sans s)</a></span></li></ul></li></ul></li><li><span><a href="#Pour-finir-en-pratique" data-toc-modified-id="Pour-finir-en-pratique-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Pour finir en pratique</a></span><ul class="toc-item"><li><span><a href="#Le-cas-simple-de-la-lecture-d'un-fichier-que-l'on-(a)-écrit" data-toc-modified-id="Le-cas-simple-de-la-lecture-d'un-fichier-que-l'on-(a)-écrit-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Le cas simple de la lecture d'un fichier que l'on (a) écrit</a></span></li><li><span><a href="#Une-simplification-&quot;pythonique&quot;" data-toc-modified-id="Une-simplification-&quot;pythonique&quot;-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Une simplification "pythonique"</a></span></li><li><span><a href="#Un-dernier-conseil" data-toc-modified-id="Un-dernier-conseil-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>Un dernier conseil</a></span></li></ul></li><li><span><a href="#Synthèse" data-toc-modified-id="Synthèse-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Synthèse</a></span><ul class="toc-item"><li><span><a href="#Avoir-les-idées-claires" data-toc-modified-id="Avoir-les-idées-claires-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Avoir les idées claires</a></span></li><li><span><a href="#Savoir-faire" data-toc-modified-id="Savoir-faire-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Savoir-faire</a></span></li><li><span><a href="#Ce-qu'il-restera-à-voir" data-toc-modified-id="Ce-qu'il-restera-à-voir-1.4.3"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Ce qu'il restera à voir</a></span></li></ul></li></ul></li></ul></div>

# ## Les fichiers
# 
# A la différence de la mémoire (vive) de l'ordinateur qui contient bien sûr l'information traitée, le fichier (_file_ en anglais) permet de conserver cette information sur des supports matériels (disques, clés, bandes magnétiques, ...) et de la retrouver même si l'alimentation électrique de l'ordinateur a été interrompue.
# Cette information peut être des données de tout type (nombres, sons, images,...), des programmes, des bibliothèques de composants du logiciel, ...
# 
# On distingue les _fichiers_ dits _texte_ (ou fichiers textuels) des _fichiers_ (dits)  _binaires._ 
# 
# - Les fichiers texte  contiennent de l'information exploitable par l'humain 
# - Les fichiers binaire contiennent de l'information uniquement exploitable par l'ordinateur : , ...
# 
# Bien sûr, ces deux types de fichiers sont au final une suite de bits 0 et de 1 stockés sur un support physique.   
# Dans ce chapitre, l'accent sera surtout mis sur les fichiers de texte utiles pour nos développements de taille modeste.

# ### Programmer avec des fichier : principes
# 
# La plupart des langages de programmation distinguent les fichiers (dits) logiques des fichiers (dits) physiques.
# 
# - Les __fichiers logiques__ sont des variables manipulées par le programme  
#     - Ce sont des variables d'un nouveau type : le type _fichier_
# - Les __fichiers physiques__ sont les supports effectifs du stockage de l'information (en mémoire, sur disque, sur clé, ...). 
#     - Ils sont identifiés par le "chemin" système de leur localisation (le _path_)(`/home/mon_user_id/work/le_fichier.txt`)   
#     - Ils ne sont manipulés qu'une seule fois : lors de l'association fichier logique $\to$ fichier physique

# __Utiliser un fichier__ (en lecture, écriture ou lecture-écriture) consiste en les 4 étapes suivantes.
# 1. __associer le fichier logique__ à __un fichier physique__
# 2. __ouvrir__ le fichier logique  
# 3. effectuer les __traitements__ désirés sur le fichier logique  
# 4. __fermer__ le fichier logique  
# 
# L'étape d'ouverture du fichier précise le __type des traitements__ qui seront effectués en distinguant :
# - la lecture : _read_
# - l'écriture : _write_
# - la lecture + l'écriture : _readwrite_  

# __Organisation :__ un fichier est décomposé en lignes et se termine par un symbole de fin de fichier : _EOF (end of file)_     
# Une ligne est une suite de caractères et se termine par un symbole de fin de ligne : _EOL (end of line)_  
# Les traitements correspondent à un _accès séquentiel_ du fichier, en commençant à ligne 1.   

# __Accès direct _vs._ accès séquentiel.__ 
# 
# On distingue :
# -  les fichiers qui permettent d'accéder _directement_ à une ligne (et l'enregistrement) quelconque de leur contenu,   
# - les fichiers qui nécessitent un parcours systématique et _séquentiel_ à partir de la dernière ligne accédée (et donc depuis le début du fichier lors de la première opération).
# 
# Ces différents comportements sont essentiellement dues à des aspects matériels.
# Historiquement, les fichiers stockés sur des bandes magnétiques (!) étaient à accès séquentiel.
# 
# La plupart des fichiers utilisables aujourd'hui sont à accès direct -- ce qui sera le cas dans ce qui suit.

# <div class="alert alert-info">
# 
# Objectif 10 : On se limite à des manipulations simples (lecture ou écriture) de fichier de texte.
#     
# </div>

# ## Allons-y en python !
# 
# Les fonctions de chacune des 4 étapes _association/ouverture/lectures-écritures/fermeture_ sont en python :
# 
# - 1 et 2 : `open(), `  
# - 3 :`.read()`, `.write()`, `.readlines()`,`.writelines()`, `.readline()`...  
# - 4 :`.close()` 

# ### Les fonctions et les méthodes
# * Ouverture et fermeture : `open()` et `close()`
# 
# * Lecture complète  
#     - `.read()`: lit tout le fichier et retourne un `str`  
#     - `.readlines()`: lit tout le fichier et retourne une `lst` de `str`  
#     
# * Lecture partielle  
#     - `.read(oct)`: lit `oct` octets dans le fichier et retourne un `str`
#     - `.readline()`: lit une ligne, caractère `\n` compris si il est présent, et retourne un `str`
# 
# * Ecriture.
#     - `.write()`: écrit une `str` ou une valeur dans le fichier 

# **Rmq.** Les fichiers _physiques_ doivent exister pour être ouverts, lus, modifiés, fermés.  

# In[1]:


get_ipython().system('ls -l ./tmp')
get_ipython().system('file ./tmp/fichier_entrees.txt')
get_ipython().system('cat ./tmp/fichier_entrees.txt')


# ### La plus simple des lectures : `read()`

# In[2]:


# on associe et on ouvre 
f = open("./tmp/fichier_entrees.txt", "r", encoding="utf8") 

# le contenu du fichier est lu et stocké dans une chaîne 
st_f = f.read()

# on regarde
print(st_f)
print(type(st_f))
print(type(f))

# on ferme
f.close()


# On aurait pu fermer le fichier juste après la lecture et travailler avec la chaîne de caractères qui contient le contenu du fichier. 

# In[3]:


# on associe et on ouvre 
f = open("./tmp/fichier_entrees.txt", "r", encoding="utf8") 

# on lit et on stocke dans une chaîne 
st_f = f.read()

# on ferme le fichier d'entrée
f.close()

# on travaille avec l'"image" du contenu du fichier
print(st_f)
print(type(st_f))
print(len(st_f))


# **Première mauvaise (fausse) surprise.** On y reviendra bien sûr ! 

# In[4]:


# on parcours et affiche la chaine de _caractères_ resultat du read()
for i in range(len(st_f)):
    print(st_f[i])


# ### Une autre lecture simple : `readlines()`

# In[5]:


# on associe et on ouvre 
f = open("./tmp/fichier_entrees.txt", "r", encoding="utf8") 

# le contenu du fichier est lu et stocké dans une liste de chaînes 
st_f = f.readlines()

# on regarde
print(st_f)
print(type(st_f), type(st_f[0]))
print(type(f))

# on ferme
f.close()


# **Pause.**
# 
# - Remarquons que ces (deux) lectures de _fichier texte_ retournent des valeurs de type _chaîne de caractères (`str`) uniquement_.
#     - C'était donc bien une mauvaise _fausse_ surprise.
# - En pratique, on aura donc souvent besoin de compléter la lecture par une conversion au type souhaité pour chaque valeur lue -- sauf si la valeur souhaitée est de type `str`. 
#     - Cette conversion dépend de ce qui a été lue : `str` _vs._ `lst` de `str`.
#     - On se facilite le travail en _adaptant la lecture_ au mieux. 
# - ($\star$) La lecture de fichier binaire impose en général de résoudre la question du type de la valeur lue lors de sa lecture : la représentation binaire de l'entier 123 est différente de celle du nombre flottant 123. .  

# ### Une lecture ligne à ligne avec `readline()`et avec conversion de type

# In[6]:


# Association et ouverture 
f_in = open("./tmp/fichier_entrees.txt", "r", encoding="utf8") 

# Entrée : lire les entrées dans f_in

# ligne 1 : nb de valeurs à lire ensuite dans le fichier f_in
n = int(f_in.readline()) # noter la conversion de type

# un tableau d'entiers pour contenir les n valeurs à lire 
vals = [0 for i in range(n)] 

# lectures ligne à ligne des n valeurs et conversions en entier
for i in range(n):
    vals[i] = int(f_in.readline()) 
    
# affichages et petits traitements (par exemple)
print(n, type(n))
print(vals, type(vals), type(vals[0]))
m = max(vals)  # fonction prédéfinie max 
print("max:", m, type(m))

# On ferme ce qu'on a ouvert
f_in.close()


# In[7]:


get_ipython().system('cat ./tmp/fichier_entrees.txt')


# ### Une lecture et une écriture (ou deux) 

# Je reviens (si besoin) dans l'état initial des fichiers de sortie et de travail avec la suite de commandes système.

# In[8]:


get_ipython().system('cat /dev/null > ./tmp/fichier_sortie.txt')
get_ipython().system('cat /dev/null > ./tmp/fichier_travail')
get_ipython().system('ls -l ./tmp/')


# In[9]:


get_ipython().system('file ./tmp/fichier_sortie.txt')
get_ipython().system('file ./tmp/fichier_travail')


# In[10]:


# on associe et on ouvre 
f_in = open("./tmp/fichier_entrees.txt","r", encoding="utf8")
f_out = open("./tmp/fichier_sortie.txt","w", encoding="utf8")
#f_tmp = open("./tmp/fichier_travail","ab")  # a : _append_ , b : _binary_

# ligne 1 
n = int(f_in.readline()) 

# pour les n valeurs
vals = [0 for i in range(n)] 

# lecture des n valeurs ligne à ligne
for i in range(n):
    vals[i] = int(f_in.readline()) 
      
# traitements 
# et stockages au format binaire dans un fichier temporaire f_tmp  
s = 0
for i in range(n):
    s = s + vals[i]
    #f_tmp.write(s.to_bytes(4, byteorder='little', signed=True))

# Sorties dans f_out
f_out.write(str(s))
f_out.write('\n') # pas nécessaire mais commode

# On ferme ce qu'on a ouvert
f_in.close()
f_out.close()
#f_tmp.close()

print("s=", s)


# In[11]:


get_ipython().system('ls -l ./tmp')
get_ipython().system('cat ./tmp/fichier_sortie.txt')
get_ipython().system('file ./tmp/fichier_sortie.txt')
get_ipython().system('file ./tmp/fichier_travail')


# **Utilisation du fichier binaire de travail** 
# 
# - Dé-commenter les 3 lignes où apparait le fichier temporaire `f_tmp`
# - Revenir à l'état initial des fichiers
# - Relancer le traitement

# **ATTENTION au `read()` !**  
# 
# Comme le dit le manuel (7.2.1):  
# > it’s your problem if the file is twice as large as your machine’s memory.

# La suite de commandes suivantes pour revenir dans l'état initial.  

# In[12]:


get_ipython().system('cat /dev/null > ./tmp/fichier_sortie.txt')
get_ipython().system('cat /dev/null > ./tmp/fichier_travail')
get_ipython().system('ls -l ./tmp/')


# ### La syntaxe classique avec `with` 
# 
# L'écriture suivante avec une clause de contexte `with` est utile en pratique.
# 
# Exemples 
# - d'abord avec les lectures complètes `read()` puis `readlines()`, 
# - ensuite avec une répétition de lectures partielles avec `readline()`(sans s),
# - avant d'approfondir certains points importants.

# In[13]:


with open("./tmp/fichier_entrees.txt", "r", encoding="utf8") as f:
    #on lit tout f et on stocke dans une str
    st = f.read()
            
    # on n a plus besoin du fichier d'entrees
    f.close() 

#voilà ce qu'on a lu
print(st)

#for caractere in st: #st est une chaine de caracteres
#    print(caractere)


# In[14]:


with open("./tmp/fichier_entrees.txt", "r", encoding="utf8") as f:
    #on lit tout f d'un seul coup comme une liste de str+\n
    entrees = f.readlines() # avec un 's' à la fin 
             
    # on n a plus besoin du fichier d'entrees
    f.close() 
        
#voilà ce qu'on a lu
print(entrees)
print(type(entrees))
      
for v in entrees: #entrees est une liste
    print(v)
      
print("Remarquer les sauts de ligne au dessus.")    


# **Lecture partielle.**
# 
# On remarquera :
# - la conversion au type entier de chaque ligne lue
# - la définition du tableau `vals` _après_ avoir lu sa taille dans le fichier. ($\star$) Une telle construction cache des choses.   
# 

# In[15]:


with open("./tmp/fichier_entrees.txt", "r", encoding="utf8") as f_in:

    # ligne 1 : nb de valeurs à lire ensuite dans le fichier f_in
    n = int(f_in.readline()) # noter la conversion de type

    # un tableau d'entiers pour contenir les n valeurs à lire 
    vals = [0 for i in range(n)] 

    # lectures ligne à ligne des n valeurs et conversions en entier
    for i in range(n):
        vals[i] = int(f_in.readline()) 

    # On ferme ce qu'on a ouvert
    f_in.close()

# affichages et petits traitements (par exemple)
print(n, type(n))
print(vals)
print(type(vals), type(vals[0]))
m = max(vals)  # fonction prédéfinie max 
print("max:", m, type(m))


# **Rmq.** Ne pas oublier les **conversions** des valeurs numériques (ou de tout autre type non `str`).

# In[16]:


with open("./tmp/fichier_entrees.txt", "r", encoding="utf8") as f:
    #on lit tout f d'un seul coup comme une liste de str+\n
    entrees = f.readlines() # avec un 's' à la fin 
             
    # on n a plus besoin du fichier d'entrees
    f.close() 

n = len(entrees)
print(n)

# ce qu'on a lu
print(entrees)

# conversion en int
v = [0 for i in range(n)]
for i in range(n): #entrees est une liste
    v[i] = int(entrees[i])
print(v)


# In[17]:


get_ipython().system('cat ./tmp/fichier_entrees.txt')
get_ipython().system('echo "On a fini d\'afficher le fichier"')


# ### $(\star)$ Approfondissements
# 
# ou 
# 
# _petites subtilités souvent à l'origine de problèmes de lecture/écriture de fichiers 
# qui font perdre beaucoup de temps :)_   
# 
# <div class="alert alert-warning">
# 
# Objectif 20 
#     
# </div>

# #### Origine des problèmes classiques
# 
# La gestion des caractères spéciaux, `\n` entre autres.
# 
# - `f.read()`peut (lire et) retourner le caractère `\n` ou  la chaîne vide `''`, ce qui est différent :
#     - `\n` = une ligne vide ... de caractères "classiques" : elle est réduite au caractère spécial qui désigne `newline`
#     - `''` = pas de ligne : on a atteint la fin du fichier (EOF)  
# Dans l'exemple suivant, remarquer que `f.read() == ''` permet de finir correctement la lecture du fichier.
# - `f.readline()` ou `f.readlines()` lit une ligne complète, caractère spécial (`\n`) compris.
#     - il retourne donc _aussi_ ce `\n` de "passage à une nouvelle ligne", 
#     - sauf dans le cas de la dernière ligne -- si celle-ci n'en comporte pas ! 

# #### Bien contrôler ses `print()`
# 
# Deux exemples pour :
# 1. rappeler comment utiliser `sep` et `end` 
# 2. expliciter l'effet du caractère spécial `\n` (nouvelle ligne) dans l'affichage d'une chaîne de caractères avec `print()`.

# In[18]:


#rappel : sep, end
s = "azertyuiop"
print(s, s, s, sep="*", end="--")
print("@@") # par defaut : end='\n'

s = "azertyuiop\n"
print(s, s, s, sep="*", end="--")


# In[19]:


# s est _une_ chaine de caractères
s = "azer\ntyuiop"
print(s)
print(s, sep="*")
print(s, end="--")


# Nous reviendrons sur les caractères spéciaux dans le chapitre sur les chaînes de caratères. 

# #### Retour sur le `.read()`
# 
# Rappel. Retourne la totalité du contenu comme une chaîne de caractères.

# In[20]:


# on associe et on ouvre 
f = open("./tmp/fichier_entrees.txt", "r", encoding="utf8") 

# le contenu du fichier est lu et stocké dans une chaîne 
st_f = f.read()

# on regarde
print(st_f)

# on regarde mieux
print(st_f, sep = "*", end="--")

print("remarquer len(st_f)=", len(st_f), " !? Explication ?")

# on ferme
f.close()


# **Explication** avec `readlines()` 

# In[21]:


# on associe et on ouvre 
f = open("./tmp/fichier_entrees.txt", "r", encoding="utf8") 

# le contenu du fichier est lu et stocké dans une liste de chaînes 
st_f = f.readlines()

# on regarde
print(st_f)
print(len(st_f))
#print(type(st_f), type(st_f[0]))
#print(type(f))

# on vérifie en comptant le nbre total de caractères 
nb = 0
for i in range(len(st_f)):
    nb = nb + len(st_f[i])
print(nb)

# on ferme
f.close()


# #### `read()` _vs._ `readline()` (sans s) 

# In[22]:


get_ipython().system('cat ./tmp/fichier_entrees.txt')


# In[23]:


print("Pour bien noter la différence entre readline() et read() : ")
print("--> bien identifier l('effet d)es sauts de ligne '\\n' du  readline():")

with open("./tmp/fichier_entrees.txt","r", encoding="utf8") as f:
    i = 0
    u = f.readline() # sans 's' à la fin : laisse le `\n` de saut de ligne sauf ''
    print("readline numero:", i, "on a lu u:", u, sep="*", end="...")
    while (u != ''): # arrêt si la dernière ligne est vide
        i = i + 1
        u = f.readline() 
        print("readline numero:", i, "on a lu u:", u, sep="*", end="---")
    print("@@@")
print("--> comprendre la dernière lecture effectuée par readline()")

print()    
print("--> des read() maintenant ... mais peu en fait : ")  
with open("./tmp/fichier_entrees.txt","r", encoding="utf8") as f:
    i = 0
    v = f.read() # lit tout f comme une str
    #print("@@@",v[-1],"@@@") # pour le quizz
    print("read numero: ", i, "on a lu v =", v, sep="*", end="---")
    while (v != ''): # arrêt si la dernière ligne est vide ... attention ! \n n'est pas une ligne vide :)
        i = i + 1
        v = f.read() # lit tout comme une str
        #v = f.read(4) # lit 8 octets et ne rajoute rien à v  
        print("read numero:", i, "on a lu v=", v, sep="*", end="---")   
    print("Fini!")
    
    f.close()

print("dernière lecture de readline: ", u)
print("dernière lecture de read: ", v)


# 
# **Quizzz**  
# 
# Quelle est la dernière ligne du fichier `./tmp/fichier_entrees.txt` ?
# 1. 188
# 2. 188\n
# 3. \n
# 4. '' (ligne vide) 
# 
# Réponse. Enlever le commentaire de l'instruction ad-hoc du code au dessus.

# En pratique, on retiendra :
# - que les sauts de lignes "visibles" sont aussi lues par `read`, `readlines`, ...  
# - que la dernière ligne d'un fichier peut être source de problème,
# - entre autres car les éditeurs de texte (et les systèmes d'exploitation) peuvent ajouter certains caractères non entérs par l'utilisateur lors de l'enregistrement et de la fermeture du fichier.

# ## Pour finir en pratique
# 
# 
# ### Le cas simple de la lecture d'un fichier que l'on (a) écrit
# 
# Deux cas de figures classiques.
# 
# 1. j'écris le traitement qui _lit_ un fichier dont la _structure_ est _décrite par ailleurs_
# 2. j'écris le traitement qui _lit_ un fichier et _je connais le traitement qui l'a créé et "rempli"_.
# 
# La démarche du second cas est simple : la logique de lecture est identique à celle de l'écriture. Elle s'obtient "inversant" le traitement d'écriture : ouverture en lecture `"r"` _vs._ écriture `"w"`, instructions de lecture `read()` ou `readlines()` ou `readline()` _vs._  instructions d'écriture `write()`, conversion inverse de `str` au type d'origine, ...

# **Exemple**. On commence par écrire la création du fichier et son écriture. 
# 
# Par souci pédagogique, l'exemple suivant inclut la création de la valeur aux traitements nécessaires à son écriture (comme une `str`) dans le fichier (en général les valeurs à stocker existent avant ce traitement).  

# In[24]:


import random
# on créé et on écrit dans un fichier 
with open("./tmp/exemple.txt", "w", encoding="utf8") as f:
    for i in range(20): # 20 dates
        # génération des dates
        m = random.randint(1, 12) # un mois au hasard
        if m == 2:
            nb_jours = 28
        elif m % 2 == 1:
            nb_jours = 31
        else:
            nb_jours = 30       
        q = random.randint(1, nb_jours) # un quantieme au hasard
        
        # traitement pour stockage
        s = str(q) + "." + str(m) + ".2021" + "\n" # represention "formatee" de la date en une chaine 
        
        # stockage
        f.write(s)
    f. close()


# In[25]:


get_ipython().system('cat ./tmp/exemple.txt ')


# On recopie le code de création-écriture et on "inverse" le traitement.

# In[26]:


# on va utiliser 20 dates
dates = [[0 for j in range(3)] for i in range(20)] # les 20 dates

# on lit le fichier d'entree -- noter le mode "r" maintenant 
with open("./tmp/exemple.txt", "r", encoding="utf8") as f:
    for i in range(20):         # parcours ligne à ligne  
        s = f.readline()        # lecture ligne
        print(s)                # pour info
        l = s.split(sep=".")    # transforme s en une liste l de ses champs identifés par 'sep'
        print(l)                # pour info
        dates[i][0] = int(l[0]) # conversion et stockage quantieme 
        dates[i][1] = int(l[1]) # idem mois
        dates[i][2] = int(l[2]) # idem annee

f. close()

print(dates)


# ### Une simplification "pythonique"
# 
# La construction python suivante est à la fois très spécifique et très utile en pratique : simple et efficace.
# Bien garder en tête que les traitements précédents n'ont pas disparu mais sont écrits de façon plus synthétique avec ce parcours typiquement "pythonique".
# 
# On reprend l'exemple précédent.

# In[27]:


# on lit le fichier d'entree -- noter le mode "r" maintenant 
f = open("./tmp/exemple.txt", "r", encoding="utf8")

d = 0
for date in f: # parcours et lit f ligne à ligne  
    #print(date) # pour info si besoin
    
    l_date = date.split(sep=".") 
    #print(l) # pour info si besoin
    
    dates[d][0] = int(l_date[0]) 
    dates[d][1] = int(l_date[1])
    dates[d][2] = int(l_date[2]) 
    d = d+1 # il faut gérer le remplissage du tableau maintenant
    
f. close()

print(dates)


# ### Un dernier conseil
# 
# - Le risque d'erreur lors de la mise au point du traitement d'ES sur fichiers est  important.  
# - Il n'est pas rare de perdre tout ou partie d'un fichier à lire.
# - On ne peut donc que conseiller :
# 1. de **commencer par** effectuer une copie de sauvegarde des fichiers originaux avant tout développement de code d'ES
# 2. de vérifier pas à pas la mise au point de ces traitement avec des `print()` bien choisis -- qui seront bien sûr commentés une fois le traitement validé.

# ## Synthèse 

# ### Avoir les idées claires
# 
# - Distinguer fichier logique _vs._ physique, texte _vs._ binaire, mode lecture _vs._ écriture (_vs._ lecture-écriture) 
# - Connaître les étapes de manipulation d'un fichier : association/ouverture/lecture-écriture/fermeture
# - Distinguer valeur (numérique) et sa représentation textuelle 
# 

# ### Savoir-faire
# 
# - Savoir écrire les lectures-écritures simples de fichier texte avec les instructions python adaptées  
# - Comprendre et gérer l'effet des caractères spéciaux 
# 

# ### Ce qu'il restera à voir
# 
# 
# Le chapitre "ES avancées" complète celui-ci en présentant comment _formater_ les données lues ou écrites dans les fichiers.
# 
# On peut se déplacer dans un fichier pour accéder à un enregistrement quelconque. Ce type de traitement nécessite de caractériser comment la position de ces enregistrements  est définie -- par le langage de programmation et en général en nombre d'octets depuis le début du fichier. Le lecteur intéressé se reportera à la documentation (de python) pour ces manipulations un peu techniques. 
# 
# Les traitements précédents permettent de créer et d'exploiter des fichiers, et ce indépendamment de leur stockage dans le _système de fichiers_ de l'environnement utiisé (Linux, w\*\*\* ou m\*\*\*).
# Il est utile de compléter ces traitements par de la _manipulation_ de fichiers de façon similaire à celle vue en cours de Système au semestre 1. Pour cela, python propose les modules suivants :  
# - `os` qui permet de se déplacer dans l'arborescence du système de fichiers  
# - `os.path`, sous-module du précédent, qui permet de lister des fichiers, des répertoires et certaines de leurs caractéristiques  
# - `shutil` qui permet de copier, déplacer et supprimer des fichiers ou des parties d'arborescence.  
# 
jupyter nbconvert --to html_embed --template toc2 3-ES-fichiersjupyter nbconvert 3-ES-fichiers.ipynb --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --SlidesExporter.reveal_theme=solarized