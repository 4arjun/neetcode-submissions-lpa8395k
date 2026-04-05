class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max_so_far = 0
        right_max_so_far = 0
        left_max = [0] * n
        right_max = [0] * n
        for i in range(1,len(height)):
            left_max_so_far = max(left_max_so_far, height[i-1])
            left_max[i] = left_max_so_far

        for i in range(len(height)-2, -1, -1):
            right_max_so_far = max(right_max_so_far, height[i+1])
            right_max[i] = right_max_so_far
        result = 0
        for i in range(len(height)):
            if (min(left_max[i], right_max[i]))-height[i]>0:
                result+=abs(height[i]-min(left_max[i], right_max[i]))
        return result
