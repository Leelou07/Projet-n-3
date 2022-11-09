class Game :
    def __init__(self):
        self.Coup = self.Coup_test()
        self.coup_verif = self.Coup_checkup()
        #self.actualisation = self.Actualisation()

    def Coup_test(self):
        var00 = 0
        var01 = 0
        var02 = 0
        var10 = 0
        var11 = 0
        var12 = 0
        var20 = 0
        var21 = 0
        var22 = 0
        
        print("\n" "|", var00, "|", var01, "|", var02, "|" "\n" "|", var10, "|", var11, "|", var12, "|" "\n" "|", var20, "|", var21, "|", var22, "|"  "\n \n" "Voici le tableau vide" "\n")
        print("\n | 1 | 2 | 3 | \n | 4 | 5 | 6 | \n | 7 | 8 | 9 |  \n \n Voici le tableau \n ")
        answer = input("Veuiller entre le nombre de votre case choisie : ")
        print("Vous avez choisi de jouer en:", answer)
        answer_verif = input("O/N")
        
        if answer_verif == "O" :
            return answer 
        else :
            self.Coup_test()
    
    def Coup_checkup(self):
        if self.Coup == 1:
            self.var00 = 1
            return self.var00
        elif self.Coup == 2:
            self.var01 = 1
            return self.var01
        elif self.Coup == 3:
            self.var02 = 1
            return self.var02
        elif self.Coup == 4:
            self.var10 = 1
            return self.var10
        elif self.Coup == 5:
            self.var11 = 1
            return self.var11
        elif self.Coup == 6:
            self.var12 = 1
            return self.var12
        elif self.Coup == 7:
            self.var20 = 1
            return self.var20
        elif self.Coup == 8:
            self.var21 = 1
            return self.var21
        elif self.Coup == 9:
            self.var22 = 1
            return self.var22 

Start = Game()   
