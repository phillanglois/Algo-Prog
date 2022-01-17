#!/usr/bin/env python
# coding: utf-8

# # Algorithmique et Programmation en 2021
# 
# Vous : **L1 math-info**  
# 
# Moi : [**Philippe Langlois**](langlois@univ-perp.fr)  
# 
# Comment me contacter : _PAR E-MAIL_  
# 
# Comment me rencontrer : sur RDV _DEMANDÉ PAR E-MAIL_  
# 
# Où me rencontrer : au bâtiment B, étage 1, à gauche (laboratoire DALI).
# 
# 

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Algorithmique-et-Programmation-en-2021" data-toc-modified-id="Algorithmique-et-Programmation-en-2021-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Algorithmique et Programmation en 2021</a></span><ul class="toc-item"><li><span><a href="#Algorithmique-:-organisation" data-toc-modified-id="Algorithmique-:-organisation-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Algorithmique : organisation</a></span><ul class="toc-item"><li><span><a href="#Contrôle-de-connaissances" data-toc-modified-id="Contrôle-de-connaissances-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Contrôle de connaissances</a></span></li><li><span><a href="#CM" data-toc-modified-id="CM-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>CM</a></span></li><li><span><a href="#TD" data-toc-modified-id="TD-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>TD</a></span></li></ul></li><li><span><a href="#Programmation-:-organisation" data-toc-modified-id="Programmation-:-organisation-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Programmation : organisation</a></span><ul class="toc-item"><li><span><a href="#Contrôle-de-connaissances" data-toc-modified-id="Contrôle-de-connaissances-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Contrôle de connaissances</a></span></li><li><span><a href="#TP" data-toc-modified-id="TP-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>TP</a></span></li><li><span><a href="#Acquis-et-prérequis" data-toc-modified-id="Acquis-et-prérequis-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Acquis et prérequis</a></span></li></ul></li><li><span><a href="#IMPORTANT-:-spécificités-période-COVID" data-toc-modified-id="IMPORTANT-:-spécificités-période-COVID-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>IMPORTANT : spécificités période COVID</a></span><ul class="toc-item"><li><span><a href="#Consignes-pour-le-distanciel" data-toc-modified-id="Consignes-pour-le-distanciel-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Consignes pour le distanciel</a></span></li><li><span><a href="#Organisation" data-toc-modified-id="Organisation-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Organisation</a></span></li><li><span><a href="#A-ce-jour-:-26.01.2021." data-toc-modified-id="A-ce-jour-:-26.01.2021.-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>A ce jour : 26.01.2021.</a></span></li></ul></li><li><span><a href="#Algorithmique-:-programme-détaillé" data-toc-modified-id="Algorithmique-:-programme-détaillé-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Algorithmique : programme détaillé</a></span></li><li><span><a href="#Programmation--:-programme-détaillé" data-toc-modified-id="Programmation--:-programme-détaillé-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Programmation  : programme détaillé</a></span></li><li><span><a href="#Supports-de-cours" data-toc-modified-id="Supports-de-cours-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Supports de cours</a></span><ul class="toc-item"><li><span><a href="#Les-pdf-sur-moodle" data-toc-modified-id="Les-pdf-sur-moodle-1.6.1"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Les pdf sur moodle</a></span></li><li><span><a href="#Les-notebook-python-sur-moodle" data-toc-modified-id="Les-notebook-python-sur-moodle-1.6.2"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Les notebook python sur moodle</a></span></li><li><span><a href="#Interactions-et-évolutions-des-supports" data-toc-modified-id="Interactions-et-évolutions-des-supports-1.6.3"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>Interactions et évolutions des supports</a></span></li></ul></li><li><span><a href="#Travailler-en-python" data-toc-modified-id="Travailler-en-python-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Travailler en python</a></span><ul class="toc-item"><li><span><a href="#IMPORTANT-:-De-quoi-a-t-on-absolument-besoin-?" data-toc-modified-id="IMPORTANT-:-De-quoi-a-t-on-absolument-besoin-?-1.7.1"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>IMPORTANT : De quoi a-t-on <em>absolument</em> besoin ?</a></span></li><li><span><a href="#En-pratique" data-toc-modified-id="En-pratique-1.7.2"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>En pratique</a></span><ul class="toc-item"><li><span><a href="#Installer-un-environnement-python" data-toc-modified-id="Installer-un-environnement-python-1.7.2.1"><span class="toc-item-num">1.7.2.1&nbsp;&nbsp;</span>Installer un environnement python</a></span></li><li><span><a href="#Distributions-python-classiques" data-toc-modified-id="Distributions-python-classiques-1.7.2.2"><span class="toc-item-num">1.7.2.2&nbsp;&nbsp;</span>Distributions python classiques</a></span></li><li><span><a href="#Environnement-de-travail-en-autonomie-pour-machine-étudiant" data-toc-modified-id="Environnement-de-travail-en-autonomie-pour-machine-étudiant-1.7.2.3"><span class="toc-item-num">1.7.2.3&nbsp;&nbsp;</span>Environnement de travail en autonomie pour machine étudiant</a></span></li></ul></li></ul></li><li><span><a href="#Références-bibliographiques" data-toc-modified-id="Références-bibliographiques-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Références bibliographiques</a></span><ul class="toc-item"><li><span><a href="#Algo-et-prog" data-toc-modified-id="Algo-et-prog-1.8.1"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>Algo et prog</a></span><ul class="toc-item"><li><span><a href="#Ellipses" data-toc-modified-id="Ellipses-1.8.1.1"><span class="toc-item-num">1.8.1.1&nbsp;&nbsp;</span>Ellipses</a></span></li><li><span><a href="#Hatier" data-toc-modified-id="Hatier-1.8.1.2"><span class="toc-item-num">1.8.1.2&nbsp;&nbsp;</span>Hatier</a></span></li><li><span><a href="#Nathan" data-toc-modified-id="Nathan-1.8.1.3"><span class="toc-item-num">1.8.1.3&nbsp;&nbsp;</span>Nathan</a></span></li></ul></li><li><span><a href="#Approfondisssement-en-algo" data-toc-modified-id="Approfondisssement-en-algo-1.8.2"><span class="toc-item-num">1.8.2&nbsp;&nbsp;</span>Approfondisssement en algo</a></span></li><li><span><a href="#Approfondisssement-en-programmation-Python" data-toc-modified-id="Approfondisssement-en-programmation-Python-1.8.3"><span class="toc-item-num">1.8.3&nbsp;&nbsp;</span>Approfondisssement en programmation Python</a></span></li><li><span><a href="#Outils" data-toc-modified-id="Outils-1.8.4"><span class="toc-item-num">1.8.4&nbsp;&nbsp;</span>Outils</a></span></li></ul></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></li></ul></div>

