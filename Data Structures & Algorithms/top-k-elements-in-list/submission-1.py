class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        result = []
        for key, value in freq.items():
            if len(result)<k:
                result.append(key)
            else:
                break
        return result