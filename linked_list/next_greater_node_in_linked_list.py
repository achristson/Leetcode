
def next_greater_node(head):

    length_of_list = 0
    curr = head
    while curr:
        curr = curr.next
        length_of_list += 1

    result = [0] * length_of_list
    stack = []
    curr = head

    for i in range(length_of_list):
        while stack:
            if stack[-1][0].val < curr.val:
                result[stack[-1][1]] = curr.val
                stack.pop()
            else:
                break
        stack.append((curr, i))
        curr = curr.next
    return result


"""
Link: https://leetcode.com/problems/next-greater-node-in-linked-list/
n = length of list
Time: O(n)
Space: O(n)
"""
