class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(ind, prevIndex, dp):
            if ind == len(nums):
                return 0
            if (ind, prevIndex) in dp:
                return dp[(ind, prevIndex)]
            take = float('-inf')
            if prevIndex == -1 or nums[ind]>nums[prevIndex]:
                take = 1+helper(ind+1, ind, dp)
            not_take = helper(ind+1, prevIndex, dp)

            dp[(ind, prevIndex)] = max(take, not_take)
            return dp[(ind, prevIndex)]

        return helper(0, -1, {})