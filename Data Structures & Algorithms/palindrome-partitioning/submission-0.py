class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def isPalindrome(word):
            return word == word[::-1]

        def helper(ind, temp):
            if ind == n:
                result.append(temp.copy())
                return
            
            for i in range(ind, n):
                if isPalindrome(s[ind:i+1]):
                    temp.append(s[ind:i+1])
                    helper(i+1, temp)
                    temp.pop()

        helper(0, [])
        return result
