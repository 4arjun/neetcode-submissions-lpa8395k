class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0]<=end:
                end = max(end, intervals[i][1])
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result