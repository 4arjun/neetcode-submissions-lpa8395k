class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        maxi = 0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            maxi = max(maxi, end-start+1)

        return maxi