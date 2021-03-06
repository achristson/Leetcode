def partition(s):
    results = []

    def is_palindrome(substring):
        left = 0
        right = len(substring)-1

        while left <= right:
            if substring[left] != substring[right]:
                return False
            left += 1
            right -= 1
        return True

    def helper(i, slate):
        if i == len(s):
            results.append(slate[:])
            return

        for j in range(i, len(s)):
            if is_palindrome(s[i:j+1]):
                slate.append(s[i:j+1])
                helper(j+1, slate)
                slate.pop()

    helper(0, [])
    return results


"""
Link: https://leetcode.com/problems/palindrome-partitioning/
Time: O(2^n)
Space: O(2^n)
"""
