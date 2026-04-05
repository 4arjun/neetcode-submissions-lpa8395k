class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while stack and stack[-1][0]<j:
                stackVal, stackInd = stack.pop()
                res[stackInd] = i-stackInd
            stack.append((j, i))
        return res
