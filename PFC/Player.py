choices = ["Pierre", "Feuille", "Ciseaux"]

class user :
    def start(self, name) :
        self.name = name
        print("Quel est votre Pseudo ?")
        return(name)

def choice ():    
    print("Les coups possibles sont", choices)
    print("Quel est votre coup ?")
    return(choice)
user_choice = choice

x = 0
def check ():
    if choice in choices :
        x = x+1
        return("D'accord")
    else :
        print("Votre coup n'est pas valide !")
        choice()

choice()

#while x == 0 :
    choice()
    check()