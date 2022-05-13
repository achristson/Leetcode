"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

idea: 
iterate through each cell in the grid and do a dfs on it.
keep a counter of the number of islands
every time we start a new dfs we increment the counter
all land cells we have seen will be changed to water so we dont have multiple dfs on the same island

let n = length of the grid
let m = length of a row in the grid
Time: O(n*m)
Space: O(n*m)
https://leetcode.com/problems/number-of-islands/
"""


def number_of_islands(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
  
def num_islands_bfs(grid):
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

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            grid[r][c] = "0"

            for neighbor_r, neighbor_c in get_neighbors(r, c):
                if grid[neighbor_r][neighbor_c] == "1":
                    queue.append((neighbor_r, neighbor_c))
    num_islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                num_islands += 1
                bfs(r, c)
    return num_islands
