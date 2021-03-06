def subsets(nums):
    result = []

    def helper(i, slate):
        if i == len(nums):
            result.append(slate[:])
            return
        helper(i+1, slate)
        slate.append(nums[i])
        helper(i+1, slate)
        slate.pop()

    helper(0, [])
    return result


"""
Link: https://leetcode.com/problems/subsets/
Time: O(2^n)
Space: O(2^n)
"""
