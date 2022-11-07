import random
from typing import final
class player :

    def __init__(self, name):
        #Initialisation prob
        self.p_stat = 50
        self.f_stat = 50
        self.c_stat = 0
        #Number of tour
        self.nb_tour = 0
        self.name = name
        #Initialisation of choice variable
    
    #Human choice
    def __human_choice(self):
        answer = input("Choissisez votre coup :")
        answer_upper = answer.capitalize()
        if(answer_upper == "Pierre" or answer_upper == "Feuille" or answer_upper == "Ciseau"):
            return answer_upper
        else:
            print("Coup invalide ! Merci de choissir un coup valide")
            self.__human_choice()
    
    #IA translate
    def __IA_translate(self, choice):
        res = choice[0]
        return res
    #IA choice
    def __ia_choice(self):
        mylist = ["Pierre", "Feuille", "Ciseau"]
        #première game
        return self.__IA_translate(random.choices(mylist, weights = [ 50, 50, 50], k=1))

    def choice(self):
        if self.name=='bot' :
            return self.__ia_choice()
        else :
            return self.__human_choice()
