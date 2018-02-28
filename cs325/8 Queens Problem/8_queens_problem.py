#!/bin/python3

# Program based off example provided here:
# https://www.ploggingdev.com/2016/11/n-queens-solver-in-python-3/

def main():

    print("In main")




# Solve via backtracking
def solve(board, col, size):

    # Base case
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            borad[i][col] = 1
            if col == size - 1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)

            board[i][col] # Backtrack step

if __name__ == "__main__":
    main()

