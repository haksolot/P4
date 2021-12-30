import random   #  Librairie pour générer des nombres aléatoire en guise de choix du bot
import time     #  Librairie pour générer une latence afin d'afficher un message brefement ou allonger le temps de réponse d'un bot


#----------------------------------------------------# Génère la grille de jeu avec 6 de hauteur par défaut
nbCol = 6
grille = []
for i in range(nbCol):
    grille.append([1,1,1,1,1,1,1],)
#----------------------------------------------------#

# Cette fonction vérifie:
    # Que l'input de l'utilisateur soit bien un nombre
    # Qu'il soit bien compris entre 1 et 7 (largeur de la grille)
    # Qu'il ne choisie pas une colonne déjà pleine
# Si il y'a une erreur elle renvoie 1 en guise d'erreur 
def verifBornes(numCol):
    try:
        if (int(numCol) > 7 or int(numCol) < 1) == True or not grille[0][int(numCol)-1] == 1:
            return 1
        else:
            return 0
    except ValueError:
        return 1

# Cette fonction génère la valeur du pion du joueur actuel
def valeurPion(tour):                                                                          
    if (tour % 2) == 0:                                                                        
        return 200                                                                             
    else:                                                                                      
        return 100                                                                             

# Place le pion du joueur actuel dans la grille
def Placement(numCol):
    global tour
    for i in range(len(grille)-1, -1, -1):
        if grille[i][int(numCol)-1] == 1:
            grille[i][int(numCol)-1] = valeurPion(tour)
            break
    return grille

# Vérifie la victoire horizontale d'un joueur (quand 4 pions sont alignés horizontalement)
    # Renvoie le numéro du gagnant
def verifHoriz(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i][j-1] + grille[i][j-2] + grille[i][j-3])==400:
                return 1
            elif (grille[i][j] + grille[i][j-1] + grille[i][j-2] + grille[i][j-3])==800:
                return 2

# Vérifie la victoire verticale d'un joueur (quand 4 pions sont alignés verticalement)
    # Renvoie le numéro du gagnant
def verifVerti(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i-1][j] + grille[i-2][j] + grille[i-3][j])==400:
                return 1
            elif (grille[i][j] + grille[i-1][j] + grille[i-2][j] + grille[i-3][j])==800:
                return 2

# Vérifie la victoire en diagonale montante d'un joueur (quand 4 pions sont alignés en diagonale montante)
    # Renvoie le numéro du gagnant
def verifDiagoM(grille):
    for i in range(len(grille)-1, -1, -1):
        for j in range(len(grille[i])-1, -1, -1):
            if (grille[i][j] + grille[i-1][j-1] + grille[i-2][j-2] + grille[i-3][j-3])==400:
                return 1
            elif (grille[i][j] + grille[i-1][j-1] + grille[i-2][j-2] + grille[i-3][j-3])==800:
                return 2

# Vérifie la victoire en diagonale déscendante d'un joueur (quand 4 pions sont alignés en diagonale déscendante)
    # Renvoie le numéro du gagnant
def verifDiagoD(grille):
        for i in range(len(grille)-1, -1, -1):
            for j in range(0, 3, +1):
                if (grille[i][j] + grille[i-1][j+1] + grille[i-2][j+2] + grille[i-3][j+3])==400:
                    return 1
                elif (grille[i][j] + grille[i-1][j+1] + grille[i-2][j+2] + grille[i-3][j+3])==800:
                    return 2

# Cette fonction regroupe toute les fonctions précedentes de vérification de victoire pour n'en faire qu'une
    # Renvoie le numéro du gagnant ou 0 si pas de victoire
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

# S'occupe de l'affichage en console de la grille et des tours de joueurs
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

# Affichage du menu permettant la selection du mode ou de la configuration
def modeMenu():
        global mode
        print('\033c')
        print("><<<<<<<              \n><<    ><<      ><<   \n><<    ><<    > ><<   \n><<<<<<<     >< ><<   \n><<        ><<  ><<   \n><<       ><<<< >< ><<\n><<             ><<   \n")
        try:
            mode = int(input('1 - 2 Players\n2 - 1 Player + Bot\n3 - Bot only\n4 - Config (default 6)\n\nMode :'))
            if mode > 4 or mode < 1:
                mode = 0
                print("Cette option n'existe pas ! Veuillez choisir une option valide")
                time.sleep(1)
                return 0
            else: 
                return 1
        except ValueError:
            print("Cette option n'existe pas ! Veuillez choisir une option valide")
            time.sleep(1)
            return 0

# Mode de jeu ou 2 joueurs (humain) s'affrontent
def mode1():
    global win
    while win == 0:
        global tour
        global grille
        
        print('\033c')
        print(affichage(grille))
        
        numCol = input('Numéro colonne :')

        if verifBornes(numCol) == 1:
            print("Ce numéro n'est pas compris dans la grille")
            time.sleep(1)
            tour -= 1
        else:
            grille = Placement(numCol)
            print('\033c')
            print(affichage(grille))

        if verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille)) != 0:
            print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille))), "gagne !")
            win = 1
            break

        else:
            tour += 1
            break

# Mode de jeu ou un humain et un bot s'affrontent
def mode2():
    global win
    while win == 0:
        global tour
        global grille
        
        print('\033c')
        print(affichage(grille))
        
        if tour % 2 == 1: 
            numCol = random.randrange(1,7)
            grille = Placement(numCol)
            time.sleep(2)
            print('\033c')
            print(affichage(grille))
            if verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille)) != 0:
                print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille))), "gagne !")
                win = 1
                break
            else:
                tour += 1
                break

        numCol = input('Numéro colonne :')

        if verifBornes(numCol) == 1:
            print("Ce numéro n'est pas compris dans la grille")
            time.sleep(1)
            tour -= 1
        else:
            grille = Placement(numCol)
            print('\033c')
            print(affichage(grille))

        if verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille)) != 0:
            print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille))), "gagne !")
            win = 1
            break

        else:
            tour += 1
            break
# Mode de jeu ou deux bot s'affrontent
def mode3():
    global win
    while win == 0:
        global tour
        global grille
        print('\033c')
        print(affichage(grille))
        numCol = random.randrange(1,7)
        while verifBornes(numCol) == 1:
            numCol = random.randrange(1,7)
        grille = Placement(numCol)
        time.sleep(2)
        print('\033c')
        print(affichage(grille))
        if verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille)) != 0:
            print("Le joueur", str(verifWin(verifHoriz(grille), verifVerti(grille), verifDiagoM(grille), verifDiagoD(grille))), "gagne !")
            win = 1
            break
        else:
            tour += 1
            break

# Configuration de la hauteur de grille
def config():
    global nbCol
    global grille
    print('\033c')
    nbCol = int(input("Hauteur des colonnes: "))
    grille = []
    for i in range(nbCol):
        grille.append([1,1,1,1,1,1,1],)


#--------------------------------------# Partie principale gérant la sélection des modes de jeu
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
    elif mode == 2:
        mode2()
    elif mode == 3:
        mode3()
    elif mode == 4:
        config()
        mode = 0
#--------------------------------------#







