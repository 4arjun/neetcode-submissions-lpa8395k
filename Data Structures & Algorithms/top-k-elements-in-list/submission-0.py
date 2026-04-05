class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        num_map = {}
        for num in nums:
            if num in num_map:
                num_map[num]+=1
            else:
                num_map[num]=1
        
        for key, value in num_map.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for i, j in heap:
            result.append(j)
        return result