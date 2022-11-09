from Player import *
from Ia import *
#Création de la classe
class Game :
    '''
    Variable
        self.player_1_point -> Number of point of player 1
        self.player_2_point -> Number of point of player 2
        self.round_nb -> Number of actual round
        self.choices_round -> list of selection of the number of round
        self.choices_nb_round -> Selection of the number of rounds
    '''
    def __init__(self):
        #Variable int
        self.player_1_point = 0
        self.player_2_point = 0
        self.round_nb = 0
        #List
        self.choices_round = [1, 3, 5, 7, 9]
        self.choices_nb_round = int(self.__round_choices())
        
        
    #Point incrementation
    def __add_point(self, bool):
        if(bool): #If true
            self.player_1_point += 1
        elif(bool != True): #If false
            self.player_2_point += 1
    
    #Round incrementation
    def __add_rounds(self):
        self.round_nb += 1
    
    #Launch game
    def __launch_game(self):
        print("--------------")
        print("-Début du jeu-")
        print("---Made  by---")
        print("-Les intellos-")
        print("--------------")

    #Choice of the number of round
    def __round_choices(self):
        #Print list
        for i in range(4):
            print(str(self.choices_round[i]) + " ", end='') # end='' print in one line
        
        #Select of number of round
        print("")
        print("En combien de manche souhaitez vous jouer ?")
        answer = input()

        #Verification of the choice
        if self.__verification_round_choice(answer) != True:
            print("Réponse incorrecte !")
            self.__round_choices()
        
        #Verification of the user choice
        print("Vous souhaitez jouer en", answer, "?")
        answer_verif = input("O/N : ")

        #Verification of the answer
        if answer_verif == "O" :
            return answer 
        else : 
            if answer_verif != "N" :
                print("Réponse invalide")
            self.__round_choices()

    #Verification of the choice of round
    def __verification_round_choice(self, answer):
        answer = int(answer) # Convert String in int
        for i in range(4):
            #Verification of the answer in the list of choice possibility
            if answer == self.choices_round[i]: 
                return True
        return False    

    #Fuction test win or fail
    def __test_win(self):
        #Player1 win
        if(player_class.player_1_stroke == "Pierre" and player_class.player_2_stroke == "Ciseau"):
            self.__add_point(True) #Incrementation of the point of player1
            return True
        elif(player_class.player_1_stroke == "Feuille" and player_class.player_2_stroke == "Pierre"):
            self.__add_point(True) #Incrementation of the point of player1
            return True
        elif(player_class.player_1_stroke == "Ciseau" and player_class.player_2_stroke == "Feuille"):
            self.__add_point(True) #Incrementation of the point of player1
            return True
        #Player2 win
        else:
            self.__add_point(False) #Incrementation of the point of player2
            return False

    #Print who win the game
    def __who_win(self):
        if(self.player_2_point == self.player_1_point):
            print("Égalité !")
        elif(self.player_2_point > self.player_1_point):
            print(player_class.player_2_name + " à gagné la partie !")
        else:
            print(player_class.player_1_name + " à gagné la partie !")
        print(player_class.player_2_name + " a " + str(self.player_2_point) + " point(s).")
        print(player_class.player_1_name + " a " + str(self.player_1_point) + " point(s).")   

        

    def game(self):
        i = 0
        self.__launch_game()
        while(i < self.choices_nb_round):
            player_class.player()
            print("GAME")
            if self.__test_win() :
                print(player_class.player_1_name + " à gagné la manche !")
            else:
                print(player_class.player_2_name + " à gagné la manche !")

            print(player_class.player_1_name + " à joué : " + player_class.player_1_stroke)
            print(player_class.player_2_name + " à joué : " + player_class.player_2_stroke)
            i += 1

        self.__who_win()



game_class = Game()
player_class = Player()
print("---------")
game_class.game()