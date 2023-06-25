## <~~MrRøølåÐe~~>
## Combinaisons de 3 chiffres
## affiche toutes les combinaisons possible de 3 chiffres dans l'ordre croissant, dans l'ordre croissant. (la répétition est volontaire)

## Variables Import et Fonction
n = 10
n = 10  # définit l'interval pour l'affichage des chiffres

## ci dessous 3 boucles imbriquées 
# la première itère x de 0 à 9
# la deuxième itère y de x à 9; si y = x  on zappe le chiffre sinon on continue sur la troisième boucle
# la troisième itère z de y à 9; si z =x ou z = y on zappe le chiffre sinon on affiche la combinaison

for x in range(n) :
    for y in range(x,n) :
        if y == x :
            pass
        else :
            for z in range(y,n):
                if z == y or z == x :
                    pass
                else:
                    print (f"{x}{y}{z}",end=" ")
#FIN