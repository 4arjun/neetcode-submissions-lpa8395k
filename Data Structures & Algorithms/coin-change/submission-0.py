class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n =len(coins)

        def helper(ind, csum, dp):
            if (ind,csum) in dp:
                return dp[(ind, csum)]
            if csum == amount:
                return 0
            if csum>amount or ind == n:
                return float('inf')
            
            take = helper(ind, csum+coins[ind], dp) + 1
            not_take = helper(ind+1, csum, dp)
            dp[(ind, csum)] = min(take, not_take)
            return dp[(ind, csum)]
        
        res = helper(0, 0, {}) 
        return res if res!=float('inf') else -1