# ## Algorithmique : organisation 
# 
# - 14 séances de CM : 1.5h/semaine sauf semaine 1 (2 séances)
# - 14 séances de TD : 1.5h/semaine sauf semaines 1, 12 et 13 (resp. 0, 2, 2 séances)
# - 3 groupes de TD
#     - Ph. Langlois, Farah Benmouhoub, Thierry Arrabal 
# 

# ### Contrôle de connaissances
# 
# - Premier contrôle écrit à mi-parcours (CC), 2 heures  :  
# __jeudi 1 avril 2021__ (date à confirmer mais ce n'est pas un poisson :) = mi-parcours et programme correspondant  
# 
# - Second contrôle écrit (CT), 2 heures  
# semaine des examens et qui porte sur la totalité du programme
# 
# - Evaluation :  moyenne(CC, CT)  

# ### CM
# 
# - séance de 1h25
# - 45-50 min de "matière de cours"
# - 25 min d'exercices dirigés et d'interactions
# - 5 min de culture générale en info : outils, historique, ...
# - 5 min de démarrage technique : faut bien !

# ### TD
# 
# - séance de 1h25
# - par groupe de 2 à __4__
# - **objectif 10** ou **objectif 20**  
#     - feuilles de TD en 2 parties
#     - objectif 10 : 
#         - applications basiques du cours, démarche guidée
#         - pour celles et ceux qui ne veulent pas continuer en informatique au delà du L2 math-info  
#     - objectif 20 : 
#         - applications plus avancées du cours, démarche plus autonome
#         - pour celles et ceux qui **veulent continuer** en licence et master informatique, CAPES  informatique (nouveau !), ...
#     - comment choisir son niveau d'objectif ?
#         - note algo semestre 1 < 10 --> objectif 10
#         - le choix n'est pas définitif
#         - méthodologie : __chaque (groupe) d'étudiants__ définit __son rythme__ en suivant le parcours proposé par le chargé de TD.  

