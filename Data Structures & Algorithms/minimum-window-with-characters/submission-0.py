class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count1, count2 = {}, {}
        ind1, ind2 = -1, -1
        mini = float('inf')

        for char in t:
            count2[char] = count2.get(char, 0) + 1
        
        start = 0
        for end in range(len(s)):
            count1[s[end]] = count1.get(s[end], 0) + 1

            while all(count1.get(k, 0) >= v for k, v in count2.items()):
                if (end-start+1)<mini:
                    mini = end-start+1
                    ind1 = start
                    ind2 = end
                count1[s[start]]-=1
                if count1[s[start]] == 0:
                    del count1[s[start]]       
                start+=1 
        if ind1 == -1:
            return ""
        else:
            return s[ind1:ind2+1]

            