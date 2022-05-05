"""
Given the root of a binary tree, return the zigzag level order 
traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

examples: 

tree:
     3
    / \
   9  20
     /  \
    15   7
output: [[3], [20, 9], [15, 7]]

tree:
      1
output: [[1]]

tree:
    empty
output: []

Idea:
traverse the tree using BFS
keep a flag (true or false)
keep a level count by taking it length of the queue before any children are added 
iterate in a for loop until we reach the level count
    put every level of nodes into a temporary list
    add each child to the queue
depending on the flag we either reverse the list or add it to our results directly
let n = number of nodes in the tree
Time: O(n)
Space: o(n)

edge case:
    - tree is null

"""


from collections import deque


def binary_zigzag_level_order(root):
    if not root:
        return []
    flag = False
    queue = deque()
    queue.append(root)
    result = []

    while queue:
        level_count = len(queue)
        temp = []

        for _ in range(level_count):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if flag:
            temp.reverse()
        flag = not flag
        result.append(temp)
    return result
