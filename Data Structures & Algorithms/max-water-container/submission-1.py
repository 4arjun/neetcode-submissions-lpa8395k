class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        left, right = 0, len(heights)-1

        while left<right:
            maxi = max(maxi,(min(heights[left], heights[right]) * (right-left)))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxi