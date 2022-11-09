'''Importation of random modul for later use'''
import random

"""Creation of a class named  "Player"""
class Player :
    
    '''
    Variable
        self.modes -> List of different game mod
        self.choices -> List of possible stroke
        self.mode -> Mod selected
        self.mode_verif -> Profile configuration
        self.player_1_name -> Name of player 1
        self.player_2_name -> Name of player 2
    '''

    def __init__(self):
        self.p_stat = 50 ; """Probability of choosing Rock"""
        self.f_stat = 50 ; """Probability of choosing Paper"""
        self.c_stat = 0 ; """Probability of choosing Scissors"""
        
        """List"""
        self.modes = ["JvsJ", "JvsIa", "IavsIa"]
        self.choices = ["Pierre", "Feuille", "Ciseaux"]
       
        """String Variable"""
        self.mode = self.__mod_choice()
        self.player_1_name, self.player_2_name = self.__mod_profil()
        self.player_1_stroke = ""
        self.player_2_stroke = ""
        
    """Choice of the game mod"""
    def __mod_choice(self):
        
        """Print list of different game mod"""
        for i in range(3):
            print(self.modes[i] + " ", end='')# end='' print in one line
        
        """Select the mod"""
        print("")
        answer = input("Choississez votre mode de jeu en tapant le nom correspondant : ")

        """Calling of the verifaction function"""
        if self.__verification_mod_choice(answer) != True :
            print("Réponse incorrecte !")
            self.__mod_choice()
        
        """Confirmation from the user of the selection"""
        print("Le mode de jeu séléctionné est", answer, ".")
        answer_verif = input("Etês-vous sûr, O/N : ")

        """Verification of the answer of the user"""
        if answer_verif == "O" :
            return answer 
        
        elif answer_verif != "N" :
            answer_verif != "N"
            print("Réponse invalide")
        self.__mod_choice() 

    """Definition of the verification function for the mods selection"""
    def __verification_mod_choice(self, answer):
        
        for i in range(3):
            """Checking the presence of the answer in the list"""
            
            if answer == self.modes[i] :
                return True
        return False     

    """Affiliation of player_1/2 with a pseudo or a ia"""
    def __mod_profil(self):
        
        #Player vs Player
            if self.mode == "JvsJ" :
                player_1 = self.__pseudo(1) 
                player_2 = self.__pseudo(2)
                return player_1, player_2
            
        #Player vs IA
            elif self.mode == "JvsIa" :
                player_1 = self.__pseudo(1)
                player_2 = "Deep blue"
                return player_1, player_2

        #IA vs IA
            else :
                player_1 = "Deep blue"
                player_2 = "AlphaGo"
                return player_1, player_2


    '''Function for the choice of the player pseudo '''
    def __pseudo(self, joueur):
        
        answer = input("Quel est le pseudo du joueur " + str(joueur) + " ?")
        print("Votre pseudo est : ", answer, ".")
        answer_verif = input("Voulez vous utilisez ce pseudo ? O/N : ")
        
        if answer_verif == "O" :
            return answer 
        
        elif answer_verif != "N" : 
            print("Réponse invalide")
        self.__pseudo(joueur)

    """Function initiating the stroke of the player in accordance with the chosen mod"""
    def player(self):
        
        #For JvsJ
        if(self.mode == "JvsJ"): 
            self.player_1_stroke = self.__player_choice()
            self.player_2_stroke = self.__player_choice()
            return
        
        #For JvsIa
        elif(self.mode == "JvsIa"):
            self.player_1_stroke = self.__player_choice()
            self.player_2_stroke = self.__ia_choice()
            return
        
        #For IavsIa
        elif(self.mode == "IavsIa"):
            self.player_1_stroke = self.__ia_choice()
            self.player_2_stroke = self.__ia_choice()
            return

    """Function asking the player stroke"""
    def __player_choice(self):
        answer = input("Choissisez votre coup :")
        answer_upper = answer.capitalize()
        
        """Verification of the validity of the answer"""
        if(answer_upper == "Pierre" or answer_upper == "Feuille" or answer_upper == "Ciseau"):
            return answer_upper
       
        else:
            print("Coup invalide ! Merci de choissir un coup valide")
            self.__player_choice()
    
    """Function controlling the Ia choices"""
    def __ia_choice(self):
        
        """List of possible strike"""
        mylist = ["Pierre", "Feuille", "Ciseau"]
        
        """First strike"""
        if(self.p_stat == 50 and self.f_stat == 50 and self.c_stat == 0):
            choice = random.choices(mylist, weights = [ 50, 0, 50], k=1)
            self.__probability_actualisation(choice[0])
            self.__verif_proba()
            return choice[0]
        
        #Résolution of the different possibilities and selection of the best strike to play 
        elif(self.p_stat > self.c_stat and self.p_stat > self.f_stat):
            self.__probability_actualisation("Pierre")
            self.__verif_proba()
            return "Pierre"
        
        elif(self.c_stat > self.p_stat and self.c_stat > self.f_stat):
            self.__probability_actualisation("Ciseau")
            self.__verif_proba()
            return "Ciseau"
        
        elif(self.f_stat > self.c_stat and self.f_stat > self.p_stat):
            self.__probability_actualisation("Feuille")
            self.__verif_proba()
            return "Feuille"
        
        elif(self.p_stat == self.c_stat and self.p_stat > self.f_stat):
            choice = random.choices(mylist, weights = [ 50, self.f_stat, 50], k=1)
            self.__probability_actualisation(choice[0])
            self.__verif_proba()
            return choice[0]
        
        elif(self.f_stat == self.p_stat and self.f_stat > self.c_stat):
            choice = random.choices(mylist, weights = [ 50, 50, self.c_stat], k=1)
            self.__probability_actualisation(choice[0])
            self.__verif_proba()
            return choice[0]
        
        elif(self.c_stat == self.f_stat and self.c_stat > self.p_stat):
            choice = random.choices(mylist, weights = [ self.p_stat, 50, 50], k=1)
            self.__probability_actualisation(choice[0])
            self.__verif_proba()
            return choice[0]
        
        elif(self.c_stat == self.f_stat and self.c_stat == self.p_stat):
            choice = random.choices(mylist, weights = [self.p_stat, self.f_stat, self.c_stat], k=1)
            self.__probability_actualisation(choice[0])
            self.__verif_proba()
            return choice[0]

    """Function that is actualising the probabilities"""
    def __probability_actualisation(self, choice):  
        
        if choice == "Pierre" : # If rock was played
            self.p_stat -= 25
            self.f_stat += 25
            self.c_stat += 25

        elif choice == "Feuille" : # If paper was played
            self.p_stat += 25
            self.f_stat -= 25
            self.c_stat += 25

        elif choice == "Ciseau" : # If scissor was played
            self.p_stat += 25
            self.f_stat += 25
            self.c_stat -= 25   

    """Function that is regulating the probability"""
    def __verif_proba(self):
        
        if(self.p_stat < 0):
            self. p_stat = 0
        
        elif(self.f_stat < 0):
            self.f_stat = 0
        
        elif(self.c_stat < 0):
            self.c_stat = 0
        
        if(self.p_stat >= 100):
            self. p_stat = 100
        
        elif(self.f_stat >= 100):
            self.f_stat = 100
        
        elif(self.c_stat >= 100):
            self.c_stat = 100
        
