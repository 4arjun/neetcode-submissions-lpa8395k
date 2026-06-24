class Solution:
    def numDecodings(self, s: str) -> int:
        
        def helper(ind, dp):
            if ind in dp:
                return dp[ind]
            if ind == len(s):
                return 1
            if s[ind] == "0":
                return 0
            count = 0

            for i in range(ind, ind+2):
                if i<len(s):
                    num = int(s[ind:i+1])
                    if 1<=num<=26:
                        count+=helper(i+1, dp)
            dp[ind] = count
            return dp[ind]
        return helper(0, {})