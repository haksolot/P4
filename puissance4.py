grille = [
    [1,1,1,1,1,1,1],    #
    [1,1,1,1,1,1,1],    #
    [1,1,1,1,1,1,1],    #
    [1,1,1,1,1,1,1],    #---Grille puissance 4
    [1,1,1,1,1,1,1],    #
    [1,1,1,1,1,1,1],    #
]

#--------------------Fonction pour vérifier les bornes max et min de l'input-----------------#
def verifBornes(numCol):
    if numCol > 7 or numCol < 0:
        return 0
    else:
        return 1
#--------------------------------------------------------------------------------------------#

#---------------Fonction changeant la valeur du pion en fonction du tour pour les joueurs--------#
def valeurPion(tour):                                                                          
    if (tour % 2) == 0:                                                                        
        return 20                                                                             
    else:                                                                                      
        return 10                                                                             
#------------------------------------------------------------------------------------------------#

#--------------------Fonction pour ajouter un pion dans la grille-----------------#
def Placement(numCol):
    for i in range(len(grille)-1, -1, -1):
        if grille[i][numCol] == 1:
            grille[i][numCol] = valeurPion(tour)
            break
    return grille
#---------------------------------------------------------------------------------#

#-------------------------Vérification de vistoire horizontale--------------------------#
def verifHoriz(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i][j-1] + grille[i][j-2] + grille[i][j-3])==40:
                return 1
            elif (grille[i][j] + grille[i][j-1] + grille[i][j-2] + grille[i][j-3])==80:
                return 2
#---------------------------------------------------------------------------------------#

tour = 1
win = 0
while win == 0:

    numCol = int(input('Numéro colonne :')) - 1 

    if verifBornes(numCol) == 1:
        print(Placement(numCol))

    if verifHoriz(grille)!= None:
        print("Le joueur", str(verifHoriz(grille)), "gagne !")
        break
    
    tour += 1

