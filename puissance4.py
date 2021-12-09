grille = [
    [0,0,0,0,0,0,0],    #
    [0,0,0,0,0,0,0],    #
    [0,0,0,0,0,0,0],    #
    [0,0,0,0,0,0,0],    #---Grille puissance 4
    [0,0,0,0,0,0,0],    #
    [0,0,0,0,0,0,0],    #
]

numCol = int(input('Numéro colonne :')) - 1 #--Ptetr - 1

#--------------------Fonction pour vérifier les bornes max et min de l'input-----------------#
def Verif(numCol):
    if numCol > 7 or numCol < 1:
        return 0
    else:
        return 1
#--------------------------------------------------------------------------------------------#

#--------------------Fonction pour ajouter un pion-----------------#
def Placement(numCol):
    grilleTmp = grille
    for i in range(5 , len(grilleTmp)):
        if grilleTmp[i][numCol] == 0:
            grilleTmp[i][numCol] = 1
            break
        else:
            i-= 1
            break
    return grilleTmp
#------------------------------------------------------------------#

if Verif(numCol) == 1:
    print(Placement(numCol))


