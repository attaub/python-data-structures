""" 
explor all possible solutions by building a solution incrementally and abandoning another one

use cases:

decision trees
permutations and combinations
search problems 
constraint satisfaction problems (sudoku, crosswords)


steps::

choice: Make a choice from the set of possible options.
constraint: Check if choice leads to solution or violates constraints.

backtrack:
if the solution is invalid
backtrack by undoing the last choice and trying another option

solution: if all constraints are satisfied and the solution is complete, add it to the result.
"""

# generate all possible permutations of a list of numbers


def permute(nums):
    def backtrack(path, used, res):
        print(f"Current path: {path}")
        print(f"Used flags: {used}")
        print(f"Current result: {res}")
        print("=" * 80)

        # base case: if satisfied, add path to results
        if len(path) == len(nums):
            # append a copy of the current path to the result
            res.append(path[:])
            print(f"Added to result: {path[:]}")
            print("==" * 40)
            return

        # iterate through the nums array
        for i in range(len(nums)):
            print(f"Checking num: {nums[i]} at index {i}")

            # if the number is already used, skip it
            if used[i]:
                print(f"Skipped {nums[i]} because it is already used")
                continue

            # mark the number as used and add it to the path
            used[i] = True
            path.append(nums[i])
            print(f"Added {nums[i]} to path: {path}")

            # recursively backtrack
            backtrack(path, used, res)

            print(f"Backtracking from path: {path}, removing {nums[i]}")
            path.pop()
            used[i] = False

    res = []
    print(f"Starting permutations for: {nums}")
    backtrack([], [False] * len(nums), res)
    print(f"Final result: {res}")
    return res


nums = [1, 2, 3]
permute(nums)


###################################################################
# generate all subsets of a list.
def subsets(nums):
    def backtrack(index, path):
        print(f"Called backtrack({index}, {path})")  
        res.append(path[:])  
        print(f"Added subset: {path[:]}")
        print("=="*40)
        for i in range(index, len(nums)):
            print(f"Appending {nums[i]} to path: {path}")  
            path.append(nums[i])  
            backtrack(i + 1, path)
            print(f"Removing {nums[i]} from path: {path}")  
            path.pop()  

    res = []
    backtrack(0, [])
    return res


nums = [1, 2, 3]
sus_sets = subsets(nums)
print("All subsets:" ,sub_sets)  

###################################################################
# n-queens problem: place N queens on an N×N chessboard such that no two queens threaten each other.

#############################################################################
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        # Check left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False
        # Check right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i] == j:
                return False
        return True

    def backtrack(row):
        if row == n:  # A valid placement is found
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place queen
                backtrack(row + 1)  # Move to the next row
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * n  # Track column positions of queens
    backtrack(0)
    return solutions

def print_solutions(solutions, n):
    for solution in solutions:
        for row in solution:
            print("".join("Q" if i == row else "." for i in range(n)))
        print("=" * n)  # Separator for different solutions

n = 8  # Change this for different board sizes
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions, n)


#############################################################################
# sudoku solver: fill a partially completed Sudoku grid.
def solveSudoku(board):
    def is_valid(num, row, col):
        block_row, block_col = row // 3 * 3, col // 3 * 3
        for i in range(9):
            if (
                board[row][i] == num
                or board[i][col] == num
                or board[block_row + i // 3][block_col + i % 3] == num
            ):
                return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in "123456789":
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = "."  # Undo the choice
                    return False
        return True

    backtrack()


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
solveSudoku(board)
print(board)

# word search in a grid: find if a word exists in a 2D grid


def exist(board, word):
    def backtrack(i, j, word_index):
        if word_index == len(word):  # Word found
            return True
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or board[i][j] != word[word_index]
        ):
            return False

        temp = board[i][j]  # Mark the cell as visited
        board[i][j] = "#"

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if backtrack(i + x, j + y, word_index + 1):
                return True

        board[i][j] = temp  # Undo the visit
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and backtrack(i, j, 0):
                return True
    return False


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
word = "ABCCED"
print(exist(board, word))  # Output: True
