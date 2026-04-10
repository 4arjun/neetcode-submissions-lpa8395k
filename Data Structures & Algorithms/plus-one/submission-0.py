class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            val = carry+digits[i]
            if val>=10:
                digits[i] = 0
            else:
                digits[i] = val
                carry = 0
                break
        if carry:
            return [1] + digits
        return digits
                    

