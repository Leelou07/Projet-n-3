board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
board_exemple = [
    [0, '|', 0, 1, 2],
    [1, '|', 0, 1, 2],
    [2, '|', 0, 1, 2]
]
def is_win_diagonal(board, player):
    if(board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return player
    elif(board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return player 
    else:
        return -1
def is_win_honrizontal(board, player):
    if(board[0][0] == player and board[0][1] == player and board[0][2] == player):
        return player
    elif(board[1][0] == player and board[1][1] == player and board[1][2] == player):
        return player
    elif(board[2][0] == player and board[2][1] == player and board[2][2] == player):
        return player
    else:
        return -1
def is_win_vertical(board,player):
    if(board[0][0] == player and board[1][0] == player and board[2][0] == player):
        return player
    elif(board[0][1] == player and board[1][1] == player and board[2][1] == player):
        return player
    elif(board[0][2] == player and board[1][2] == player and board[2][2]):
        return player
    else:
        return -1
def is_win(board, player):
    if((is_win_diagonal(board, player)) or (is_win_honrizontal(board, player)) or (is_win_vertical(board, player))):
        return True
    else:
        return False
def game(board, player, board_exemple):
    print("Planche de jeu type :")
    print_exemple_board(board_exemple)
    answer = input("Quel ligne voulez vous jouer ?")
    int(answer)
    answer2 = input("Quel colonne voulez vous jouer ?")
    int(answer2)
    board[int(answer)][int(answer2)] = player
    return board

def print_board(board):
    for i in range(3):
        print(str(board[i][0]) + " " + str(board[i][1]) + " " + str(board[i][2]))

def print_exemple_board(board):
    for i in range(3):
        print(str(board[i][0]) + " " + str(board[i][1]) + " " + str(board[i][2]) + " " + str(board[i][3]) + " " + str(board[i][4]))


print_board(board)

#print(is_win_diagonal(board))
player = 1
point_1 = 0
point_2 = 0
while(True):
    game(board, player, board_exemple)
    if(is_win(board, player)):
        if (player == 1):
            point_1 += 1
            print(str(player) + " a gagné")
        else:
            point_2 += 1
            print(str(player) + " a gagné")
    if(player == 1):
        player = 2
    else :
        player = 1
    print("Votre jeu est :")
    print_board(board)
    print("")
