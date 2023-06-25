##<~~MrRøølåÐe~~>
## Combinaisons de 2 chiffres
## affiche toutes les combinaisons possible de 2 nombres entre 00 et 99 dans l'ordre croissant.

## Variables Import et Fonction
n = 100 # définit l'interval pour l'affichage des chiffres

# ci dessous 2 boucles imbriquées
# la premiere itère x jusqu'à 99
# la deuxième itère y de x jusqu'à 99; si y = x on saute le chiffre sinon on affiche la combinaison
for x in range(n) :
    for y in range(x,n) :
        if y == x :
            pass
        else :
            print (f"{x:02d} {y:02d},",end=" ") #affiche la combinaison des chiffres avec 2 digits
#FIN