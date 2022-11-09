class User : 
    #Initialise
    def __init__(self):
        self.modes = ["JvsJ", "JvsIa", "IavsIa"] #Liste des modes
        self.choices = ["Pierre", "Feuille", "Ciseaux"] #Liste coups possibles
        self.mode = self.__mode()
        self.mode_verif = self.__mode_verif()
        self.player_1_name = self.player_1
        self.player_2_name = self.player_2
        print("La partie oppose", self.player_1_name, "à", self.player_2_name)
    
    '''
    Choix du mode de jeu 
    '''
    def __mode(self):
        print("Choississez votre mode de jeu en tapant le nom correspondant")
        answer = input(self.modes)
        print("Le mode de jeu séléctionné est", answer, ".")
        answer_verif = input("Etês-vous sûr, O/N")

        if answer_verif == "O" :
            return answer
        else :
            if answer_verif != "N" :
                print("Répone invalide")
            print("Choisissez un nouveau mode")
            self.__mode()        

    '''
    Orientation du choix du mode de jeu 
    '''

    def __mode_verif(self):
            if self.mode == "JvsJ" :
                 self.player_1 = self.pseudo() 
                 self.player_2 = self.pseudo()
                 return self.player_1, self.player_2
            '''
            elif self.mode == "JvsIa" :
                self.player_1 = self.pseudo()
                self.player_2 = #Ia
                return self.player_1, self.player_2


            else :
                self.player_1 = #Ia
                self.player_2 = #Ia
                return self.player_1, self.player_2
            '''


    '''
    Choix du Pseudo
    '''
    def pseudo(self):
        answer = input("Quel est votre pseudo ?")
        print("Votre pseudo est :", answer, ".")
        answer_verif = input("Voulez vous utilisez ce pseudo ? O/N")
        
        if answer_verif == "O" :
            return answer
        else :
            if answer_verif != "N" :
                print("Répone invalide")
            print("Choisissez un nouveau pseudo")
            self.pseudo()
    
    '''
    Choix du Coup
   
    def choice(self):
        print("Les coups possibles sont :", self.choices)
        answer = input("Quel est votre coup ?")
        
        if answer in self.choices :
            True 
            print("Votre coup est :", answer)
            return answer
        else : 
            print("Votre coup n'existe pas !")
            self.choice()
    '''

joueur = User() #Lance la classe
#joueur.choice() #Lance le choix du Coup
