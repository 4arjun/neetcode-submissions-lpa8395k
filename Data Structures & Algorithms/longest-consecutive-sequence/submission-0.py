class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxi = 0
        for num in seen:
            if num-1 not in seen:
                length = 1
                while num+1 in seen:
                    num+=1
                    length+=1
                maxi = max(maxi, length)
        return maxi
