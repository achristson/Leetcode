def letter_combinations(digits):
        if not digits:
            return []
        
        mappings = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        
        def helper(i, slate):
            if len(slate) == len(digits):
                result.append("".join(slate))
                return
            
            for j in range(len(mappings[digits[i]])):
                slate.append(mappings[digits[i]][j])
                helper(i+1,slate)
                slate.pop()
                
        helper(0,[])
        return result
