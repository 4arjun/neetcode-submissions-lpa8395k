class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reachable = 0
        jumps = 0
        curr_end = 0
        for i in range(len(nums)-1):
            max_reachable = max(max_reachable, nums[i]+i)

            if curr_end == i:
                jumps+=1
                curr_end = max_reachable
        return jumps