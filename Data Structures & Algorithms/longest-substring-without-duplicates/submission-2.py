class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        maxi = 0
        for end in range(len(s)):
            if s[end] not in seen:
                maxi = max(maxi, end-start+1)
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
        return maxi