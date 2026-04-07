class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def helper(temp, visited):
            if len(temp) == n:
                result.append(temp.copy())
                return
            for i in range(n):
                if i in visited:
                    continue
                visited.add(i)
                temp.append(nums[i])
                helper(temp, visited)
                visited.remove(i)
                temp.pop()

        helper([], set())
        return result