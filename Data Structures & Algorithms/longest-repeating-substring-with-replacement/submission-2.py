class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        start = 0
        maxf = 0
        maxi = 0
        for end in range(len(s)):
            if s[end] in char_freq:
                char_freq[s[end]]+=1
            else:
                char_freq[s[end]]=1
            
            maxf = max(maxf, char_freq[s[end]])

            while (end-start+1-maxf) > k:
                char_freq[s[start]]-=1
                if char_freq[s[start]] == 0:
                    del char_freq[s[start]]
                start+=1
            maxi = max(maxi, end-start+1)
        return maxi



            