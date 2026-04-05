class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        find1 = find2 = find3 = False
        for a, b, c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a == target[0]:
                find1 = True
            if b == target[1]:
                find2 = True
            if c == target[2]:
                find3 = True
        return True if find1 and find2 and find3 else False