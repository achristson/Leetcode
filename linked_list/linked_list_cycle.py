
def has_cycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


"""
Link: https://leetcode.com/problems/linked-list-cycle/submissions/
Time: O(n)
Space: O(1)
"""
