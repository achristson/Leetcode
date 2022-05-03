# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_node_from_end(head, n):
    dummy = ListNode()
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n):
        if fast.next:
            fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


"""
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

n = length of linked list
Time: O(n)
Space: O(1)
"""
