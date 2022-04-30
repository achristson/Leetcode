"""
Problem: Stair climbing problem

Let's say there's a robot that can move a unit distance to the right or a unit
distance to the up.
Let's say instructions for it are R to move right and U to move up.
The robot starts at position (0, 0) and
Moving to right is adding one to x coordinate and moving up is adding one to y
coordinate
So for exampole after RRU you would be at (2, 1)

You are given a coordinate (x, y) to reach using the robot.
Assume x > 0 and y > 0 and both are integers.

1- Print all possible unique instructions for the robot that will have it
reach the given coordinate
2- How many possible such instructions are there?
(Is there a faster way to calculate just the number other than generating all
such possible insturctions?)

Example:

(4, 3)

RRRRUUU
RRRURUU
RRRUURU
RRRUUUR
....
UUURRRR
"""


def stair_climbing_unique_instructions(x, y):
    instruction = []
    for _ in range(x):
        instruction.append("R")
    for _ in range(y):
        instruction.append("U")

    def helper(i, slate):
        if i == len(instruction):
            print("".join(slate))
            return
        h_set = set()
        for j in range(i, len(instruction)):
            if instruction[j] not in h_set:
                h_set.add(instruction[j])
                instruction[i], instruction[j] = instruction[j], instruction[i]
                slate.append(instruction[i])
                helper(i+1, slate)
                slate.pop()
                instruction[i], instruction[j] = instruction[j], instruction[i]
    helper(0, [])


def stair_climbing_possible_instructions(x, y):
    grid = [[0 for _ in range(x+1)] for _ in range(y+1)]

    for i in range(1, len(grid[0])):
        grid[0][i] = 1

    for i in range(1, len(grid)):
        grid[i][0] = 1

    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            grid[r][c] = grid[r-1][c] + grid[r][c-1]
    print(grid[y][x])


stair_climbing_possible_instructions(4, 3)