# ## Programmation : organisation
# 
# - 11 séances de CM : 2h/semaine (4) puis 1h/semaine (7)
# - 10 séances  de TP : 1.5h/semaine (4) puis 3h/semaine 
# - 5 groupes de TP
#     - Ph. Langlois, Vincent Zucca, Hanane Benmaghnia, Téo Plenet, Farah Benmouhoub
#    

# ### Contrôle de connaissances
# 
# - Contrôle continu (CC) :   
#     - 2 TP "en temps limité", cad. à rendre __avec dead-line__ de dépôt 
#     - **vendredi 20 mars 2021 et vendredi 10 avril 2021** 
#     
# - Contrôle terminal _sur machine_ (CT) : 3 heures  
#     - **vendredi 15 mai 2021**  (date à confirmer)  
#     
# - Evaluation : moyenne(CC, CT) avec CC = moyenne(2 TP)

# ### TP
# 
# - 1 TP = un _notebook jupyter_   
# 
# - codage, expérimentation et approfondissement :
#     - des TD d'algo 
#     - du CM de Programmation  
# 
# - exemples de TP avec dead-line (pour l'évaluation de CC) :  
#     - mini base de données  
#     - traitement d'images  
#     - cryptographie   
# 
# 
#     

# ### Acquis et prérequis
# 
# - Savoir différencier les _types_ de données :  
#     - type scalaire : booléen, entier, réels, caractères  
#     - type composés : chaîne de caractères, vecteur, matrice, ...  
# 
# - Connaître leur _représentation_ dans un langage informatique donné  
#     - `bool`, `int`, `float`, `str`, `list`  
#     - et les changement de types associés : `int()`, `float()`, ...  

# - Bien différencier _valeur_ vs. _variable_ vs. _constante_  
#     - _évaluation_   
#     - et comprendre comment le modèle d'exécution en modifie l'état  
#     - _affectation_ : `=`  

# - Bien comprendre le modèle _séquentiel_ de l'exécution d'un algorithme   
#     - _instruction_   
#     - _expression_ ("formule")   
# 
# - Comprendre que les structures de contrôle permettent de _casser_ la séquentialité de l'exécution d'un algorithme  
#     - branchement conditionnel  : _choisir_   
#         - `if ...:`, `elif ...:`,  `else:`  
#     - répétitions : _répéter_  
#         - `while`  
#         - `for . in ...`, (`break`, `continue`)   
#     

# - Distinguer : les _entrées_ vs. le _traitement_ vs. la _sortie_  
#     - `input()`, `print()`  
# 
# - Spécificités python  
#     - _indentation_  
#     - typage dynamique  

# ## IMPORTANT : spécificités période COVID
# 
# ### Consignes pour le distanciel 
# 
# - Il est de votre responsabilité d'avoir une connection et un environnement fonctionnels
# - Votre environnement doit comporter un micro, une caméra, et un débit suffisant à leur utilisation.  
#     - On trouve sur le net des caméras usb pour 2€ (voire moins) donc il est difficile d'accepter l'absence de caméra opérationnelle -- en cette période. 
# - La connection sous zoom doit faire apparaitre explicitement vos **Nom et  Prénom, dans cet ordre**.
# - La **caméra doit être active** pendant toute la séance, sauf raison indiquée préalablement par e-mail à mon attention et ou indication **explicite** de l'enseignant.
#     - En pratique, l'enseignant peut demander nominativement à un.e étudiant.e d'activer ou de désactiver sa caméra.
# - En revanche, le micro doit être **systématiquement désactivé** pendant toute la séance
#     - En pratique, l'enseignant peut demander nominativement à un.e étudiant.e d'activer son micro.

