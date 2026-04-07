class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        def helper(ind, temp):
            result.append(temp.copy())
     
            
            for i in range(ind, n):
                if i>ind and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                helper(i+1, temp)
                temp.pop()


        helper(0, [])
        return result