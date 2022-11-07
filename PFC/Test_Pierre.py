choices = ["Pierre", "Feuille", "Ciseaux"]

class User :
    def __init__(self) :
        self.name = self.__username_choice()
        print(self.name)
        
    def __username_choice(self):
        username = input("Quel est votre Pseudo ? ")
        print ("Votre pseudo est" , username)
        

def choice ():    
    print("Les coups possibles sont :", choices)
    user_choice = input("Quel est votre coup ?")
    print("Votre coup est :", user_choice)
user_choice = choice


def check ():
    if choice in choices :
        True
        print("Coup valide")
    else :
        print("Votre coup n'est pas valide !")
        choice()

while True :
    player = User()
    print(player.name)
    