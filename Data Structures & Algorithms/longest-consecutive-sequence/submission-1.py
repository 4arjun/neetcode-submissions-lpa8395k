class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxi = 0
        for num in nums:
            if num-1 not in seen:
                count=0
                while num+count in seen:
                    count+=1
                maxi = max(maxi, count)
        return maxi