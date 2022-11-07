from player import *
class game :
    
    def __init__(self):
        test = player()
        self.point_user = 0
        self.point_ia = 0
        #self.list = ["Pierre", "Feuille", "Ciseau"]
        self.user_choice = test.choice
        self.ia_choice = test.ia_choice
        self.ifwin = self.__test_win()

        if(self.ifwin == True):
            self.point_user += 1
            print(self.point_user)
        print("Point joueur " + str(self.point_user))
        print("Point ia : " + str(self.point_ia))

    def launch_game():
        print("--------------")
        print("-Début du jeu-")
        print("---Made  by---")
        print("-Les intellos-")
        print("--------------")

    def __test_win(self):
        print(self.ia_choice)
        if(self.user_choice == "Pierre" and self.ia_choice == "Ciseau"):
            print("1")
            return True
        elif(self.user_choice == "Feuille" and self.ia_choice == "Pierre"):
            print("1")
            return True
        elif(self.user_choice == "Ciseau" and self.ia_choice == "Feuille"):
            print("1")
            return True
        elif(self.user_choice == "Pierre" and self.ia_choice == "Pierre"):
            print("2")
            return False
        elif(self.user_choice == "Feuille" and self.ia_choice == "Feuille"):
            print("2")
            return False
        elif(self.user_choice == "Ciseau" and self.ia_choice == "Ciseau"):
            print("2")
            return False    

while(True):
    test = game()
   