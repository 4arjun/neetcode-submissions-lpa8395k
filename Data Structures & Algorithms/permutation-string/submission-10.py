class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = Counter(s1)
        freqs2 = {}
        if len(s2)<len(s1):
            return False
        for i in range(len(s1)):
            freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1
        if freqs1 == freqs2:
            return True
        start = 0
        for end in range(len(s1),len(s2)):
            freqs2[s2[end]] = freqs2.get(s2[end], 0) + 1
            freqs2[s2[start]]-=1
            if freqs2[s2[start]] == 0:
                del freqs2[s2[start]]
            start+=1
            if freqs1 == freqs2:
                return True
        return False
        
            
