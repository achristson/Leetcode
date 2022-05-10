"""
Given an m x n board board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:

Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

idea:
do a dfs on each O we see on the border of the board
because the O's on the border cannot be surrounded by X's 
any O's connected to them would also not be able to be surrounded by X's
change all O's to a temporary value -> T
once that is done iterate through the board and change all O's to X's and T's to O's
n = length of the board
m = length of a row in the board
Time: O(n*m)
Space: O(n*m)
Link: https://leetcode.com/problems/surrounded-regions/

"""


def surrounded_regions(board):
    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if 0 > r or r >= rows or 0 > c or c >= cols or board[r][c] != "O":
            return
        board[r][c] = "T"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        if board[r][0] == "O":
            dfs(r, 0)
        if board[r][cols - 1] == "O":
            dfs(r, cols - 1)

    for c in range(cols):
        if board[0][c] == "O":
            dfs(0, c)
        if board[rows - 1][c] == "O":
            dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            if board[r][c] == "T":
                board[r][c] = "O"
    return board
