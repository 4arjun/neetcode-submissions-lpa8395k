class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        start = 0
        max_freq = 0
        maxi = 0
        for end in range(len(s)):
            char_map[s[end]] = char_map.get(s[end], 0) + 1
            max_freq = max(max_freq, char_map[s[end]])

            while (end-start+1)-max_freq>k:
                char_map[s[start]]-=1
                start+=1
            maxi = max(maxi, end-start+1)

        return maxi


                
