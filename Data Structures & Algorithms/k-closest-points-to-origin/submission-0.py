class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for u, v in points:
            dist = u*u + v*v
            heapq.heappush(heap, (-dist, u, v))

            if len(heap)>k:
                heapq.heappop(heap)
        return [[u, v] for (_, u, v) in heap]
