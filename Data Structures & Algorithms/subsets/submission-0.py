class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def helper(ind, temp):
            if ind==n:
                result.append(temp.copy())
                return 
            temp.append(nums[ind])
            take = helper(ind+1, temp)
            temp.pop()
            not_take = helper(ind+1, temp)
        helper(0, [])
        return result
