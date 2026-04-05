class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        result = 0
        for end in range(len(s)):
            if s[end] not in seen:
                seen.add(s[end])
            elif s[end] in seen:
                while s[end] in seen:
                    seen.remove(s[start])
                    start+=1
                seen.add(s[end])
            result = max(result, end-start+1)
        return result

            
