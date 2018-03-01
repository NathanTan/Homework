#!/bin/python3

def main():
    size = 6
    start = (2, 2)
    board = create_board(size)
    fill_board(board, size)
    print_board(board, size)

    execute_knights_tour(board, size, start)
    print_board(board, size)

# Checks if the path is complete
def path_is_closed(board, size):
    None

def execute_knights_tour(board, size, knight_pos):
    
    update_board(board, size, knight_pos)
    knight_pos = get_next_pos(board, size, knight_pos)
    print_board(board, size)
    update_board(board, size, knight_pos)
    knight_pos = get_next_pos(board, size, knight_pos)
    print_board(board, size)
    
    update_board(board, size, knight_pos)
    knight_pos = get_next_pos(board, size, knight_pos)
    


def get_next_pos(board, size, knight_pos):
    availible_spaces = get_legal_moves(board, size, knight_pos)
    if len(availible_spaces) < 1:
        print("ERROR")
        print_board(board, size)
        print("Knights position: " + str(knight_pos))
    return availible_spaces[0]

def get_legal_moves(board, size, knight_pos):
    moves = []
    row = knight_pos[0]
    col = knight_pos[1]
    min_val = 9 # 8 is the maximum allowed value
    min_val_loc = -1 # The position of the lowest value in the array


    # Bottom right
    x = row + 2
    y = col + 1
    if x < size and y < size:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))

    x = row + 1
    y = col + 2
    if x < size and y < size:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))
    
    #Top right
    x = row - 1
    y = col + 2
    if x >= 0 and y < size:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))

    x = row - 2
    y = col + 1
    if row - 2 >= 0 and col + 1 < size:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))

    #Top left
    x = row - 2
    y = col - 1
    if x >= 0 and y >= 0:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))

    x = row - 1
    y = col - 2
    if x >= 0 and y >= 0:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))

    # Bottom right
    x = row + 1
    y = col - 2
    if x < size and y >= 0:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))
    x = row + 2
    y = col - 1    
    if x < size and y >= 0:
        min_val, min_val_loc = mark_min(board[x][y], min_val, min_val_loc, len(moves))
        moves.append((x, y))

    return moves

def mark_min(board_val, min_val, min_val_loc, moves_len):  
    if board_val < min_val and board_val > 0:
        return board_val, moves_len # Set the new values
    else:
        return min_val, min_val_loc # Keep the old values



def update_board(board, size, knight_pos):
    row = knight_pos[0]
    col = knight_pos[1]
    board[row][col] = 0
    # Bottom right
    x = row + 2
    y = col + 1
    print(x)
    print(y)
    if x < size and y < size and board[x][y] > 0:
        board[x][y]  -= 1
    x = row + 1
    y = col + 2
    if x < size and y < size and board[x][y] > 0:
        board[x][y]  -= 1
    
    x = row - 1
    y = col + 2
    #Top right
    if x >= 0 and y < size and board[x][y] > 0:
        board[x][y]  -= 1
    x = row - 2
    y = col + 1
    if x >= 0 and y < size and board[x][y] > 0:
        board[x][y]  -= 1

    #Top left
    x = row - 2
    y = col - 1
    if x >= 0 and y >= 0 and board[x][y] > 0:
        board[x][y]  -= 1
    x = row - 1
    y = col - 2
    if x >= 0 and y >= 0 and board[x][y] > 0:
        board[x][y]  -= 1

    # Bottom right
    x = row + 1
    y = col - 2
    if x < size and y >= 0 and board[x][y] > 0:
        board[x][y]  -= 1
    x = row + 2
    y = col - 1
    if x < size and y >= 0 and board[x][y] > 0:
        board[x][y]  -= 1

def create_board(size):
    graph = [[0 for x in range(size)] for y in range(size)]
    return graph


# Designed for a board of at least 4 x 4
def fill_board(board, size):
    val = 0
    for row in range(size):
        for col in range(size):
            if (col == 0 and row == 0) or\
               (col == size - 1 and row == 0) or\
               (col == 0 and row == size - 1) or\
               (col == size - 1 and row == size - 1):
                val = 2
            elif (col == 0 and row == 1) or\
                 (col == 1 and row == 0) or\
                 (col == 0 and row == size - 2) or\
                 (col == 1 and row == size - 1) or\
                 (col == size - 2 and row == 0) or\
                 (col == size - 1 and row == 1) or\
                 (col == size - 2 and row == size - 1) or\
                 (col == size - 1 and row == size - 2):
               val = 3
            elif (col == 1 and row == 1) or\
                 (col == 1 and row == size - 2) or\
                 (col == size - 2 and row == 1) or\
                 (col == size - 2 and row == size - 2):
               val = 4
            #4 is the highest number that can be on the edge of the board
            elif col == 0 or row == 0 or col == size - 1 or row == size - 1:
                val = 4 
            #6 is the highest number that can be on the board without being in the 'internal square'
            elif col == 1 or row == 1 or col == size - 2 or row == size - 2:
                val = 6
            else:
                val = 8
            board[row][col] = val
            #print("board[" + str(row) + "][" + str(col) + "]: " + str(val))

def print_board(board, size):
    for row in range(size):
        for col in range(size):
            print(board[row][col], end=" ")
        print("")
    print("")

if __name__ == "__main__":
    main()
