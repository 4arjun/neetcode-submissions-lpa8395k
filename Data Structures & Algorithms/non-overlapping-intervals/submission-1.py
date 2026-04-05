class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]    
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]<end:
                end = min(end, intervals[i][1])
                count+=1
            else:
                start = intervals[i][0]
                end = intervals[i][1]
        return count