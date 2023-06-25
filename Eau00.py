
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