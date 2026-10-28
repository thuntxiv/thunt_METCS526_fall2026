# METCS 526 Fall 2026 - MIDTERM
# Author: Tyler Hunt; Professor: Dr. David Mellor

import sys
import math

SYMBOLS = [] # List of valid symbols (to be populated on reading input)

#------------------------------PROBLEM 3----------------------------

def check_board(board:list, size:int):
    '''
    Checks if the given game board of the given size is in a valid state. To be considered valid, it must follow these conditions:
    • Each row contains each symbol at most once
    • Each column contains each symbol at most once
    • The board is divided into n non-overlapping sub-boards, each of size
        √n x √n (for a 4x4 board, four 2x2 sub-boards; for a 9x9 board, nine
        3x3 sub-boards), starting from the top-left corner. Each sub-board
        contains each symbol at most once.
    • Every non-empty cell contains one of the n listed symbols. A cell holding
        any other symbol makes the board invalid.
    Returns True or False accordingly.

    PARAMETERS
        board:LIST<STRING>
            A list of strings representing the state of the game board
        size:INT
            The integer side length of the game board (must be a perfect square)
    RETURN
        BOOL
            True if the game board follows all of the listed conditions, meaning it's in a valid state
            False if the game board breaks any of the conditions, constituting an invalid state
    '''
    # Check the whole board for row/column overlaps in symbols
    if not check_subboard(board, size, False):
        return False
    # This confirms conditions, 1, 2, and 4. Now, we need to check condition 3's sub-boards

    sub_size = int(math.sqrt(size))

    # Think of the board as a matrix of matrices representing sub-boards with dimensions sub_size X sub_size
    # Current row offset: i
    for i in range(sub_size):
        # subboard starting index: sub_size * (0, 1, 2, ... sub_size - 1)
        sub_board = board[i * sub_size:i * sub_size + sub_size] # Grab the rows needed for the current sub-board 
        
        # Current column offset: j
        for j in range(sub_size):
            # i, j references the current subboard location in the matrix of matrices
            for curr_row in range(sub_size):
                # Slice each row according to the desired columns for our sub-board
                sub_board[curr_row] = board[i * sub_size + curr_row][j * sub_size:j * sub_size + sub_size]

            # Check the sub-board, using the True flag to indicate that symbols cannot be repeated anywhere
            if not check_subboard(sub_board, sub_size, True):
                return False
    return True

def check_subboard(board:list, size:int, sub:bool):
    '''
    Checks if the given board or sub-board follows these conditions:
    • Each row contains a symbol at most once
    • Each column contains a symbol at most once
    If the 'sub' flag is True:
    • Each sub-board contains each symbol at most once
    Returns True or False accordingly.

    PARAMETERS
        board:LIST<STRING>
            A list of strings representing the current board to check
        size:INT
            The integer side length of the board to check
        sub:BOOL
            A boolean indicating whether or not the given board is a sub-board, determining if
            duplicate symbols need to be ruled out over the whole board.
    RETURN
        True if the given board follows all of the applicable game conditions
        False otherwise
    '''
    symbols_left = SYMBOLS.copy() # If needed, work with a list of the symbols that is continously removed from
    # Check every tile in the game board
    for i in range(size):
        for j in range(size):
            # Determine if the current symbol appears twice in its row/column
            if not check_symbol(board, i, j):
                return False
            # If this board is a sub-board, make sure the current symbol is still available
            if sub:
                if board[i][j] != '.':
                    if board[i][j] not in symbols_left:
                        return False
                    # If the symbol is available, remove it from the list. Now, it can't appear in the board again without failing
                    symbols_left.remove(board[i][j]) 
    return True

def check_symbol(board:list, row:int, col:int):
    '''
    Checks if the current symbol at the position given by row,col appears again at any point in its shared row or column.
    Returns True or False accordingly.

    PARAMETERS
        board:LIST<STRING>
            The game board that the symbol resides in, represented by a list of strings
        row:INT
            The row that the current symbol is found in
        col:INT
            The column that the current symbol is found in
    RETURN
        BOOL
            True if the same symbol as the one found at row,col never appears again in the same row and column.
            False if at least one of the same symbol appears in the same row or column.
    '''
    if not board[row][col] in SYMBOLS:
        if board[row][col] == '.': # Ignore empty tiles
            return True
        return False # Invalid character
    # Check the current symbol's entire row and entire column for any identical symbols
    for i in range(len(board)):
        if i != row:
            if board[i][col] == board[row][col]:
                return False
        if i != col:
            if board[row][i] == board[row][col]:
                return False
    return True

def print_board(board:list):
    '''
    For debugging; Prints the current state of the given board with one row per line.

    PARAMETERS
        board:LIST<STRING>
            A list of strings representing the game board to be printed
    RETURN
        None
    '''
    for row in board:
        print(row)

def check_input():
    '''
    Checks every line of input for the game board size, all valid symbols, and each row of the game board,
    then processes and determines whether the board is in a valid state based on multiple conditions related
    to symbol placement.

    PARAMETERS
        None
    RETURN
        None
    '''
    n = int(input()) # Line 1: Dimensions of puzzle board
    global SYMBOLS 
    SYMBOLS = input().strip().split(',') # Line 2: Valid symbols (Referenced in a const global list)
    board = []
    # Lines 2 - n+2: game board 
    for line in sys.stdin:
        if len(line) > 1:
            board.append("".join(line.strip().split(",")))
    print(f"The board is {"in" * (not check_board(board, n))}valid")

if __name__ == "__main__":
    check_input()