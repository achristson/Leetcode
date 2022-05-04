"""
tree:
         3
        / \
       5   1
      / \ / \
     6  2 0  8
       / \
      7   4
examples:
given nodes (6, 4) lca = 5
given nodes (2, 0) lca = 3
given nodes (1, 8) lca = 1
given nodes (7, 4) lca = 2

idea:
traverse the tree looking for our given nodes, if we find it then we True to our parent
our parent will evaluate the lca based on 2 cases
cases:
 - the current node is one of the nodes given and one of our children returned True -> lca is the current node
 - both children returned True -> lca is the current node
if either case is True then we have found our lca and we can stop traversing

steps:

check if the current node is null
if its not null
    call the function on the left child
    call the function on the right child

    check if our value is one of the given nodes

    check our two cases
        if either passes then set the lca our value
return if we found a node in either of our subtrees to our parent

"""


def lowest_common_ancestor(root, p, q):

    lca = None

    def find_lca(node, p, q):
        if not node:
            return False

        nonlocal lca
        if lca:
            return False

        left = find_lca(node.left, p, q)
        right = find_lca(node.right, p, q)

        current = node == p or node == q

        if left + right + current >= 2:
            lca = node
        return left or right or current

    find_lca(root, p, q)
    return lca
