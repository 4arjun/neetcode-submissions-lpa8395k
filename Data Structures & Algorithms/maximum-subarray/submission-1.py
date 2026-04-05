class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = 0
        maxi = float('-inf')
        for num in nums:
            csum+=num
            maxi = max(maxi, csum)
            if csum<0:
                csum = 0
        return maxi
            