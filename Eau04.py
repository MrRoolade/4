#~~> MrRøølåÐe <~~#
## Prochain nombre premier
### programme qui affiche le premier nombre premier supérieur au nombre donné en argument.
#### Affiche -1 si le paramètre est négatif ou mauvais.

import sys

# Fonctions
def is_prime(n):
    for x in range(2, n-1) :
        if n % x == 0 :  
            return(False)
    return (True)

def next_prime_number(user_value):
    n = user_value + 1
    while not is_prime(n) :
        n += 1
    return(n)

def quit_program():
    print("-1")
    sys.exit()

# Parsing
user_value = sys.argv[1]
number_of_value = len(sys.argv)
  
# Gestion des erreurs   
if number_of_value == 2 :
    try:
        user_value = int(user_value)
        if user_value <= 0 :
            quit_program()
    except (ValueError, IndexError): #si erreur de type de variable
        quit_program()
else:
    quit_program()

# Résolution
result = next_prime_number(user_value)

# Résultat
print(result)