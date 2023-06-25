## 
## affiche la transformation d'une heure affichée en format 24h en une heure affichée en format 12h

## Variables Import et Fonction
n = 100

for x in range(n) :
    for y in range(x,n) :
        if y == x :
            pass
        else :
            print (f"{x:02d} {y:02d},",end=" ")
#FIN