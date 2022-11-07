#Import
from player import *

class game :

    def __init__(self):
        # Variables points
        self.ia_point = 0
        self.human_point = 0
        self.nb_manche = 0

    #Fuction point
    def incre_point(self, bool):
        if(bool):
            self.human_point += 1
        elif(bool != True):
            self.ia_point += 1
    #Fuction nb manche
    def incre_manche(self):
        self.nb_manche += 1
    #Launch fuction
    def launch_game(self):
        print("--------------")
        print("-Début du jeu-")
        print("---Made  by---")
        print("-Les intellos-")
        print("--------------")

    #Fuction test eguality



    #Fuction test win or fail
    def test_win(self, human_choice, ia_choice):
        if(human_choice == "Pierre" and ia_choice == "Ciseau"):
            self.incre_point(True)
            return True
        elif(human_choice == "Feuille" and ia_choice == "Pierre"):
            self.incre_point(True)
            return True
        elif(human_choice == "Ciseau" and ia_choice == "Feuille"):
            self.incre_point(True)
            return True
        else:
            self.incre_point(False)
            return False
    
    #Print current point
    def who_win(self):
        if(self.ia_point == self.human_point):
            print("Égalité !")
        elif(self.ia_point > self.human_point):
            print("L'IA a gagne !")
        else:
            print("Vous avez gagnez !")
        print("L'ia a : " + str(self.ia_point) + "points.")
        print("Et vous avez : " +str(self.human_point) + "points.")   


player_class = player("Leelou")
player2_class = player('bot')
game_class = game()
game_class.launch_game()

while(game_class.nb_manche < 3):
    a = player_class.choice()
    b = player2_class.choice()
    if(a != b):
        game_class.test_win(a, b)
        game_class.who_win()
        print(a)
        print(b)
        game_class.incre_manche()
    else:
        print("Egalité nouvelle manche")
