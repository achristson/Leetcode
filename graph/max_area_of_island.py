"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:

Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [
    [0,0,0,0,0,0,0,0]
    ]
Output: 0

idea;
iterate through each cell in the grid and do a dfs
when we come across a 1 we will change it to 0 so we dont do multiple dfs's on the same island
keep a counter of the number of 1's in the island we are doing the dfs for
once the dfs is done we will compare the count to the previous max count
if it is greater then we will make the update
let m = length of the grid
let n = length of the column
Time: O(m*n)
Space: o(m*n)

https://leetcode.com/problems/max-area-of-island/
"""


def max_area_of_islands(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        return (1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1))

    max_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_count = max(max_count, dfs(r, c))
    return max_count

def max_area_of_island_bfs(grid):
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
        count = 0
        grid[r][c] = 0

        while queue:
            r, c = queue.popleft()
            count += 1

            for neighbor_r, neighbor_c in get_neighbors(r, c):
                if grid[neighbor_r][neighbor_c] == 1:
                    grid[neighbor_r][neighbor_c] = 0
                    queue.append((neighbor_r, neighbor_c))
        return count

    max_area = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, bfs(r, c))
    return max_area
