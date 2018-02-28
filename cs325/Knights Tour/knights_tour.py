#!/bin/python3

def main():
    print("In main")
    size = 4
    board = create_board(size)
    fill_board(board, size)
    print_board(board, size)


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


if __name__ == "__main__":
    main()
