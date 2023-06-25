#~> MrRøølåÐe <~#
## ARGUMENTS à L'ENVERS
## 
import sys

# verif_digit = False    #si les arguments doivent etre que des chiffres
Nbre_Arg = len(sys.argv)

if Nbre_Arg > 1:

    # verif_digit = any(arg.isdigit() for arg in sys.argv)      #si les arguments doivent etre que des chiffres

    # if not verif_digit:                                       #si les arguments doivent etre que des chiffres

        for i in range(Nbre_Arg-1,0,-1):
            if sys.argv != sys.argv[0]: 
                print(sys.argv[i])

    # else :                                                    #si les arguments doivent etre que des chiffres
        # print("error")
else :
    print("error")