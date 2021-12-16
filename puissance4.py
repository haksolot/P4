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
    if (numCol > 7 or numCol < 0) == True:
        return 1
    else:
        return 0
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
        if grille[i][numCol-1] == 1:
            grille[i][numCol-1] = valeurPion(tour)
            break
    return grille
#---------------------------------------------------------------------------------#

#-------------------------Vérification de victoire horizontale--------------------------#
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

#------Vérification d'une victoire par diagonale montante-----#
def verifDiagoM(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i-1][j-1] + grille[i-2][j-2] + grille[i-3][j-3])==40:
                return 1
            elif (grille[i][j] + grille[i-1][j-1] + grille[i-2][j-2] + grille[i-3][j-3])==80:
                return 2
#--------------------------------------------------------------#

#------Vérification d'une victoire par diagonale déscendante-----#
def verifDiagoD(grille):
        for i in range(len(grille)-1, -1, -1):
            for j in range(0, 3, +1):
                if (grille[i][j] + grille[i-1][j+1] + grille[i-2][j+2] + grille[i-3][j+3])==40:
                    return 1
                elif (grille[i][j] + grille[i-1][j+1] + grille[i-2][j+2] + grille[i-3][j+3])==80:
                    return 2
#-----------------------------------------------------------------#


#----------------------------Vérification Win----------------------#
def verifWin(horiz, verti, diagoM, diagoD):
    if horiz != None:
        return horiz
    elif verti != None:
        return verti
    elif diagoM != None:
        return diagoM
    elif diagoD != None:
        return diagoD
    else:
        return 0
#-------------------------------------------------------------------#

#--------------- Afiche les pions dans le cadriage----------#
def affichage(grille):
    plateau = " 1 2 3 4 5 6 7\n _ _ _ _ _ _ _ \n"
    tmp = " "
    for i in range(0, len(grille), +1):
        for j in range(0, len(grille[i]), +1):
            if grille[i][j] == 1:
                tmp = " "
            elif  grille[i][j] == 10:
                tmp = "¤"
            elif  grille[i][j] == 20:
                tmp = "@"
            plateau = plateau[0:len(plateau)] + "|" + tmp
            if j == len(grille[i])-1:
                plateau = plateau[0:len(plateau)] + "|\n"
    return plateau
#-----------------------------------------------------------#

tour = 1
win = 0

while win == 0:

    numCol = int(input('Numéro colonne :'))

    if verifBornes(numCol) == 1:
        print("Ce numéro n'est pas compris dans la grille")
        tour -= 1
    else:
        grille = Placement(numCol)
        print(affichage(grille))


    if verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille)) != 0:
        print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille))), "gagne !")
        break

    tour += 1

