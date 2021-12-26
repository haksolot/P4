import random

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
    if type(int(numCol)) == str:
        return 1
    elif (int(numCol) > 7 or int(numCol) < 1) == True:
        return 1
    else:
        return 0
#--------------------------------------------------------------------------------------------#

#---------------Fonction changeant la valeur du pion en fonction du tour pour les joueurs--------#
def valeurPion(tour):                                                                          
    if (tour % 2) == 0:                                                                        
        return 200                                                                             
    else:                                                                                      
        return 100                                                                             
#------------------------------------------------------------------------------------------------#

#--------------------Fonction pour ajouter un pion dans la grille-----------------#
def Placement(numCol):
    for i in range(len(grille)-1, -1, -1):
        if grille[i][int(numCol)-1] == 1:
            grille[i][int(numCol)-1] = valeurPion(tour)
            break
    return grille
#---------------------------------------------------------------------------------#

#-------------------------Vérification de victoire horizontale--------------------------#
def verifHoriz(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i][j-1] + grille[i][j-2] + grille[i][j-3])==400:
                return 1
            elif (grille[i][j] + grille[i][j-1] + grille[i][j-2] + grille[i][j-3])==800:
                return 2
#---------------------------------------------------------------------------------------#

#---------------------------Vérification de victoire verticale-----------------------#
def verifVerti(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i-1][j] + grille[i-2][j] + grille[i-3][j])==400:
                return 1
            elif (grille[i][j] + grille[i-1][j] + grille[i-2][j] + grille[i-3][j])==800:
                return 2
#-------------------------------------------------------------------------------------#

#------Vérification d'une victoire par diagonale montante-----#
def verifDiagoM(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i-1][j-1] + grille[i-2][j-2] + grille[i-3][j-3])==400:
                return 1
            elif (grille[i][j] + grille[i-1][j-1] + grille[i-2][j-2] + grille[i-3][j-3])==800:
                return 2
#--------------------------------------------------------------#

#------Vérification d'une victoire par diagonale déscendante-----#
def verifDiagoD(grille):
        for i in range(len(grille)-1, -1, -1):
            for j in range(0, 3, +1):
                if (grille[i][j] + grille[i-1][j+1] + grille[i-2][j+2] + grille[i-3][j+3])==400:
                    return 1
                elif (grille[i][j] + grille[i-1][j+1] + grille[i-2][j+2] + grille[i-3][j+3])==800:
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
    global tour
    plateau = " 1 2 3 4 5 6 7\n _ _ _ _ _ _ _ \n"
    tmp = " "
    for i in range(0, len(grille), +1):
        for j in range(0, len(grille[i]), +1):
            if grille[i][j] == 1:
                tmp = " "
            elif  grille[i][j] == 100:
                tmp = "O"
            elif  grille[i][j] == 200:
                tmp = "X"
            plateau = plateau[0:len(plateau)] + "|" + tmp
            if j == len(grille[i])-1:
                plateau = plateau[0:len(plateau)] + "|\n"

    if tour % 2 == 0:                                                                        
        plateau = plateau[0:len(plateau)] + "\n\nJoueur 2"                                                                             
    else:                                                                                      
        plateau = plateau[0:len(plateau)] + "\n\nJoueur 1"
    return plateau
#-----------------------------------------------------------#
def modeMenu():
        global mode
        mode = int(input('1 - 2 Players\n2 - 1 Player + Bot\n3 - Bot only\n\nMode :'))
        if mode > 3 or mode < 1:
            mode = 0
            print("Cette option n'existe pas ! Veuillez choisir une option valide")
            return 0
        else: 
            return 1


def mode1():
    global win
    while win == 0:
        global tour
        global grille
        

        print(affichage(grille))
        
        numCol = input('Numéro colonne :')

        if verifBornes(numCol) == 1:
            print("Ce numéro n'est pas compris dans la grille")
            tour -= 1
        else:
            grille = Placement(numCol)
            print(affichage(grille))

        if verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille)) != 0:
            print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille))), "gagne !")
            win = 1
            break

        else:
            tour += 1
            break


win = 0
mode = 0
tour = 1

while win == 0:
    if mode == 0:
        while modeMenu() == 0:
            if mode == 0:
                modeMenu()
            if mode != 0:
                break
    if mode == 1:
        mode1()








