
"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example:

tree:
    1
   / \
  2   3
output: 25
12 + 13 = 25

tree:
    4
   / \
  9   0
 / \
5   1
output: 1026
495 + 491 + 40 = 1026

Idea:
keep a global sum
do a dfs and store each value in a list 
once we reach the leaf then we convert the values in the list to one number and then add to our global sum

let n = number of node in the tree
Time: O(n)
Space: O(n)
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""


def sum_root_to_leaf_numbers(root):
    global_sum = 0

    def get_number(slate):
        n = len(slate)-1
        current = 0
        for num in slate:
            current += num * (10**n)
            n -= 1
        return current

    def get_root_to_leaf_number(node, slate):
        if not node.left and not node.right:
            nonlocal global_sum
            slate.append(node.val)
            global_sum += get_number(slate)
            slate.pop()
            return
        slate.append(node.val)
        if node.left:
            get_root_to_leaf_number(node.left, slate)
        if node.right:
            get_root_to_leaf_number(node.right, slate)
        slate.pop()

    get_root_to_leaf_number(root, [])
    return global_sum
