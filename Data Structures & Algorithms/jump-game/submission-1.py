class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if max_reachable>=i:
                max_reachable = max(max_reachable, nums[i]+i)
            else:
                return False
        
        return True if max_reachable >= len(nums)-1 else False