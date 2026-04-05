class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        char_map1 = Counter(s1)
        char_map2 = {}
        for end in range(len(s1)):
            char_map2[s2[end]] = char_map2.get(s2[end], 0) + 1
        start = 0
        for end in range(len(s1), len(s2)):
            if char_map1 == char_map2:
                return True
            char_map2[s2[start]] -= 1
            if char_map2[s2[start]] == 0:
                del char_map2[s2[start]]
            char_map2[s2[end]] = char_map2.get(s2[end], 0) + 1
            start+=1
        return char_map1 == char_map2

        