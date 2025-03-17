"""
36. Valid Sudoku
Medium
Topics
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

from collections import defaultdict
from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check for each rows
        for row in board:
            data = set()
            for num in row:
                if num == '.': continue

                if num in data:
                    return False
                data.add(num)

        # check for each columns
        for row in range(len(board)):
            data = set()
            for col in range(len(board)):
                if board[col][row] == '.': continue

                if board[col][row] in data:
                    return False
                data.add(board[col][row])

        #check for sub blocks (3x3)s
        for row_block in range(0,9,3):
            for col_block in range(0,9,3):
                blocks = [(row_block+i, col_block+j) for i in range(3) for j in range(3)]
                data = set()
                for i,j in blocks:
                    if board[i][j] == '.': continue

                    if board[i][j] in data:
                        return False
                    data.add(board[i][j])

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.': continue

                num = board[row][col]
                block = (row//3, col//3)

                if num in rows[row] or num in cols[col] or num in blocks[block]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                blocks[block].add(num)

        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

response = Solution().isValidSudoku(board)
print(response)
