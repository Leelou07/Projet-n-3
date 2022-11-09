import random
class Player :
    def __init__(self):
        #Proba de tirage
        self.p_stat = 50
        self.f_stat = 50    
        self.c_stat = 0
        
        #Choix ia
        self.ia_choice = self.ia_choice()
       
        #Choix joueur
        self.choice = self.__choice()

        #Proba IA
        self.probability_actualisation_ia = self.probability_actualisation()

        #Verif Prob
        self.verif_proba = self.__verif_proba()

        print("choix ia : " + str(self.ia_choice))
           
    '''
    Partie Player
    '''

    def __choice(self):
        return input("Votre coup ?")
    
    """
    Partie Ia
    """

    def ia_choice(self):
        mylist = ["Pierre", "Feuille", "Ciseau"]
        ## Premier lancé
        if(self.p_stat == 50 and self.f_stat == 50 and self.c_stat == 0):
            return (random.choices(mylist, weights = [ 50, 0, 50], k=1))
        ##Verif autre
        elif(self.p_stat > self.c_stat and self.p_stat > self.f_stat):
            return "Pierre"
        elif(self.c_stat > self.p_stat and self.c_stat > self.f_stat):
            return "Ciseau"
        elif(self.f_stat > self.c_stat and self.f_stat > self.p_stat):
            return "Feuille"
        elif(self.p_stat == self.c_stat and self.p_stat > self.f_stat):
            return str(random.choices(mylist, weights = [ 50, self.f_stat, 50], k=1))
        elif(self.f_stat == self.p_stat and self.f_stat > self.c_stat):
            return str(random.choices(mylist, weights = [ 50, 50, self.c_stat], k=1))
        elif(self.c_stat == self.f_stat and self.c_stat > self.p_stat):
            return str(random.choices(mylist, weights = [ self.p_stat, 50, 50], k=1))
        elif(self.c_stat == self.f_stat and self.c_stat == self.p_stat):
            return str(random.choices(mylist, weights = [ self.p_stat, self.f_stat, self.c_stat], k=1))

    def probability_actualisation(self):
        self.ia_choice = self.ia_choice[0]
        if self.ia_choice == "Pierre" : ## SI PIERRE VIENT DETRE JOUER
            self.p_stat += 25
            self.f_stat -= 25
            self.c_stat -= 25

        elif self.ia_choice == "Feuille" : ## SI FEUILLE VIENT DETRE JOUER
            self.p_stat -= 25
            self.f_stat += 25
            self.c_stat -= 25

        elif self.ia_choice == "Ciseau" : ## SI CISEAU VIENT DETRE JOUER
            self.p_stat -= 25
            self.f_stat -= 25
            self.c_stat += 25   

    def __verif_proba(self):
        if(self.p_stat < 0):
            self. p_stat = 0
        elif(self.f_stat < 0):
            self.f_stat = 0
        elif(self.c_stat < 0):
            self.c_stat = 0
            

Play = Player()

