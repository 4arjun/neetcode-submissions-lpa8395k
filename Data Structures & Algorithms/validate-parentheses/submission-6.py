class Solution:
    def isValid(self, s: str) -> bool:
        open = {"[":"]", "(":")", "{":"}"}
        stack = []
        for br in s:
            if br in open:
                stack.append(open[br])
            else:
                if not stack or stack.pop()!=br:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False