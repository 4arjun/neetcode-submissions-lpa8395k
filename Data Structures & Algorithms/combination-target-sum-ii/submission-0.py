class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()
        def helper(ind, temp, csum):
            if csum == target:
                result.append(temp.copy())
                return
            if ind == n or csum>target:
                return 
            
            for i in range(ind, n):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
                if csum+candidates[i]>target:
                    break
                temp.append(candidates[i])
                helper(i+1, temp, csum+candidates[i])
                temp.pop()
        helper(0, [], 0)
        return result