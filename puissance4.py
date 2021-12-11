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

#---------------------------Vérification de victoire verticale-----------------------#
def verifVerti(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i-1][j] + grille[i-2][j] + grille[i-3][j])==40:
                return 1
            elif (grille[i][j] + grille[i-1][j] + grille[i-2][j] + grille[i-3][j])==80:
                return 2
#-------------------------------------------------------------------------------------#

#----------------------------Vérification Win----------------------#
def verifWin(horiz, verti, diago):
    if horiz != None:
        return horiz
    elif verti != None:
        return verti
    elif diago != None:
        return diago
    else:
        return 0
#-------------------------------------------------------------------#

#--------------------Vérification de victoire diagonale----------#
#   Rien pour le moment 
#----------------------------------------------------------------#
tour = 1
win = 0
while win == 0:

    numCol = int(input('Numéro colonne :')) - 1 

    if verifBornes(numCol) == 1:
        print(Placement(numCol))

    if verifWin(verifHoriz(grille), verifVerti(grille), fonctiondiagonal) != 0:
        print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), fonctiondiagonal)), "gagne !")
        break

    tour += 1

