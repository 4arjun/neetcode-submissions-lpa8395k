class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        start = 0
        end = 0
        maxi = 0
        while end<len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end+=1
                maxi = max(maxi, end-start)
            else:
                seen.remove(s[start])
                start+=1
        return maxi
        

