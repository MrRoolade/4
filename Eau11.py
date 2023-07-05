#~~> MrRøølåÐe <~~#
## Différence minimum absolue 
### un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres.
#### Nombres négatifs acceptés.
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def difference_absolute(user_value):
    array_difference = []
    difference = 0
    for i in range(len(user_value)):
        for j in range(i+1,len(user_value)):
            difference = int(user_value[i]) - int(user_value[j])
            if difference < 0 :
                 difference *= -1
            array_difference.append(difference)
    return array_difference

def find_mini(array_difference):
     mini_value = array_difference[0]
     for i in range (1,len(array_difference)):
          if array_difference[i] < mini_value:
               mini_value = array_difference[i]
     return mini_value
                 
def quit_program():
    print("error")
    sys.exit()

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
array_difference = difference_absolute(user_value)
result = find_mini(array_difference)

# Résultat
print(result)