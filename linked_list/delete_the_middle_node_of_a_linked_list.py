class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head):
    if not head.next:
        return None

    dummy = ListNode()
    dummy.next = head

    fast = head
    slow = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return dummy.next


"""
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/
let n = length of linked list
Time: O(n)
Space: O(1)
"""
