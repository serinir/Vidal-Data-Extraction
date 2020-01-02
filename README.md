# Projet python (tout le projet doit etre mis dans le dossier French d'Unitex GramLab)

## app.py
`app.py` lance le serveur en localhost port a definire la commande est :
```bash
    $ app.py <port>
```
## scraper.py NORMALEMENT aspirer.py  intervalle port 
Genere: 
- subst.dic (tous les medicaments de l'intervalle, par lettre alphabetique(triés), trouvés dans les 26 pages Vidal)
Format : <nomMedicament>,. N+Subst 
ex: abacavir,.N+subst 
    abatacept,.N+subst
    
- info.txt (contient le nombre de medicaments trouvés, par lettre alphabetique + le nombre total des medicaments trouvés toute lettre confondue)
Format : <lettre>: entier
          Total : entier
ex : A : 26 
     B : 20
   Total: 46

## enrichir.py  corpus-medical.txt
Modifie : subst.dic (il ajoute les medicaments trouvés dans corpus-medical.txt , trié et sans doublons ) 
(doit conserver son encodage de départ, à savoir « UTF-16 LE avec BOM » (UCS-2 LE BOM)).

Genere: 
- subst_enri.dic (tous les medicaments de corpus-medical.txt sans les trier, ni supprimer les doublons) 
Format : <nomMedicament>,. N+Subst 
ex: zellouch,.N+subst 
    abatacept,.N+subst
Les médicaments issus de l’enrichissement doivent également être affichés sur la console, avec un compteur commençant à 1.
    
- infos2.txt (contient les informations concernant les medicaments de corpus-medical.txt () 
le nombre de médicaments issus de l’enrichissement pour chaque lettre de l’alphabet 
le nombre total de médicaments issus de l’enrichissement.

Format : <lettre>: entier
          Total : entier
ex : A : 26 
     B : 20
   Total: 46

## unitex.py 
 script qui appelle unitex. 
Pour pouvoir unitliser UnitexToolLogger, il faut copier Unitex-GramLab\App UnitexToolLogger.exe dans Unitex-GramLab\French

## posologie.grf 
Graphe sous unitex, qui extrait les occurrences de posologies de traitement à partir de corpus-medical.txt.
Le resultat doi etre placé dans concord.html qui se trouve dans corpus-medical_snt. 
