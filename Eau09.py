#~~> MrRøølåÐe <~~#
## Entre min et max 
### un programme programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def between_min_max(i_value):
    if i_value[0]>i_value[-1]:
        limit_down, limit_up = int(i_value[-1]) , int(i_value[0])
    else:
        limit_down, limit_up = int(i_value[0]) ,int(i_value[-1])
    return limit_down, limit_up

def between_function(limit_down,limit_up):
    value_between =[]
    for i in range(limit_up-limit_down):
        value_between.append(str(limit_down)+" ")
        limit_down += 1
    return value_between
      
def quit_program():
    print("error")
    sys.exit()

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
i_value = list(user_value)
  
# Gestion des erreurs 
try:
   if number_of_value != 3 :
        raise ValueError
   for value in user_value:
        if value.isdigit() == False:
            raise ValueError
except (ValueError, IndexError):
        quit_program()

# Résolution
limit_down, limit_up = between_min_max(i_value)
result = between_function(limit_down, limit_up)

# Résultat
print("".join(result))