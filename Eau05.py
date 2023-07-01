#~~> MrRøølåÐe <~~#
## String dans string
### programme qui détermine si une chaîne de caractère se trouve dans une autre.
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def research_string_in_string(first_value, second_value):
    for i in range(len(first_value) - len(second_value) +1):
            if second_value == first_value[i: i +len(second_value)]:
                return True
    return False

def quit_program():
    print("error")
    sys.exit()

# Parsing
user_value = sys.argv[1:]
first_value= sys.argv[1]
second_value= sys.argv[-1]
number_of_value = len(sys.argv)
  
# Gestion des erreurs   
if number_of_value ==3 :
    try:
        for value in user_value :
            if value.isdigit() :
                quit_program()
    except (ValueError, IndexError): #si erreur de type de variable
        quit_program()
else:
     quit_program()


# Résolutio
result = research_string_in_string(first_value, second_value)

# Résultat
print(result)