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
   
def island_perimeter_bfs(grid):
    rows, cols = len(grid), len(grid[0])

    def get_neighbors(r, c):
        delta_r = [-1, 0, 1, 0]
        delta_c = [0, 1, 0, -1]
        neighbors = []

        for i in range(len(delta_r)):
            new_r = r + delta_r[i]
            new_c = c + delta_c[i]
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))
        return neighbors

    def get_perimeter(r, c):
        count = 0
        if r - 1 < 0 or grid[r - 1][c] == 0:
            count += 1
        if r + 1 >= rows or grid[r + 1][c] == 0:
            count += 1
        if c - 1 < 0 or grid[r][c - 1] == 0:
            count += 1
        if c + 1 >= cols or grid[r][c + 1] == 0:
            count += 1
        return count

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        perimeter = 0
        while queue:
            r, c = queue.popleft()
            perimeter += get_perimeter(r, c)
            grid[r][c] = 2

            for neighbor_r, neighbor_c in get_neighbors(r, c):
                if grid[neighbor_r][neighbor_c] == 1:
                    queue.append((neighbor_r, neighbor_c))
        return perimeter

    total_perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                total_perimeter += bfs(r, c)
    return total_perimeter
