#~~> MrRøølåÐe <~~#
## chiffre only 
### un programme qui détermine si une chaîne de caractères ne contient que des chiffres. 
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def only_digits():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(i_value)):
        if i_value[i] not in numbers:
            return False
    return True
        
def quit_program():
    print("error")
    sys.exit()

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
i_value = list(" ".join(user_value))
  
# Gestion des erreurs 
try:
    number_of_value > 1
except (ValueError, IndexError):
        quit_program()

# Résolution
result = only_digits()

# Résultat
print(result) 