"""
example:

Given
tree:
     3
    / \
   9  20
     /  \
    15   7
output = [[3], [9, 20], [15, 7]]

Given
tree:
     1
output  = [[1]]

Given
null tree
output = []

Idea:
if we get a null tree we return an empty list
we want to capture all the inputs at each level
we can use a modified BFS for this
initialize a results list
add root element to a queue and while the queue is not empty we do the following
    keep a counter of the size of the queue before any children are added
    keep a temporary list where we store all elements which are at the same level
    until we reach the counter value we
        pop the next node from the queue add add its value to the temporary list
        add its children to the queue
    once we reach the counter value we add our temporary list to our results
once the queue is empty we can return our results
"""


from collections import deque


def level_order_traversal(root):
    if not root:
        return []

    results = []
    queue = deque()
    queue.append(root)

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
        results.append(temp)
    return results


"""
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
let n = number of nodes in the tree
Time: O(n)
Space: O(n)
"""
