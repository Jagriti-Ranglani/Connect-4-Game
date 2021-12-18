from collections import Counter
import numpy as np

# Creating Board
def create_board(r,c):
    b = np.zeros((r,c))
    b = b.astype(int)
    return b

# Logic for piece Droping
def drop_piece(r, b, col, player_piece):
    i = r-1
    while i>=0:
        if b[0][col] != 0:
            print("Invalid entry! Try another column")
            break
        else:
            if b[i][col] == 0:
                b[i][col] = player_piece
                break
            else:
                i -= 1
    print(b)


# Rows & Cols winning
def checkRows(x, no_of_connecting_piece, turn):
    for row in x:
        d = Counter(row)
        player1 = 1
        player2 = 2
        if turn == 0 and d[player1] >= no_of_connecting_piece:
            return 1
        elif turn == 1 and d[player2] >= no_of_connecting_piece:
            return 2
    return 0

def checkDiagonals(x):
    pass

# Winning Conditions
def win_conditions(b, no_of_connecting_piece, turn):
    for x in [b, np.transpose(b)]:
        result = checkRows(x, no_of_connecting_piece, turn)
        if result:
            return result
    return checkDiagonals(b)


# Main program
print("Hello Guys Let's play the game Connect Four")
row = int(input("No of rows : "))
column = int(input("No of cols : "))
piece = int(input("No of connected piece required for winning : "))

game_over = False
board = create_board(row,column)
turn = 0

print(board)

while not game_over:
    if turn==0:
        selected_col = int(input("Player 1 - "))
        drop_piece(row, board, selected_col, 1)
        

    else:
        selected_col = int(input("Player 2 - "))
        drop_piece(row, board, selected_col, 2)

    results = win_conditions(board, piece, turn)
    if results==1 or results==2:
        print(f"Player {results} wins")
        break

    turn += 1
    turn = turn%2