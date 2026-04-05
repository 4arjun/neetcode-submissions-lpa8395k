class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map1 = Counter(s1)
        char_map2 = {}
        start = 0
        for end in range(len(s2)):
            if s2[end] in char_map1:
                if s2[end] in char_map2:
                    char_map2[s2[end]]+=1
                else:
                    char_map2[s2[end]] = 1
                while char_map1[s2[end]]<char_map2[s2[end]]:
                    char_map2[s2[start]]-=1
                    if char_map2[s2[start]] == 0:
                        del char_map2[s2[start]] 
                    start+=1
            else:
                char_map2 = {}
                start = end+1
            print(char_map1)
            print(char_map2)
            if char_map1 == char_map2:
                return True
        return False
