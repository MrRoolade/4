#~~> MrRøølåÐe <~~#
## la suite de Fibonacci
### programme qui affiche le N-ème élément de la célèbre suite de Fibonacci.
#### Affiche -1 si le paramètre est négatif ou mauvais.

import sys

# Fonction
def function_fibonacci(n):
    n = int(n)
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else:
        return  function_fibonacci(n-1) + function_fibonacci(n-2)
    
def sortie_prog():
    print("-1")
    exit()

# Parsing
Nbre_Arg = len(sys.argv)
fibonacci = []
x = 0
  
# Gestion des erreurs   
if Nbre_Arg ==2  :
    try:
        x = int(sys.argv[1])
        sys.argv[1].isdigit()

    except ValueError:
        sortie_prog()
        
    except IndexError:
        sortie_prog()
else:
    sortie_prog()

# Résolution
for x in range(0,x+1):
    fibonacci.append(function_fibonacci(x))

# Résultat
print(fibonacci[x])