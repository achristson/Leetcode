def letter_case_permutation(s):
    results = []

    def helper(i, slate):
        if len(slate) == len(s):
            results.append("".join(slate))
            return

        if s[i].isdigit():
            slate.append(s[i])
            helper(i+1, slate)
            slate.pop()
        else:
            slate.append(s[i].upper())
            helper(i+1, slate)
            slate.pop()
            slate.append(s[i].lower())
            helper(i+1, slate)
            slate.pop()

    helper(0, [])
    return results


"""
Link: https://leetcode.com/problems/letter-case-permutation/
Time: O(2^n)
Space: O(2^n)
"""
