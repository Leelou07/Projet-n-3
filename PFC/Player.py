choices = ["Pierre", "Feuille", "Ciseaux"]
verif = 0
while verif == 0 :
    def move():
        print("Les coups possibles sont", choices)
        return input("Quel est votre coup ?")
    if move in choices :
        print("D'accord")
        verif = 1
    else :
        print("Votre coup n'existe pas !")