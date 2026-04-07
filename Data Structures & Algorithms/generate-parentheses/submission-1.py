class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
    
        def helper(temp, open_b, close_b):
            if len(temp) == 2*n:
                result.append("".join(temp))
                return
                
            if open_b:
                temp.append("(")
                helper(temp, open_b-1, close_b)      
                temp.pop()      
            if close_b>open_b:
                temp.append(")")
                helper(temp, open_b, close_b-1)
                temp.pop()

        helper([], n, n)
        return result            

