from random import *  # ici je fait une importation de module , il s'agit dans notre cas du module random , l'asterix sert a importer toutes les fonctions de ce module , il est cependant déconseillé professionnellement 

print("""\n ██████╗██╗  ██╗██╗███████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗
██╔════╝██║  ██║██║██╔════╝██╔═══██╗██║   ██║████╗ ████║██║
██║     ███████║██║█████╗  ██║   ██║██║   ██║██╔████╔██║██║
██║     ██╔══██║██║██╔══╝  ██║   ██║██║   ██║██║╚██╔╝██║██║
╚██████╗██║  ██║██║██║     ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝
                                                  \n""")

def game(): # je définis ici une fonction game 

    print("Vous jouez a chifoumi contre l'ordi , il peut choisir 3 options , les voici :\n\n1-Pierre\n2-Feuille\n3-Ciseaux\n") # affichage dees instructions

    choix_joueur = input('Pierre (p), Feuille (f) ou Ciseaux (c) ?') # on demande au joueur ce qu'il veut choisir entre pierre feuille papier et ciseau 
    choix_pc = randint(1, 3) # appel a la fonction randint() du module random pour choisir un nombre pseudo-aleatoire entre 1 et 3 , qui sont les arguments speécifiés entre parenthèses 

    if choix_pc == 1:                      # si le choix du PC est la premiere option :
        choix_pc == "Pierre"               # alors il s'agirat de la pierre 

    elif choix_pc == 2:                    # Sinon , si le choix du PC est la deuxieme option :
        choix_pc == "Feuille"              # Alors , il s'agirat de la feuille 

    elif choix_pc == 3:                    # Sinon , si le choix du PC corespond a la troisieme option :
        choix_pc == "Ciseaux"              # Alors il s'agirat des ciseaux 

    if choix_joueur == 'p':                              # Si le choix du joueur correspond a la touche P (pierre) :
        print("Vous avez choisi Pierre.")                # Afficher au joueur son choix 
        print("L'ordinateur a choisi", choix_pc)         # Ainsi qu'afficher le choix du PC 

    elif choix_joueur == 'f':                            # Sinon si le choix du joueur correspond a F (feuille) : 
        print("Vous avez choisi Feuille.")               # Monter choix joueur 
        print("L'ordinateur a choisi", choix_pc)         # Montrer choix PC 

    elif choix_joueur == 'c':                            # Sinon si le choix du joueur correspond a C (ciseaux) :
        print("Vous avez choisi Ciseaux.")               # Afficher choix joueur
        print("L'ordinateur a choisi", choix_pc)         # Afficher choix PC 

    if (choix_joueur == 'p' and choix_pc == 3) or (choix_joueur == 'f' and choix_pc == 1) or (choix_joueur == 'c' and choix_pc == 2):       # Si le choix du joueur est pierre ET que le choix du PC est la troisieme option , OU bien , que le choix du joueur est feuille ET que le choix du PC est 1 , OU BIEN , que le choix du joueur est ciseaux ET que le choix du PC est 2 : (oui je sais c'est long) 
        print("Vous gagnez !")                                                                                                              # Alors afficher la fucking victoire 

    elif (choix_joueur == 'p' and choix_pc == 2) or (choix_joueur == 'f' and choix_pc == 3) or (choix_joueur == 'c' and choix_pc == 1):     # Sinon si , le choix joueur est pierre ET que le PC choisi 2 , Ou alors , que le chois joueur est feuille ET que le fucking PC a choisi la troisieme option , OU bien , que le choix joueur est ciseaux ET que le pc a choisi 1 : 
        print("L'ordinateur gagne !")                                                                                                       # Alors t'as perdu , ha la loose XPTDRRRRR

    elif (choix_joueur == 'p' and choix_pc == 1) or (choix_joueur == 'f' and choix_pc == 2) or (choix_joueur == 'c' and choix_pc == 3):     # Sinon , si tout le charabia (le meme principe que les lignes d'au dessus mais avec des valeurs modifiées) : 
        print("Egalité !")                                                                                                                  # Alors égalité ! 


    retry = input("\nVoulez vous rejouer ? O/N")     # Variable contenant une demande pour rejouer , car apres tout on est des tryharders Pro Gamers du chifoumi de Gam's 

    if retry == 'o':                                 # Si la variable correspond a la lettre O ( donc si t'as tapé o)
        game()                                       # Alors normalement le jeu va redemarrer 
    else:                                            # Sinon :
        exit()                                       # Sortir 

start = input("Appuyez sur une touche pour commencer")         # Variable contenant une entrée qui propose d'appuyer sur une touche pour démarrer le jeu 

if start =='':                                                 # Si t'appuies sur un peu n'importe quelle touche de ton beau clavier : 
    game()                                                     # Le jeu démarre ! 