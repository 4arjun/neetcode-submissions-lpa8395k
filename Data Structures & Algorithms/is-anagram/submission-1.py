class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = [0]*26
        if len(s) != len(t):
            return False
        n = 0
        for char in s:
            if char_map[ord(char)-ord('a')] == 0:
                n+=1
            char_map[ord(char)-ord('a')] +=1
        for char in t:
            char_map[ord(char)-ord('a')] -=1
            if char_map[ord(char)-ord('a')] == 0:
                n-=1
        return n==0
        
        