# ### Organisation
# 
# **Ce qui suit est susceptible de modifications importantes, difficilement anticipables et indépendantes de notre volonté. Une communication par e-mail (via l'ENT) sera systématiquement effectuée en cas de modification. Bien sûr, cet engagement n'engage que ces enseignements d'algorithmique et de programmation, semestre 2, L1 math-info.**

# ### A ce jour : 26.01.2021.
# 
# - Les séances de CM, TD et TP ont lieu aux jours et heures indiquées sur l'emploi du temps en ligne.
# - Les CM sont dispensés en distanciel par zoom -- relire les consignes du paragraphe précédent.  
# - Les TP de programmation sont organisés en distanciel et par groupe de TP sous l'encadrement et la responsabilité de l'enseignant de TP -- relire les consignes du paragraphe précédent.
# - **Les infos de connection sont diffusées par e-mail 1/4h environ avant le démarrage de chaque séance.**
# 
# 

# **Cas particulier des TD d'algorithmique :**
# 
# Afin de maximiser votre interaction avec un enseignant tout en respectant les contraintes sanitaires (1/2 occupation des salles) et les consignes ministérielles (TD en présentiel à 50%), nous adoptons l'organisation suivante :
# 
# - La moitié de la promotion (un premier méta-groupe) sera en _TD présentiel_ une semaine sur deux, l'autre moitié (un second méta-groupe) en _TD distanciel_ au **même moment**.
# - Chaque méta-groupe est composée d'étudiants des groupes TD1, TD2 et TD3.
#     - Un découpage de ces 2 méta-groupes _est_ indiquée sous l'ENT. 
#     - Si besoin de changer de semaine en présentiel, me contacter **dès maintenant** par e-mail et avec des arguments précis et fondés.  
# 
# Le scénario suivant s'applique alternativement à chaque méta-groupe chaque semaine : semaines paires vs. semaines impaires.
# - Le méta-groupe en présentiel est réparti dans deux salles de TD, chacune avec un.e chargé.e de TD.
# - Le méta-groupe en distanciel (au même moment) est dans une des deux configurations suivantes (à affiner avec l'expérience) :
#     - successivement par moitié pour 45 minutes (essai les 2 première semaines);
#     - ou tous pendant 1h30.    
# 
# Ainsi les enseignants de TD seront avec vous chaque semaine : une semaine sur deux en présentiel, l'autre en distanciel. 

# ## Algorithmique : programme détaillé
# 
# 1. utilisation avancée de boucles et de tableaux
#     - boucles imbriquées, indépendantes ou non
#     - traitements divers avec des tableaux 1D ou plus 
#     - premières estimations de complexité 

# 2. complexité
#     - combien _coûte_ un algorithme pour résoudre un pb donné ?  
#     - combien de temps ? combien de place mémoire ?  
#     - tous les problèmes coûtent pareils ?  
#     - notions : complexité en temps, pire cas, complexité asymptotique  
# 5. exemple d'algos plutôt numériques et leurs complexités
#     - différentes évaluations de polynômes 

# 4. récursivité : 
#     - **la notion centrale du semestre**
#     - principes 
#     - applications 
#     - notions : itératif vs. récursif, pile/arbre des appels, complexité
#     - Remarque : la récursion s'appuie sur la notion de _fonction_ qui est donc étudiée de façon simultanée en Algorithmique et Programmation  

# 5. rechercher 
#     - recherche séquentielle
#     - recherche dichotomique 
#     - notions : les algos, leurs complexités, (les preuves)   
# 6. trier 
#     - tris itératif : algos, complexité, (preuve)   
#     - tris  récursifs : algo, complexité, (preuve)   

# 7. compléments si assez de temps : prouver la terminaison et la correction d'un algorithme
#     - l'algo fournit la/les solution/s en un temps fini
#     - l'algo résoud bien le pb
#     - notions : invariant de boucle, preuve de terminaison

