#~~> MrRøølåÐe <~~#
## Eau : ok
### un programme qui célèbre !!!

import sys

# Fonctions             
def quit_program():
    sys.exit("error")

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
result = input("comment avez vous trouvé les épreuves de l'eau ? : ") 

# Gestion des erreurs 
try:
    if result.isdigit() :
        raise ValueError    
except (ValueError, IndexError):
        quit_program()

# Résultat
print(f'J\'ai terminé l\'Épreuve de l\'Eau et c\'était {result}')

for i in range(10):
    x=10-i
    print(f'Eau'*i, end="")
    print(f'{result}'*x)

