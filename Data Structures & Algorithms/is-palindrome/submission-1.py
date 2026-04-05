class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s):
            new_s = ""

            for char in s:
                if char.isalpha() or char.isdigit():
                    new_s+=char.lower()
            print(new_s)
            
            return new_s == new_s[::-1]

        return isPalindrome(s)
