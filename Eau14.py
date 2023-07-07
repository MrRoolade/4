#~~> MrRøølåÐe <~~#
## Par ordre Ascii
### un programme qui qui trie les éléments donnés en argument par ordre ASCII
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def my_selection_sort_by_ord(user_value):
    for i in range(len(user_value) - 1):
        min_index = i
        for j in range(i + 1, len(user_value)):
            for k in range(len(user_value[min_index])):
                if k >= len(user_value[j]):
                    break
                if ord(user_value[j][k].lower()) < ord(user_value[min_index][k].lower()):
                    min_index = j
                    break
                elif ord(user_value[j][k].lower()) > ord(user_value[min_index][k].lower()):
                    break
            else:
                if len(user_value[j]) < len(user_value[min_index]):
                    min_index = j

        user_value[i], user_value[min_index] = user_value[min_index], user_value[i]
    return user_value

# Fonctions sans utiliser la methode ord()
# def my_selection_sort(user_value):
#     for i in range(len(user_value)-1):
#         position_min = i
#         for j in range(i+1, len(user_value)):
#             if  user_value[position_min] > user_value[j]:
#                 position_min = j
#         temp = user_value[i]
#         user_value[i]= user_value[position_min]
#         user_value[position_min] = temp
#     return  user_value
                 
def quit_program():
    sys.exit("error")

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
  
# Gestion des erreurs 
try:
   if number_of_value <= 2 :
        raise ValueError
except (ValueError, IndexError):
        quit_program()

# Résolution
# result = my_selection_sort(user_value)
result_by_ord = my_selection_sort_by_ord(user_value)

# Résultat
# print(" ".join(result))
print(" ".join(result_by_ord))