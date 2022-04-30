def combination_sum(candidates, target):
    result = []

    def combination_sum_helper(i, slate):
        if sum(slate) == target:
            result.append(slate[:])
            return
        if sum(slate) > target:
            return

        for j in range(i, len(candidates)):
            slate.append(candidates[j])
            combination_sum_helper(j, slate)
            slate.pop()

    combination_sum_helper(0, [])
    return result


"""
Link: https://leetcode.com/problems/combination-sum/
Time: O(b^n)
Space: O(b^n)
"""
