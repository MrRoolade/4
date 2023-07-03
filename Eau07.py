#~~> MrRøølåÐe <~~#
## Majuscule
### programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules.
#### Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def upper_case_the_first_letter():
    for i in range(len(i_value)):
        if i_value[i] not in [' ', '\t', '\n']:
            if i == 0 or i_value[i-1] in [' ','\t', '\n']:	
                i_value[i] = i_value[i].upper()     
            else :
                i_value[i] = i_value[i].lower()       
    return "".join(i_value) 
        
def quit_program():
    print("error")
    sys.exit()

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
i_value = list(" ".join(user_value))
  
# Gestion des erreurs 
if number_of_value >1:  
    try:
      for value in user_value :
        if value.isdigit() :
            quit_program()
    except (ValueError, IndexError):
        quit_program()
else :
    quit_program()

# Résolution
result = upper_case_the_first_letter()

# Résultat
print(result) 