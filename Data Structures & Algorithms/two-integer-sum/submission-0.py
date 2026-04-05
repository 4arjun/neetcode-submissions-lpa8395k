class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in dict:
                return [dict[new_target], i]
            else:
                dict[nums[i]] = i