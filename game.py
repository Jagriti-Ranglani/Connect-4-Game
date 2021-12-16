import numpy as np

def create_board(r,c):
    b = np.zeros((r,c))
    return b

def drop_piece(r, b, col, piece):
    i = r-1
    while i>=0:
        if b[0][col] != 0:
            print("Invalid entry! Try another column")
            break
        else:
            if b[i][col] == 0:
                b[i][col] = piece
                break
            else:
                i -= 1
    print(b)

print("Hello Guys Let's play the game Connect Four")
row = int(input("No of rows : "))
column = int(input("No of cols : "))

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


    turn += 1
    turn = turn%2