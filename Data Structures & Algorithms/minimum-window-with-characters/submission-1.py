class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map1 = {}
        char_map2 = Counter(t)
        mini = float('inf')
        start = 0
        have, need = 0, len(t)
        st = ""

        for end in range(len(s)):
            if s[end] in char_map2:
                char_map1[s[end]] = char_map1.get(s[end], 0) + 1
                if char_map1[s[end]]<=char_map2[s[end]]:
                    have+=1



            while have == need:
                if (end-start+1)<mini:
                    mini = end-start+1
                    st = s[start:end+1]

                if s[start] in char_map2:
                    char_map1[s[start]]-=1
                    if char_map1[s[start]] < char_map2[s[start]]:
                        have -= 1
                    if char_map1[s[start]] == 0:
                        del char_map1[s[start]]
                start+=1
        return st



