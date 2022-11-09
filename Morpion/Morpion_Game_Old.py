class Game :
    def __init__(self):
        self.var00 = 0
        self.var01 = 0
        self.var02 = 0
        self.var10 = 0
        self.var11 = 0
        self.var12 = 0
        self.var20 = 0
        self.var21 = 0
        self.var22 = 0
        self.hit = self.hit_test()
        self.check = self.hit_check()
        self.actualisation = self.actualise()
        
    def hit_test(self):
        print("\n" "|", self.var00, "|", self.var01, "|", self.var02, "|" "\n" "|", self.var10, "|", self.var11, "|", self.var12, "|" "\n" "|", self.var20, "|", self.var21, "|", self.var22, "|"  "\n \n" "Voici le tableau vide" "\n")
        print("\n | 1 | 2 | 3 | \n | 4 | 5 | 6 | \n | 7 | 8 | 9 |  \n \n Voici le tableau \n ")
        answer = input("Veuiller entre le nombre de votre case choisie : ")
        print("Vous avez choisi de jouer en:", answer, "O/N ")
        answer_verif = input()
        
        if answer_verif == "O" :
            return answer 
        else :
            self.hit_test()
    

    def hit_check(self):
        if self.hit == 1:
            if self.var00 != 0:
                print("Cette case est déjà prise")
                self.hit_test()
            self.var00 = 1
            return self.var00

        elif self.hit == 2:
            if self.var01 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var01 = 1
            return self.var01

        elif self.hit == 3:
            if self.var02 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var02 = 1
            return self.var02

        elif self.hit == 4:
            if self.var10 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var10 = 1
            return self.var10

        elif self.hit == 5:
            if self.var11 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var11 = 1
            return self.var11

        elif self.hit == 6:
            if self.var12 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var12 = 1
            return self.var12

        elif self.hit == 7:
            if self.var20 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var20 = 1
            return self.var20

        elif self.hit == 8:
            if self.var21 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var21 = 1
            return self.var21

        elif self.hit == 9:
            if self.var22 != 0:
               print("Cette case est déjà prise")
               self.hit_test()
            self.var22 = 1
            return self.var22 





    def actualise(self):
        print("\n" "|", self.var00, "|", self.var01, "|", self.var02, "|" "\n" "|", self.var10, "|", self.var11, "|", self.var12, "|" "\n" "|", self.var20, "|", self.var21, "|", self.var22, "|"  "\n \n")

Start = Game()   



    