#~~> MrRøølåÐe <~~#
## Tri par sélection
### un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def my_selection_sort(user_value):
    # user_value_sort = user_value
    for i in range(len(user_value)-1):
        position_min = i
        for j in range(i+1, len(user_value)):
            if  int(user_value[position_min]) > int(user_value[j]):
                position_min = j
        temp = user_value[i]
        user_value[i]= user_value[position_min]
        user_value[position_min] = temp
    # user_value = user_value_sort
    return  user_value
                 
def quit_program():
    # print("error")
    sys.exit("error")

# Parsing
    user_value = sys.argv[1:]
number_of_value = len(sys.argv)
  
# Gestion des erreurs 
try:
   if number_of_value <= 2 :
        raise ValueError
   for value in user_value:
        if not (value.isdigit() or value.startswith('-') ):
            raise ValueError
except (ValueError, IndexError):
        quit_program()

# Résolution
result = my_selection_sort(user_value)

# Résultat
print(" ".join(result))