#~> MrRøølåÐe <~#
## ARGUMENTS à L'ENVERS
## programme qui affiche ses arguments reçus à l’envers

import sys

# Fonction
def invert_arg() :
     for i in range(Nbre_Arg-1,0,-1):
            if sys.argv != sys.argv[0]: 
                new_array.append(sys.argv[i])
    
# Parsing
Nbre_Arg = len(sys.argv)
new_array =[]

# Gestion des erreurs
if Nbre_Arg <= 1:
    print("error")
    
# Résolution
invert_arg()

# Résultat
for i in range(Nbre_Arg-1):
    print(new_array[i])