class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2

        def helper(ind, csum, dp):
            if (ind, csum) in dp:
                return dp[(ind, csum)]

            if csum == target:
                return True

            if ind == len(nums):
                return False
            
            take = helper(ind+1, csum+nums[ind], dp)
            not_take = helper(ind+1, csum, dp)
            dp[(ind, csum)] = take or not_take
            return dp[(ind, csum)]
        return helper(0, 0, {})
