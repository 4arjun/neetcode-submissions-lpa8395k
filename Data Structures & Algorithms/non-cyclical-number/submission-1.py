class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(val):
            ssum = 0
            while val>0:
                digit = val%10
                ssum+=digit*digit
                val = val//10
            return ssum

        seen = set()

        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squares(n)
        return True
