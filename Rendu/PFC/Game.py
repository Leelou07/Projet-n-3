'''Importation of Player class'''
from Player import *

"""Creation of a class named  "Game" """
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
       
        """Integ Variables """
        self.player_1_point = 0
        self.player_2_point = 0
        self.round_nb = 0
        
        """"List"""
        self.choices_round = [1, 3, 5, 7, 9]
        self.choices_nb_round = int(self.__round_choices())
        
        
    """Function for the points incrementation"""
    def __add_point(self, bool):
        
        if(bool): #If true : add 1 point to player_1
            self.player_1_point += 1
        
        elif(bool != True): #If false : add 1 point to player_2
            self.player_2_point += 1
    

    """Function that is announcing the start of the game and giving the credits"""
    def __launch_game(self):
        print("--------------")
        print("-Début du jeu-")
        print("---Made  by---")
        print("-Les intellos-")
        print("--------------")

    """Choice of the number of round"""
    def __round_choices(self):
        
        """Print list of different rounds possible"""
        for i in range(4):
            print(str(self.choices_round[i]) + " ", end='')  
            """end='' ; to print in one line"""
        
        """Selection of the number of round"""
        print("")
        print("En combien de manche souhaitez vous jouer ?")
        answer = input()

        """Calling of the verifaction function"""
        if self.__verification_round_choice(answer) != True:
            print("Réponse incorrecte !")
            self.__round_choices()
        
        """Confirmation from the user of the selection"""
        print("Vous souhaitez jouer en", answer, "?")
        answer_verif = input("O/N : ")

        """Verification of the answer of the user"""
        if answer_verif == "O" :
            return answer 
        
        else : 
            if answer_verif != "N" :
                print("Réponse invalide")
            self.__round_choices()

    """Verification of the validity of the answer"""
    def __verification_round_choice(self, answer):
        
        answer = int(answer) ; """Convertion of String in int"""
        for i in range(4):
            """Checking the presence of the answer in the list of choice"""
            
            if answer == self.choices_round[i]: 
                return True
        return False    

    """Function establishing the win conditions"""
    def __test_win(self):
        
        """In case player_1 win"""
        if(player_class.player_1_stroke == "Pierre" and player_class.player_2_stroke == "Ciseau"):
            self.__add_point(True) ; """Incrementation of the point of player_1"""
            return True
        
        elif(player_class.player_1_stroke == "Feuille" and player_class.player_2_stroke == "Pierre"):
            self.__add_point(True) ; """Incrementation of the point of player_1"""
            return True
        
        elif(player_class.player_1_stroke == "Ciseau" and player_class.player_2_stroke == "Feuille"):
            self.__add_point(True) ; """Incrementation of the point of player_1"""
            return True
        
        #In case player_2 win
        else:
            self.__add_point(False) ; """Incrementation of the point of player_2"""
            return False

    """Function printing the winner and the score"""
    def __who_win(self):
        
        #In case of Eguality
        if(self.player_2_point == self.player_1_point):
            print("Égalité !")
        
        elif(self.player_2_point > self.player_1_point):
            print(player_class.player_2_name + " à gagné la partie !")
        
        else:
            print(player_class.player_1_name + " à gagné la partie !")
        print(player_class.player_2_name + " a " + str(self.player_2_point) + " point(s).")
        print(player_class.player_1_name + " a " + str(self.player_1_point) + " point(s).")   

        
    """"Function controlling the launching of the game"""
    def game(self):
        i = 0
        self.__launch_game()
        
        """Loop controlling the rounds"""
        while(i < self.choices_nb_round):
            player_class.player()
            
            """Printing the winner of the round and what each player played"""
            if self.__test_win() :
                print(player_class.player_1_name + " à gagné la manche !")
            
            else:
                print(player_class.player_2_name + " à gagné la manche !")

            print(player_class.player_1_name + " à joué : " + player_class.player_1_stroke)
            print(player_class.player_2_name + " à joué : " + player_class.player_2_stroke)
            i += 1

        self.__who_win()


"""Association of each class with a variable"""
game_class = Game()
player_class = Player()

"""Launching of the Game"""
game_class.game()