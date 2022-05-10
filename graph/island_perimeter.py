"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. 
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:

Input: grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

idea:
iterate through the grid and do a dfs when we find a 1
we will keep a count of all the neighbors that are out of bounds or water
return this count and the sum of all the counts for each cell in the island
let n = length of the grid
let m = length of a row in the grid
Time: O(n*m)
Space: O(n*m)
Link: https://leetcode.com/problems/island-perimeter/
"""


def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 2
        count = 0
        if r - 1 < 0 or grid[r - 1][c] == 0:
            count += 1
        if r + 1 >= rows or grid[r + 1][c] == 0:
            count += 1
        if c - 1 < 0 or grid[r][c - 1] == 0:
            count += 1
        if c + 1 >= cols or grid[r][c + 1] == 0:
            count += 1

        return (count + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1))

    perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += dfs(r, c)
    return perimeter
