class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p1, p2 = 0, len(s)-1
        while p1<=p2:
            while p1<=p2 and not(s[p1].isalnum()):
                p1+=1
            while p1<=p2 and not(s[p2].isalnum()):
                p2-=1
            print(p1, p2)
            if p1<=p2 and s[p1]!=s[p2]:
                return False
            p1+=1
            p2-=1
        return True
            