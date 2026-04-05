class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(ind, temp, open, close):
            if ind == 2*n:
                result.append(''.join(temp))
                return 
            if open:
                temp.append("(")
                helper(ind+1, temp, open-1, close)
                temp.pop()
            if open<close:
                temp.append(")")
                helper(ind+1, temp, open, close-1)
                temp.pop()

        helper(0,[],n,n)
        return result