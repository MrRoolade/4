#~~> MrRøølåÐe <~~#
## la suite de Fibonacci
### programme qui affiche le N-ème élément de la célèbre suite de Fibonacci.
#### Affiche -1 si le paramètre est négatif ou mauvais.

import sys
fibonacci = []

def function_fibonacci(n):
    n = int(n)
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else:
        return  function_fibonacci(n-1) + function_fibonacci(n-2)
    
if len(sys.argv) ==2  :

    try:
        x = int(sys.argv[1])
        if sys.argv[1].isdigit():

            for x in range(0,x+1):
                fibonacci.append(function_fibonacci(x))

            print(fibonacci[x])

    except ValueError:
        print("-1")

    except IndexError:
        print("-1")
else:
    print("-1")

#~~> MrRøølåÐe <~~#
