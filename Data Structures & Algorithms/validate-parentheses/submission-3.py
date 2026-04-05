class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "{", "["]
        dict = {"(":")", "{":"}", "[": "]"}
        for char in s:
            if char in open:
                stack.append(char)
            
            else:
                if stack:
                    el = stack.pop()
                else:
                    return False
                if char != dict[el]:
                    return False
        return len(stack) == 0 
