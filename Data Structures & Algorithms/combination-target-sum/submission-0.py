class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)

        def helper(ind, csum, temp):
            if csum == target:
                result.append(temp.copy())
                return
            if csum>target or ind>=n:
                return 

            for i in range(ind, n):

                temp.append(nums[i])
                take = helper(i, csum+nums[i], temp)
                temp.pop()
        helper(0, 0, [])
        return result

