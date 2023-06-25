## 
## affiche la transformation d'une heure affichée en format 24h en une heure affichée en format 12h

## Variables Import et Fonction
n = 10

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