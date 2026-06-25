class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxprod = [0]*n
        minprod = [0]*n
        maxprod[0] = nums[0]
        minprod[0] = nums[0]
        ans = nums[0]

        for i in range(1, n):
            maxprod[i] = max(nums[i], nums[i]*maxprod[i-1], nums[i]*minprod[i-1])

            minprod[i] = min(nums[i], nums[i]*maxprod[i-1], nums[i]*minprod[i-1])
            ans = max(ans, maxprod[i])
        return ans