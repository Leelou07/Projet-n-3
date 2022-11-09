import random
class Player :
    '''
    Variable
        self.modes -> List of different game mod
        self.choices -> List of possible strokes
        self.mode -> Mod selected
        self.mode_verif -> Profile configuration
        self.player_1_name -> Name of player 1
        self.player_2_name -> Name of player 2
    '''
    def __init__(self):
        #Proba de tirage
        self.p_stat = 50
        self.f_stat = 50    
        self.c_stat = 0
        #List
        self.modes = ["JvsJ", "JvsIa", "IavsIa"]
        self.choices = ["Pierre", "Feuille", "Ciseaux"]
        #String Variable
        self.mode = self.__mod_choice()
        self.player_1_name, self.player_2_name = self.__mod_profil()
        self.player_1_stroke = ""
        self.player_2_stroke = ""
        
    #Choice of the game mod
    def __mod_choice(self):
        #Print list
        for i in range(3):
            print(self.modes[i] + " ", end='')# end='' print in one line
        
        #Select the mod
        print("")
        answer = input("Choississez votre mode de jeu en tapant le nom correspondant : ")

        #Verification of the choice
        if self.__verification_mod_choice(answer) != True :
            print("Réponse incorrecte !")
            self.__mod_choice()
        
        #Verification of the user choice
        print("Le mode de jeu séléctionné est", answer, ".")
        answer_verif = input("Etês-vous sûr, O/N : ")

        #Verification of the answer
        if answer_verif == "O" :
            return answer 
        elif answer_verif != "N" :
            answer_verif != "N"
            print("Réponse invalide")
        self.__mod_choice() 

    #Verification of the mod choice
    def __verification_mod_choice(self, answer):

        for i in range(3):
            #Verification of the answer in the list of choice possibility
            if answer == self.modes[i] :
                return True
        return False     

    #Creation of player1 and player2 name
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

            


    '''
    Choix du Pseudo
    '''
    def __pseudo(self, joueur):
        answer = input("Quel est le pseudo du joueur " + str(joueur) + " ?")
        print("Votre pseudo est : ", answer, ".")
        answer_verif = input("Voulez vous utilisez ce pseudo ? O/N : ")
        
        if answer_verif == "O" :
            return answer 
        elif answer_verif != "N" : 
            print("Réponse invalide")
        self.__pseudo(joueur)

    #GOOD
    def player(self):
        if(self.mode == "JvsJ"):
            self.player_1_stroke = self.__player_choice()
            self.player_2_stroke = self.__player_choice()
            return
        elif(self.mode == "JvsIa"):
            self.player_1_stroke = self.__player_choice()
            self.player_2_stroke = self.__ia_choice()
            return
        elif(self.mode == "IavsIa"):
            self.player_1_stroke = self.__ia_choice()
            self.player_2_stroke = self.__ia_choice()
            return

    def __player_choice(self):
        answer = input("Choissisez votre coup :")
        answer_upper = answer.capitalize()
        if(answer_upper == "Pierre" or answer_upper == "Feuille" or answer_upper == "Ciseau"):
            return answer_upper
        else:
            print("Coup invalide ! Merci de choissir un coup valide")
            self.__player_choice()
    
    #---___ IA ___---#
    def __ia_choice(self):
        mylist = ["Pierre", "Feuille", "Ciseau"]
        ## Premier lancé
        if(self.p_stat == 50 and self.f_stat == 50 and self.c_stat == 0):
            choice = random.choices(mylist, weights = [ 50, 0, 50], k=1)
            self.__probability_actualisation(choice[0])
            self.__verif_proba()
            return choice[0]
        ##Verif autre
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

    def __probability_actualisation(self, choice):  
        if choice == "Pierre" : ## SI PIERRE VIENT DETRE JOUER
            self.p_stat -= 25
            self.f_stat += 25
            self.c_stat += 25

        elif choice == "Feuille" : ## SI FEUILLE VIENT DETRE JOUER
            self.p_stat += 25
            self.f_stat -= 25
            self.c_stat += 25

        elif choice == "Ciseau" : ## SI CISEAU VIENT DETRE JOUER
            self.p_stat += 25
            self.f_stat += 25
            self.c_stat -= 25   

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
        
