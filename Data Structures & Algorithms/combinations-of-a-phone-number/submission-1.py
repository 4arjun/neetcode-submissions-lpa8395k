class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        result = []
        if len(digits) == 0:
            return []
        def helper(ind, temp):
            if ind == len(digits):
                result.append("".join(temp))
                return
            
            for ch in num_map[digits[ind]]:
                temp.append(ch)
                helper(ind+1, temp)
                temp.pop()
        helper(0, [])

        return result
