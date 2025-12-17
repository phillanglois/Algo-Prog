(ch:intro)=
# Algo Prog en 2026

Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.

- Vous : **L1 math-info**  
- Moi : **Philippe Langlois**   
- Comment me contacter : ![](./fig/mail_phl.png)  
- Comment me rencontrer : sur RDV _DEMANDÉ PAR E-MAIL_  
- Où me rencontrer : au bâtiment B, étage 1, à gauche (laboratoire DALI).

## Algo-Prog ce semestre


- Les [supports du CM](https://phillanglois.github.io/Algo-Prog/bonjour.html) régulièrement mis à jour.
- Les autres ressources sont sur l'espace moodle de cet enseignement.

### Saison 2026

- 16 séances de CM, 1.5h : 1 séance/semaine, 3 ou 2 les deux premières semaines
- 13 séances de TD-TP, 3h : 1 séance/semaine 
- chargés de TD : David Parello (TD1), Nassima Haroune (TD2), Ph. Langlois (TD3), Laurent Zamo (TD4)


### Contrôle de connaissances et dates importantes

CC : contrôle "dit" continu, CT contrôle "dit" terminal

```{Warning}
**Note UE = 0.25*(CC1+CC2) + 0.5*CT**
```

**Dates et détails.** Les dates de ces évaluations sont annoncées en début de [la page d'accueil du cours](ch:bonjour).

## Structure de l'enseignement

### Organisation

- 10 chapitres, 16 séances de CM, 12 séances de TD ou TP
- "13ème séance" : écrit mi-parcours, TP de fin de semestre
- Pour chaque chapitre  
  - explicitation des _compétences_ visées : savoirs, savoirs-faire
  - des quizz d'aide à la compréhension et la mémorisation de ces compétences
  - _l'enseignant_ ... présente et explique des exercices détaillés en CM : top-down
  - _vous_ travaillez sur des exercices de TD et de TP, les contrôles des années précédentes, ... _Vous_ sollicitez le chargé de TD pour toute question : bottom-up

### CM

```{warning}
Le CM est **essentiel** à la compréhension globale de l'UE issue de l'articulation de toutes les notions traitées.
```

Une séance de CM de deux heures = deux séquences d'une heure organisées comme suit :

- "matière de cours" : nouvelles notions (40 min)
- exercices dirigés et interactions : quizz, questions/réponses, ... (10 min)
- pause (5 min)

#### La très grande importance des CM

- **Tout** ce qui est nécessaire à votre compréhension est présenté en cours avec des explications orales adaptées, les répétitions nécessaires des points importants, les mises en garde sur les notions difficiles,  ce qui est essentiel _vs._ ce qui est plus secondaire, les compétences à acquérir : savoir, savoir faire et savoir être, ce qui est attendu pour le contrôle de connaissance, ce qui relève de l'objectif 10 _vs._ de l'objectif 20, ...
  
  - les 2/3 du travail de compréhension/mémorisation reposent sur les CM 

- **Morale** : ne manquer aucun CM, être attentif, prendre des notes, poser des questions, **se poser** des questions, demander des pauses pour reprendre une attention maximale  

  - les notes de cours fournies sont trompeuses : comme un film sans le son :(

- **Méthodologie de travail du CM** : 
    1. relire le cours le soir de l'amphi (15-20 min) 
    2. le reprendre en détail 4-5 jours après et en préparant des exercices de TD ou de TP -- en groupe : ça aide !
    3. faire une auto-évaluation de ce que _vous_ en avez retenu la veille du cours suivant : le chapitre _Compétences_ est utile. 
    4. identifier les questions à poser en séance de TD ou en CM

**Il est faux de croire** que :

> l'exercice posé en examen n'a pas été traité en cours ni en td !  

Cette impression traduit une _compréhension insuffisamment approfondie_ du cours. 
C'est-à-dire un investissement insuffisant dans les étapes 2-3-4 de la méthodologie décrite au paragraphe précédent.
Visez deux résultats : 

  1. d'abord une véritable _appropriation personnelle_ du cours ;
  2. ensuite, à terme, _votre autonomie_ dans cette démarche d'appropriation, autonomie indispensable à la réussite à l'université. 

### Objectif 10 ou Objectif 20 ?

**Objectif 10 (O10)** 

- applications basiques du cours, démarche guidée
- pour celles et ceux qui ne veulent pas continuer en informatique au delà du L2 math-info  

**Objectif 20 (O20)**

- applications plus avancées du cours, démarche plus autonome
- pour celles et ceux qui **veulent continuer** en licence et master informatique, CAPES  informatique (nouveau !), ...

**Contrat**

- feuilles de TD en 2 parties : O10 et 020
- tous les sujets notés comportent au moins 10 points de niveau O10 

**Comment choisir son niveau d'objectif ?**

- note algo semestre 1 < 10 --> objectif 10
- le choix n'est pas définitif
- méthodologie : __chaque (groupe) d'étudiants__ définit __son rythme__ en suivant le parcours proposé par le chargé de 
TD.

### TD et TP 

TD : des exercices pour appliquer les connaissances du cours 

TP : un sujet sur un thème pour maitriser les notions et acquérir du savoir-faire personnel  

- 1 TP = un _notebook jupyter_
- codage, expérimentation et approfondissement 
- exemples de TP : mini base de données, traitement d'images, cryptographie, classification, problèmes classiques en informatique : huit reines, sac à dos, ...

### Supports de cours

```{note}
Excepté ce support de cours, toutes les autres ressources sont sur moodle et sont mises à jour **très** régulièrement
```

- corrections des exercices objectif 10 des TD : au fur et à mesure du semestre
- sujets des TP : notebook python (versions ipynb, pdf, html)  
- sujets et correction des CC et CT des années précédentes

### Les outils pour comprendre, mieux retenir

```{tip}
**Pratiquer pour maitriser**
```

- un environnement python qui fonctionne

- les [notebook jupyter](https://jupyter.org/try)
  - sur votre machine : _la solution à privilégier_
  - en ligne : [google colab](https://colab.research.google.com), [cocalc](https://cocalc.com)
- MTU [Utiliser les notebooks Jupyter](https://moodle.luniversitenumerique.fr/course/view.php?id=1086)
_Utiliser les notebooks Jupyter_
  - première séance  de TD

- [python tutor](http://pythontutor.com) 
  - permet de visualiser l'effet des instructions d'un petit code  
  - très utile au début pour comprendre des _effets de programmation_, pas d'algorithmique
  - complément de l'idle python
  - demo 

- les quizz en ligne (moodle)


## Des points importants

1. Votre guide : la liste des [compétences par chapitre](ch:competences)
2. Un environnement python, similaire sur sa machine perso et en salles info
   1. Installer un environnement python : fortement conseillé en **L1 Informatique**
   2. Utiliser [http://basthon.fr](basthon) : un environnement python très complet basé sur sur les notebooks jupyter  

```{Important}
On conseille d'installer une distribution récente [Anaconda](https://www.anaconda.com/products/individual)  (python $\ge$ 3.11).  
```

Une fois Anaconda installée, vous avez accès à toutes les ressources python nécessaires ce semestre : jupyter, interpréteur python, principaux modules, gestionnaire conda, ... 

Plus de détail [un peu plus loin](#travailler-en-python)

Le web est bien sûr plein de tutos et autres sites explicatifs ...
On peut s'aider des liens ci-après.

- [Un tutoriel](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/)  
- [Un autre](https://www.davidculley.com/installing-python-on-a-mac/) pour mac mais/et en anglais, très complet : le début seul devrait vous suffire.

**Pièges**

- Ne pas confondre ~~`python 2`~~ et `python 3` 


## Pré-requis et programme 

### Acquis du semestre 1 et prérequis 

```{warning}
Vérifiez vos acquisitions en début de semestre 2 !
```

- Savoir différencier les _types_ de données :  
  - type scalaire : booléen, entier, réels, caractères  
  - type composés : chaine de caractères, vecteur, matrice, ...  

- Connaitre leur _représentation_ dans un langage informatique donné  
  - `bool`, `int`, `float`, `str`, `list`  
  - et les changement de types associés : `int()`, `float()`, ...  
  - (python) : un rappel sur le "type" `bool`est proposé en [annexe du cours](./a1-booleens.ipynb).

- Bien différencier _valeur_ vs. _variable_ vs. _constante_  
  - _évaluation_ 
  - et comprendre comment le modèle d'exécution en modifie l'état  
  - _affectation_ : `=`  

- Bien comprendre le modèle _séquentiel_ de l'exécution d'un algorithme   
  - _instruction_   
  - _expression_ ("formule")   

- Comprendre que les structures de contrôle permettent de _casser_ la séquentialité de l'exécution d'un algorithme  
  - branchement conditionnel  : _choisir_   
      - `if ...:`, `elif ...:`,  `else:`  
  - répétitions : _répéter_  
      - `while`  
      - `for . in ...`, (`break`, `continue`)   
  
- Utilisation avancée de boucles et de tableaux
  - boucles imbriquées, indépendantes ou non
  - traitements divers avec des tableaux 1D ou plus
  - _[un chapitre en annexe](ann:boucles) du support de cours du semestre 2 rappelle ces aspects_  
  
- Distinguer : les _entrées_ vs. le _traitement_ vs. la _sortie_  
  - `input()`, `print()`  

- Spécificités python  
  - _indentation_  
  - typage dynamique  

### Programme détaillé des aspects "algorithmique"

- Récursivité : 
  - **la notion centrale du semestre**
  - principes 
  - applications 
  - notions : itératif vs. récursif, pile/arbre des appels, complexité

```{note} 
La récursion s'appuie sur la notion de _fonction_ présentée dans les aspects plutôt programmation.
```

- Rechercher 
  - recherche séquentielle
  - recherche dichotomique 
  - notions : les algos, leurs complexités, (les preuves)   
  - versions itératives ou récursives de ces algorithmes 
  
- Trier 
  - des algorithmes de tris dits naïfs  : algos, complexité, (preuve)   
  - des algorithmes de tris dits rapides : : algos, complexité, (preuve)
  - versions itératives ou récursives de ces algorithmes 

- Complexité
  - combien _coûte_ un algorithme pour résoudre un pb donné ?  
  - combien de temps ? combien de place mémoire ?  
  - tous les problèmes coûtent pareils ?  
  - notions : complexité en temps, pire cas, complexité asymptotique  
  - exemples d'algos plutôt numériques et leurs complexités
    - différentes évaluations de polynômes 

- Compléments si assez de temps : prouver la terminaison et la correction d'un algorithme
  - l'algo fournit la/les solution/s en un temps fini
  - l'algo résout bien le pb
  - notions : invariant de boucle, preuve de terminaison

### Programme détaillé des aspects "programmation" 

#### Rappels de notions du semestre 1

- Tableaux 1D :
  - rappel : avec des listes python (`lst`)
  - exemples du cours : lire, stocker, moyenne/min/max d'un tableau (valeurs, indices)
  - applications : les vecteurs, les chaines de caractères 

- Tableaux 2D, 3D ; application au traitement d'images
  - avec des listes (de listes) python  
  - images et matrices  
  - boucles imbriquées  
  - exemples du cours : 
    - traitement d'images : initialisation niveaux de gris, transformations d'images (miroir, contraste, contours, ...) 
    - algorithmes sur les matrices : vérification (identité, symétrie), calcul (produit de matrices,...) , génération de formes particulières (transposée, ...)

- Fonctions : **une notion centrale** à maitriser 
  - fonctions prédéfinies ou existantes
  - en-tête, corps, appel, paramètres formels et effectifs. 
  - portée, visibilité, variables locales vs. paramètres  

#### Notions du semestre 2

- Fonctions : aspects plus avancés
  - tests unitaires
  - mode de passage des paramètres
  - exemples du cours : doubler, permuter  

- Types de données scalaires et composés
  - approfondissement : introspection  
  - autres types de données composés
    - listes (`lst`) : fonctions et méthodes
    - n-uplets (`tuple`), dictionnaires (`dict`), ensembles (`set`)

- Entrées/sorties et fichiers
  - Très pratique pour tester ses développements : 
  ```{important}
  **Bannir les entrées au clavier !** 
  Plus d'`input()` à tours de bras SVP !!!
  ```
- Modules
  - utilisation de modules existants : `math`
  - exemple d'outils : `numpy`, `matplotlib`, `time` 
  

-   
```{note}
Par manque de temps, les notions suivantes ne sont pas abordés en séance bien que très utiles en pratique.
Des ressources présentées en annexe du support de cours pourront être exploitées de façon autonome par les étudiants (objectif 20) qui le souhaitent.

- `ndarray` de `numpy`
- les exceptions en python
```


(envir-machine)=
## Travailler en python

:::{ATTENTION}
**Problème entre Windows, votre dossier réseau et jupyter en salles informatique**

*Sous windows :*

- jupyter à accès aux dossiers locaux de la machine sur laquelle vous travaillez
- mais jupyter n'a pas directement accès à votre "dossier_réseau".
- Cependant jupyter peut charger un fichier de votre dossier
- 
Que faire si on veut retrouver ses notebook d'une séance à une autre en ayant changé de place en salle informatique ou continuer son travail hors des salles info ?

En début de séance : 

1. enregistrer le notebook jupyter de travail sur la machine locale ("Bureau" par exemple)
2. ouvrir **ce** fichier avec jupyter (via anaconda)
3. enregistrer régulièrement votre travail

En fin de séance 👍

1. enregistrer votre notebook
2. fermer et quitter jupyter
3. par le gestionnaire de fichiers windows, déplacer votre notebook (qui est sur "Bureau) vers votre "dossier_réseau"

Ainsi dans votre "dossier_reseau", votre notebook est enregistré dans l'état où il était sous jupyter.
A la prochaine séance en salle informatique, reprendre les étapes décrites **à partir de ce notebook**. 
:::

Il est indispensable :

- d'avoir accès à un environnement de programmation python, si possible assez complet,

- d'avoir son propre ordinateur configuré de façon complète et selon vos préférences.    

Il y a déjà 3 choix d'OS possibles : windows, linux et mac os ; les 2 premiers étant disponibles sur les ordinateurs de l'UPVD.    

Ensuite, les [distributions python](#distributions-python-classiques) sont assez variées, et peuvent différer selon les OS .

Il est aisé _pour chacun_ de trouver ce qui correspond à ses contraintes matérielles et ses envies.  



### IMPORTANT : De quoi a-t-on *absolument* besoin ?

Ce qui suit est une liste minimale de composants utiles cette année et les années à venir. 
Elle peut sembler longue mais en pratique, ces composants "arrivent" d'un seul coup avec une distribution -- cf. paragraphe suivant.  


- l'`IDLE` python 3  
    - éditeur, interpréteur, débugger utilisé en TP au semestre 1

- `jupyter notebook`  
    - pour intégrer dans _un unique fichier_ du texte, des maths ($\LaTeX$) et du code python qui s'exécute, les résultats de ces executions (valeurs, courbes, images, ...) et exporter tout ça en `html`ou `pdf` ou en `slide`  
    - très utile pour les exercices 
    - _utilisé pour les TP de programmation à rendre_
    - utilisable dans toutes les matières ou presque    
    

- les gestionnaire de paquets (modules) python pour compléter et mettre à jour son environnement
    - `conda`: plus complet si distribution anaconda utilisée (solution recommandée)  
    - `pip` : classique
    - Exemple d'utilisation : 
        - `conda` : `conda list`, `conda install le_module_que_je_veux` et voilà, c'est fini ! 
        - `pip` : pareil `list`, `update`, `install`  

- modules indispensables 
    - `numpy` : fournit des _vrais_ tableaux multi-dimentionnels et des tas de fonctions et types numériques pour effectuer du calcul
    - `matplotlib` : pour le traitement graphique de données, et en particulier :
        -  `matplotlib.pyplot` pour des affichages élaborés
        -  `matplotlib.image`  pour le traitement d'images
    - `tkinter` : pour réaliser des interfaces graphiques  
    
- modules utiles mais optionnels cette année  
    - `scipy` : scientific python qui rassemble des modules de calcul scientifiques (dont `numpy`) 


**Conseil**
- Choisir une distribution la plus complète possible dès le début.   


### Distributions python classiques  

On télécharge, on installe, on travaille !  

- [Anaconda](https://www.anaconda.com/products/individual)  : à privilégier (pour son gestionnaire `conda`) sauf choix perso justifié.  
- [Enthought Python Distribution](http://www.enthought.com/products/epd.php) : très complet  
- [Thonny](https://thonny.org/) Attention : Thonny installe sa propre version de Python par défaut.   
- [Pyzo](http://www.pyzo.org)
- [SAGEMATH](http://sagemath.org/)  : bcp plus général qu'un simple environnement python. A conseiller pour ceux qui veulent continuer en ... mathématiques.


### Que faire en cas de problème avec sa configuration python ...

1. En parler en TD : solution sans garantie de succès tant les configurations de vos ordinateurs peuvent être variées
2. Utiliser le forum moodle de cet UE pour solliciter les autres étudiants de votre promotion : il est probable que vous partagiez une configuration commune
3. **L'unique fois où ce conseil est donné dans ce cours.** Chercher sur les (bons) forums sur internet  (linux, hardware, stack overflow, python.org, ...) 

## Références bibliographiques

### Algo et prog

- Informatique pour tous en CPGE avec Python et nouveaux programmes 2013 : 
    - B. Wack _et al._ (Eyrolles)  
    - Th. Audibert et A. Oussalah. (Ellipses)   
    - E. Le Nagard (Pearson)


L'introduction de la spécialité NSI (Numérique et Science Informatique) a donné l'opportunité de la publication de nombreux ouvrages de niveau Première ou Terminale. Le programme de ces classes étant assez ambitieux, ces ouvrages sont de bonnes premières références, voire de très bonnes pour les étudiant.e.s Objectif 10. 

#### Ellipses

Titre : Spécialité Numérique et sciences informatiques : 30 leçons avec exercices corrigés - Première - Nouveaux programmes
Auteur(s) : Balabonski Thibaut, Conchon Sylvain, Filliâtre Jean-Christophe, Nguyen Kim
Editeur : Ellipses
ISBN : 9782340033641 (Première)
Volume niveau Terminale en préparation.

Titre : Spécialité Numérique et sciences informatiques - Première, , Terminale  - nouveaux programmes
Auteur(s) : Serge Bays (Auteur) Bertrand Hauchecorne (Direction) 
Editeur : Ellipses
Collection	Prepas Sciences
ISBN : 2340031729 (Première), 2340038448 (Terminale)

Titre : Spécialité NSI (numérique et sciences informatiques) - Première - nouveaux programmes
Auteur(s) : Legrand David
Editeur : Ellipses
Collection Parcours et méthodes
ISBN : 9782340038578 (Première),

Spécialité Numérique et sciences informatiques - Première - nouveaux programmes
Cécile Canu (Auteur) 
Editeur : Ellipses
Collection Competences Attendues
ISBN : 2340031788 

Titre : Spécialité NSI - Numérique et sciences informatiques - Terminale - nouveaux programmes
Auteur(s) : Jean-Christophe Bonnefoy (Auteur) Bertrand Petit (Auteur) 
Editeur : Ellipses
Collection Competences Attendues
ISBN :  2340038154 

#### Hatier

Titre : NSI 1ère générale (spécialité) - Prépabac Cours & entraînement. 
Nouveau programme, nouveau bac (2020-2021)
Auteur(s) : Céline Adobet (Auteur) Guillaume Connan (Auteur) Gérard Rozsavolgyi (Auteur) Laurent Signac (Auteur) 
Nouveau programme de Première (2020-2021) 
Editeur : Hatier
Collection	: Prepabac Entrainement Progress
ISBN : 2401052305
Version e-book : 8,99€

Titre : NSI Tle générale (spécialité) - Prépabac Cours & entraînement. 
Nouveau programme, nouveau bac (2020-2021)
Auteur(s) : Guillaume Connan (Auteur) Vojislav Petrov (Auteur) Gérard Rozsavolgyi (Auteur) Laurent Signac (Auteur) 
Editeur : Hatier
Collection	: Prepabac Entrainement Progress
ISBN : 2401064613
Version e-book : 8,99€

#### Nathan

Titre : Interros des Lycées Numérique Sciences Informatiques - Première, Terminale
Auteur(s) :  Stéphane Pasquet (Auteur) MIKAEL LEOPOLDOFF 
Editeur : Nathan
Collection: Interros des Lycées
ISBN : 2091574651 (Première),  2091575437  (Terminale)

### Approfondisssement en algo

- Des petits livres 
    - Cormen
    - Damphousse
    
- Des gros, voire très gros, livres
    - Cormen _et al._
    - Knuth

### Approfondisssement en programmation Python

- poly ou [bouquin](https://www.dunod.com/sciences-techniques/python-3-apprendre-programmer-dans-ecosysteme-python-0) de Cordeau-Pointal (fr)
- le site en anglais [RealPython](https://realpython.com) est de très grande qualité (eng.)
- [ref python 3](https://docs.python.org/3/reference/index.html)  (eng.)


## Conclusion

Bon courage et bon travail ce semestre !  
