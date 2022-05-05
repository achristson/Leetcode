"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

examples:
input: 
    3
   / \
  9  20 
    /  \
   15   7
output: 3

input: 
    1
     \
      2
output: 2

Idea: 
traverse the tree with dfs 
keep track of maximum depth so far
add to depth as we go down the tree
when we reach a leaf we update the maximum depth so far if we have a larger value

let n = number of nodes in the tree
Time: O(n)
Space: O(n)

edge case:
    - null tree
"""


def max_depth(root):
    if not root:
        return 0

    max_so_far = 0

    def get_depth(node, depth):
        if not node:
            nonlocal max_so_far
            max_so_far = max(max_so_far, depth)
            return
        get_depth(node.left, depth + 1)
        get_depth(node.right, depth + 1)

    get_depth(root, 0)
    return max_so_far
