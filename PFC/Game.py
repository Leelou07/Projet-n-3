#Import
from Ia import *

class game :

    def __init__(self):
        # Variables points
        self.ia_point = 0
        self.human_point = 0
        self.nb_manche = 0
        self.choices_manche = [1, 3, 5, 7, 9]
        self.choix_nbr_manche = self.__choix()
        

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

    #Choix du nombre de manche
    def __choix(self):
        print("En combien de manche souhaitez vous jouer ?")
        answer = input(self.choices_manche)
        print("Vous souhaitez jouer en", answer, "?")
        answer_verif = input("O/N")
        
        if answer_verif == "O" :
            return answer 
        else : 
            self._choix()





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

while(game_class.nb_manche < int(game_class.choix_nbr_manche)):
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
