print("""\n ██████╗██╗  ██╗██╗███████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗
██╔════╝██║  ██║██║██╔════╝██╔═══██╗██║   ██║████╗ ████║██║
██║     ███████║██║█████╗  ██║   ██║██║   ██║██╔████╔██║██║
██║     ██╔══██║██║██╔══╝  ██║   ██║██║   ██║██║╚██╔╝██║██║
╚██████╗██║  ██║██║██║     ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝
                                                  \n""")

registre = ["Pierre","Feuille","Ciseaux"]
lastCoup = [registre[0]]

def makeChoise(lastCoup) :
    if lastCoup == registre[0] :
       return registre[1]
    elif lastCoup == registre[1] :
        return registre[2]
    elif  lastCoup == registre[2] :
        return registre[0]
        
    
def game(): # je définis ici une fonction game 
    isFinish = 0
    gagnant = ""
    print("Vous jouez a chifoumi contre l'ordi , il peut choisir 3 options , les voici :\n\n1-Pierre\n2-Feuille\n3-Ciseaux\n") # affichage dees instructions
    while isFinish<=3 :
        choix_pc = makeChoise(lastCoup[len(lastCoup)-1])
        choix_joueur = input('Pierre (p), Feuille (f) ou Ciseaux (c) ?') # on demande au joueur ce qu'il veut choisir entre pierre feuille papier et ciseau 
        #choix_pc = registre[0] # appel a la fonction randint() du module random pour choisir un nombre pseudo-aleatoire entre 1 et 3 , qui sont les arguments speécifiés entre parenthèses 

        if choix_joueur == 'p':                              # Si le choix du joueur correspond a la touche P (pierre) :
           
            print("Vous avez choisi Pierre.")             # Afficher au joueur son choix 
            lastCoup.append(choix_pc)
            print("L'ordinateur a choisi", choix_pc)       # Ainsi qu'afficher le choix du PC 
            


        elif choix_joueur == 'f':                            # Sinon si le choix du joueur correspond a F (feuille) : 
            #choix_pc = makeChoise(lastCoup[len(lastCoup)-1]) 
            print("Vous avez choisi Feuille.")               # Monter choix joueur 
            lastCoup.append(choix_pc)
            print("L'ordinateur a choisi", choix_pc)         # Montrer choix PC
            

        elif choix_joueur == 'c':                            # Sinon si le choix du joueur correspond a C (ciseaux) :
            #choix_pc = makeChoise(lastCoup[len(lastCoup)-1])
            print("Vous avez choisi Ciseaux.")               # Afficher choix joueur
            lastCoup.append(choix_pc)
            print("L'ordinateur a choisi", choix_pc)         # Afficher choix PC 
            
        
        if (choix_joueur == 'p' and choix_pc == registre[2]) or (choix_joueur == 'f' and choix_pc == registre[0]) or (choix_joueur == 'c' and choix_pc == registre[1]):       # Si le choix du joueur est pierre ET que le choix du PC est la troisieme option , OU bien , que le choix du joueur est feuille ET que le choix du PC est 1 , OU BIEN , que le choix du joueur est ciseaux ET que le choix du PC est 2 : (oui je sais c'est long) 
            print("Vous gagnez !")
            isFinish = isFinish+1                                                                                                   # Alors afficher la fucking victoire 

        elif (choix_joueur == 'p' and choix_pc == registre[1]) or (choix_joueur == 'f' and choix_pc == registre[2]) or (choix_joueur == 'c' and choix_pc == registre[0]):     # Sinon si , le choix joueur est pierre ET que le PC choisi 2 , Ou alors , que le chois joueur est feuille ET que le fucking PC a choisi la troisieme option , OU bien , que le choix joueur est ciseaux ET que le pc a choisi 1 : 
            print("L'ordinateur gagne !")                                                                                                       # Alors t'as perdu , ha la loose XPTDRRRRR
            isFinish = isFinish+1

        elif (choix_joueur == 'p' and choix_pc == registre[0]) or (choix_joueur == 'f' and choix_pc == registre[1]) or (choix_joueur == 'c' and choix_pc == registre[2]):     # Sinon , si tout le charabia (le meme principe que les lignes d'au dessus mais avec des valeurs modifiées) : 
            print("Egalité !")
            isFinish = isFinish+1                                                                                                # Alors égalité ! 


start = input("Appuyez sur une touche pour commencer")         # Variable contenant une entrée qui propose d'appuyer sur une touche pour démarrer le jeu 

if start =='':                                                 # Si t'appuies sur un peu n'importe quelle touche de ton beau clavier : 
    game()                                                     # Le jeu démarre ! 
    lastCoup[len(lastCoup)-1]
    