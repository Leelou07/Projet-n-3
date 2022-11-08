class Morpion:
    def __init__(self):
        self.board = board

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

def is_win_diagonal(board, player):
    if (board [0][0] == player and board [1][1] == player and board [2][2] == player ):
        print("T'as gagné bg")
    elif (board [0][2] == player and board [1][1] == player and board [2][0] == player):
        print("T'as gagné bg")
    else:
        return -1

def is_win_horizontal(board, player):
    if (board[0][0] == player and board[1][0] == player and board[2][0] == player ):
        print ("t'as gagné bg")
    elif (board[0][1] == player and board[1][1] == player and board[2][1] == player ):
        print ("t'as gagné bg")
    elif (board[0][2] == player and board[1][2] == player and board[2][2] == player ):
        print ("t'as gagné bg")
    else:
        return -1

def is_win_vertical(board, player):
    if (board[0][0] == player and board[0][1] == player and board[0][2] == player ):
        print ("t'as gagné bg")
    elif (board[1][0] == player and board[1][1] == player and board[1][2] == player ):
        print ("t'as gagné bg")
    elif (board[2][0] == player and board[2][1] == player and board[2][2] == player ):
        print ("t'as gagné bg")
    else:
        return -1

def initialisation():
    print("\n | 0 | 0 | 0 | \n | 0 | 0 | 0 | \n | 0 | 0 | 0 |  \n \n Voici le tableau vide \n")
    print("\n | 1 | 2 | 3 | \n | 4 | 5 | 6 | \n | 7 | 8 | 9 |  \n \n Voici le tableau \n ")
    player_choice = input("Veuiller entre le nombre de votre case choisie : ")
    
    if player_choice == 1:
        board[0][0] == 1
    if board[0][0] == 1:
        print("\n | 1 | 0 | 0 | \n | 0 | 0 | 0 | \n | 0 | 0 | 0 |  \n")

def declaration_des_règles():
    board[0][0] == 0
    board[0][1] == 0
    board[0][2] == 0
    board[1][0] == 0
    board[1][1] == 0
    board[1][2] == 0
    board[2][0] == 0
    board[2][1] == 0
    board[2][2] == 0



initialisation()




