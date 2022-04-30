def combination_sum_3(k, n):
        result = []
        
        def helper(i,slate):
            if sum(slate) > n or i > n:
                return 
            if sum(slate) == n and len(slate) == k:
                result.append(slate[:])
                return
            
            for j in range(i, n+1):
                if 1 <= j < 10:
                    slate.append(j)
                    helper(j+1,slate)
                    slate.pop()
        helper(1,[])
        return result