# ## Programmation  : programme détaillé
# 
# 1. types de donnnées scalaires
#     - rappels 
#     - approfondissement : introspection  

# 2. fonctions 
#     - en-tête, corps, appel, paramètres formels et effectifs. 
#     - portée, visibilité, variables locales vs. paramètres  
#     - mode de passage des paramètres
#     - exemples du cours : doubler, permuter  

# 3. tableaux 1D 
#     - rappel : avec des listes python (`lst`)
#     - avec des `ndarray` de `numpy`
#     - exemples du cours : Lire, stocker, moyenne/min/max d'un tableau (valeurs, indices)
# 
# 4. tableaux 2D, 3D ; application au traitement d'images
#     - avec des listes (de listes) python  
#     - avec des `ndarray` de `numpy`
#     - images et matrices  
#     - boucles imbriquées  
#     - exemples du cours : 
#         - traitement d'images : initialisation niveaux de gris, transformations d'images (miroir, contraste, contours, ...) 
#         - algorithmes sur les matrices : vérification (identité, symétrie), calcul (produit de matrices,...) , génération de formes particulières (transposée, ...)

# 5. autres types de données composés
#     - listes (`lst`) : fonctions et méthodes
#     - n-uplets (`tuple`), ensembles (`set`), dictionnaires (`dict`)
# 6. entrées/sorties et fichiers
# 7. modules
#     - utilisation de modules existants 
#     - exemple d'outils :`numpy`, `scipy`, `matplotlib`, `time` 
#     - définition de ses modules
# 9. exceptions

# ## Supports de cours
# 
# ### Les pdf sur moodle 
# 
# - feuilles des sujets de TD (algo) et TP (prog)  
# - sujets et correction des CC et CT des années précédentes

# ### Les notebook python sur moodle
# 
# Version `html` des notebooks jupyter présentés en CM.
# 
# 
# Et aussi certains :
# - sujets et corrections TD 
# - sujets et corrections contrôles, devoirs et examens des années précédentes

# ### Interactions et évolutions des supports
# 
# __Evolution en 2021 :__ 
# 
# Un notebook supplémentaire `Complements-2021.ipynb` est mis à jour à chaque séance, et sur moodle en version html.
# 
# Les autres supports (CM, TD, TP) sont mis à jour en cas d'erreur importante.  
# 
# 

# ## Travailler en python
# 
# Il est indispensable :
# 
# - d'avoir accès à un environnement de programmation python, si possible assez complet,
# 
# - d'avoir son propre ordinateur configuré de façon complète et selon vos préférences.    
# 
# Il y a déjà 3 choix d'OS possibles : windows, linux et mac os ; les 2 premiers étant disponibles sur les ordinateurs de l'UPVD.    
# 
# Ensuite, les [distributions python](#En%20pratique) sont assez variées, et peuvent différer selon les OS .
# 
# Il est aisé _pour chacun_ de trouver ce qui correspond à ses contraintes matérielles et ses envies.  

# ### IMPORTANT : De quoi a-t-on *absolument* besoin ?
# Ce qui suit est une liste minimale de composants utiles cette année et les années à venir. 
# Elle peut sembler longue mais en pratique, ces composants "arrivent" d'un seul coup avec une distribution -- cf. paragraphe suivant.  
# 
# 
# - l'`IDLE` python 3  
#     - éditeur, interpréteur, débugger utilisé en TP au semestre 1
# - `jupyter notebook`  
#     - pour intégrer dans _un unique fichier_ du texte, des maths ($\LaTeX$) et du code python qui s'exécute, les résultats de ces éxecutions (valeurs, courbes, images, ...) et exporter tout ça en `html`ou `pdf` ou en `slide`  
#     - très utile pour les exercices 
#     - _utilisé pour les TP de programmation à rendre_
#     - utilisable dans toutes les matières ou presque    
#     
# - les gestionnaire de paquets (modules) python pour compléter et mettre à jour son environnement
#     - `conda`: plus complet si distribution anaconda utilisée (solution recommandée)  
#     - `pip` : classique   
#     - Exemple d'utilisation : 
#         - `conda` : `conda list`, `pip install le_module_que_je_veux` et voilà, c'est fini ! 
#         - `pip` : pareil `list`, `update`, `install`  
# 
# - modules indispensables 
#     - `numpy ` : fournit des _vrais_ tableaux multi-dimentionnels et des tas de fonctions et types numériques pour effectuer du calcul
#     - `matplotlib`: pour le traitement graphique de données, et en particulier :
#         -  `matplotlib.pyplot` pour des affichages élaborés
#         -  `matplotlib.image`  pour le traitement d'images
#     - `tkinter` : pour réaliser des interfaces graphiques  
#     
# - modules utiles mais optionnels cette année  
#     - `scipy `: scientific python qui rassemble des modules de calcul scientifiques (dont `numpy`) 

