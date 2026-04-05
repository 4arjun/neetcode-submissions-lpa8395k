class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = {}
        for task in tasks:
            if task not in taskMap:
                taskMap[task] = 1
            else:
                taskMap[task]+=1

        heap = []
        for key, val in taskMap.items():
            heapq.heappush(heap,(0, key))
        time = 0
        while heap:
            print(heap)
            if heap[0][0]<=time:
                val, key = heapq.heappop(heap)
                taskMap[key]-=1
                if taskMap[key]>0:
                    heapq.heappush(heap, (val+n+1, key))
            time+=1
        return time 

