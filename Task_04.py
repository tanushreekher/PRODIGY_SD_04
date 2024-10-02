# Sudoku Solver using Backtracking Algorithm

def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    """Check if it's valid to place the num at board[row][col]."""
    # Check if the number is in the current row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is in the current column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is in the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers 1-9 in the empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        # Recursively try to solve the rest of the board
                        if solve_sudoku(board):
                            return True
                        
                        # Backtrack if placing the current number doesn't lead to a solution
                        board[row][col] = 0
                
                return False  # No valid number found for this cell
    return True  # All cells are filled and valid

# Example Sudoku puzzle (0 represents an empty cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
print("Original Sudoku board:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSudoku solved:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