# **Pièges**
# - Ne pas confondre `python 2` et `python 3` 
# 
# **Conseil**
# - Choisir une distribution la plus complète possible dès le début.   

# ### En pratique
# 
# #### Installer un environnement python
# 
# On conseille d'installer la distribution Anaconda.  
# Dans ce cadre, on peut s'aider des  liens ci-après.
# Le web est bien sûr plein de tutos et autres sites explicatifs ...
# 
# - [Un tutoriel](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/)  
# - [Un autre](https://www.davidculley.com/installing-python-on-a-mac/) pour mac mais/et en anglais, très complet : le début seul devrait vous suffire.
# 
# #### Distributions python classiques  
# 
# On télécharge, on installe, on travaille !  
# 
# - [Anaconda](https://www.anaconda.com/products/individual)  : à privilégier (pour son gestionnaire `conda`) sauf choix perso justifié.  
# - [Enthought Python Distribution](http://www.enthought.com/products/epd.php) : très complet  
# - [Thonny](https://thonny.org/) Attention : Thonny installe sa propre version de Python par défaut.   
# - [Pyzo](http://www.pyzo.org)
# - [SAGEMATH](http://sagemath.org/)  : bcp plus général qu'un simple environnement python. A conseiller pour ceux qui veulent continuer en ... mathématiques.
# 
# 
# #### Environnement de travail en autonomie pour machine étudiant 
# 
# - [edupython](https://edupython.tuxfamily.org) issu d'AmiensPython mais **[pour windows](http://edupython.tuxfamily.org/documentation/index.php?title=Installation_et_Configuration)**
#     - Moteur Python : version 3.7.6
#     - Editeur : PyScripteur (version 3.6.3)
#     - Administration de base de données : SQLite Database Browser (version 3.11.2)
#     - **Jupiter notebook préinstallé** 
#     - Module lycée
#     - Calcul numérique: Numpy (version 1.18.3) et Scipy (version 1.4.1)
#     - Sorties graphiques: Matplotlib (version 3.1.3)
#     - Calcul formel: Sympy (version 1.5.1)
#     - Traitement d'images: PIL (Pillow 7.0.0) et Open CV (Version 4.2.0)
#     - Liaison série: Serial (version 2.7)
#     - Base de données: SQLite3 (version standard) et mysql (version 8.0.13)
#     - Traitement de données: Pandas (version 1.0 3)
#     - Réalisation de jeux: Pygame (version 1.9.4)
#     - Autres: pyknon (musique), Nanpy (Arduino), Follium (cartes), scikit-learn (IA)... 
#  
#  
# 
# 
# 
# 

# ## Références bibliographiques
# 
# ### Algo et prog
# - Informatique pour tous en CPGE avec Python et nouveaux programmes 2013 : 
# 
#     - B. Wack _et al._ (Eyrolles)  
#     - Th. Audibert et A. Oussalah. (Ellipses)   
#     - E. Le Nagard (Pearson)
# 

