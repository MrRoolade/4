#~~> MrRøølåÐe <~~#
## Index wanted 
### un programme qui affiche le premier index d’un élément recherché dans un tableau.
#### Le tableau est constitué de tous les arguments sauf le dernier.
##### L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.
###### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def find_index(i_value,search_value):
      for i in range(len(i_value)):
        if i_value[i] == search_value :
             index_value = i
             return index_value
      
def quit_program():
    print("error")
    sys.exit()

# Parsing
user_value = sys.argv[1:-1]
search_value = sys.argv[-1]
number_of_value = len(sys.argv)
i_value = list(user_value)
  
# Gestion des erreurs 
try:
   if number_of_value <= 2 :
        raise ValueError
   for value in user_value:
        if value.isdigit():
            raise ValueError
except (ValueError, IndexError):
        quit_program()

# Résolution
# limit_down, limit_up = between_min_max(i_value)
result = find_index(i_value,search_value)

# Résultat
print(user_value)
print(search_value)
print(i_value)
print(i_value.index(search_value))
print(result)