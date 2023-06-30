#~~> MrRøølåÐe <~~#
## la suite de Fibonacci
### programme qui affiche le premier nombre premier supérieur au nombre donné en argument.
#### Affiche -1 si le paramètre est négatif ou mauvais.

import sys

# Fonction
def next_prime_number(user_value):
    n = user_value
    reste_division = []
    for x in range(2, n-1) :            # boucle sur l'interval de nombre entre 2 et la saisie -1
                reste = n % x           #affecte le résulat de l'opération '%' dans la variable 'reste'
                reste_division.append(reste) #enregistre reste dans la liste reste_division

    if reste_division.count(0) != 0 :  
    # teste la presence du chiffre zero dans la liste ou si la saisie est 0 ou 1
        return(False)
    else :
        return (True)

def sortie_prog():
    print("-1")
    sys.exit()

# Parsing
user_value = sys.argv[1]
number_of_value = len(sys.argv)
x = 0
n = 0
  
# Gestion des erreurs   
if number_of_value == 2 :
    try:
        user_value.isdigit()
        user_value = int(user_value) +1

        user_value != 0
        user_value != 1
        user_value < 0 # teste si l'argument est négatif

    except (ValueError, IndexError): #si erreur de type de variable
        sortie_prog()
else:
    sortie_prog()

# Résolution
while next_prime_number(user_value) is False:
     user_value += 1 

# Résultat
print(user_value)