# - L'introduction de la spécialité NSI (Numérique et Science Informatique) a donné l'opportunité de la publication de nombreux ouvrages de niveau Première ou Terminale. Le programme de ces classes étant assez ambitieux, ces ouvrages sont de bonnes premières références, voire de très bonnes pour les étudiant.e.s Objectif 10. 
# 
# #### Ellipses
# 
# Titre : Spécialité Numérique et sciences informatiques : 30 leçons avec exercices corrigés - Première - Nouveaux programmes
# Auteur(s) : Balabonski Thibaut, Conchon Sylvain, Filliâtre Jean-Christophe, Nguyen Kim
# Editeur : Ellipses
# ISBN : 9782340033641 (Première)
# Volume niveau Terminale en préparation.
# 
# Titre : Spécialité Numérique et sciences informatiques - Première, , Terminale  - nouveaux programmes
# Auteur(s) : Serge Bays (Auteur) Bertrand Hauchecorne (Direction) 
# Editeur : Ellipses
# Collection	Prepas Sciences
# ISBN : 2340031729 (Première), 2340038448 (Terminale)
# 
# Titre : Spécialité NSI (numérique et sciences informatiques) - Première - nouveaux programmes
# Auteur(s) : Legrand David
# Editeur : Ellipses
# Collection Parcours et méthodes
# ISBN : 9782340038578 (Première),
# 
# Spécialité Numérique et sciences informatiques - Première - nouveaux programmes
# Cécile Canu (Auteur) 
# Editeur : Ellipses
# Collection Competences Attendues
# ISBN : 2340031788 
# 
# Titre : Spécialité NSI - Numérique et sciences informatiques - Terminale - nouveaux programmes
# Auteur(s) : Jean-Christophe Bonnefoy (Auteur) Bertrand Petit (Auteur) 
# Editeur : Ellipses
# Collection Competences Attendues
# ISBN :  2340038154 
# 
# 
# #### Hatier
# 
# Titre : NSI 1ère générale (spécialité) - Prépabac Cours & entraînement. 
# Nouveau programme, nouveau bac (2020-2021)
# Auteur(s) : Céline Adobet (Auteur) Guillaume Connan (Auteur) Gérard Rozsavolgyi (Auteur) Laurent Signac (Auteur) 
# Nouveau programme de Première (2020-2021) 
# Editeur : Hatier
# Collection	: Prepabac Entrainement Progress
# ISBN : 2401052305
# Version e-book : 8,99€
# 
# Titre : NSI Tle générale (spécialité) - Prépabac Cours & entraînement. 
# Nouveau programme, nouveau bac (2020-2021)
# Auteur(s) : Guillaume Connan (Auteur) Vojislav Petrov (Auteur) Gérard Rozsavolgyi (Auteur) Laurent Signac (Auteur) 
# Editeur : Hatier
# Collection	: Prepabac Entrainement Progress
# ISBN : 2401064613
# Version e-book : 8,99€
# 
# #### Nathan
# 
# Titre : Interros des Lycées Numérique Sciences Informatiques - Première, Terminale
# Auteur(s) :  Stéphane Pasquet (Auteur) MIKAEL LEOPOLDOFF 
# Editeur : Nathan
# Collection: Interros des Lycées
# ISBN : 2091574651 (Première),  2091575437  (Terminale)
# 
# 
# 

# ### Approfondisssement en algo
# - des petits livres 
#     - Cormen
#     - Damphousse
#     
# - des gros, voire très gros, livres
#     - Cormen _et al._
#     - Knuth
# 
# ### Approfondisssement en programmation Python
# - poly ou bouquin de Cordeau-Pointal (fr)
# - [ref python 3](https://docs.python.org/3/reference/index.html)  (eng)

# ### Outils
# - _Débuter avec les notebooks_. De Denis Pinsard et disponible sur moodle/Programmation Python.
# 
# - [python tutor](http://pythontutor.com) 
#     - permet de visualiser l'effet des instruactions d'un petit code  
#     - très utile au début pour comprendre des _effets de programmation_, pas d'algorithmique
#     - complément de l'idle python
#     - demo 

# ## Conclusion
# 
# Bon travail ce semestre !  
support html généré avec :
```
jupyter nbconvert --to html_embed --template toc2 0-presentation-2021.ipynb
```