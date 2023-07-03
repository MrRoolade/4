#~~> MrRøølåÐe <~~#
## Majuscule sur 2
### programme qui met en majuscule une lettre sur deux d’une chaîne de caractères.
#### Seule les lettres (A-Z, a-z) sont prises en compte..
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Fonctions
def upper_case_one_letter_on_two():
    counter = 0
    for i in range(len(i_value)):
        if i_value[i].isalpha():
            counter += 1
            if counter % 2 != 0 : 	
                i_value[i] = i_value[i].upper()
            else:	
                i_value[i] = i_value[i].lower()
    return "".join(i_value) 
            
def quit_program():
    print("error")
    sys.exit()

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
i_value =list(" ".join(user_value))
  
# Gestion des erreurs   
if number_of_value >1:
    try:
        for value in user_value :
            if value.isdigit() :
                quit_program()
    except (ValueError, IndexError): #si erreur de type de variable
        quit_program()
else:
    quit_program()
    
# Résolution
result = upper_case_one_letter_on_two()

# Résultat
print(result) 