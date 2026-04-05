class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ['+', '-', '*', "/"]
        for char in tokens:
            if char not in symbols:
                stack.append(char)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if char == "+":
                    stack.append(left+right)
                if char == "-":
                    stack.append(left-right)
                if char == "*":
                    stack.append(left*right)
                if char == "/":
                    stack.append(left/right)
        return int(stack[-1])
