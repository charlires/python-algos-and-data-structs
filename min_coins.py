from typing import List

class Solution: 
    def minCoins(self, coins: List[int], amount: int) -> int:
        # dp = [amount + 100] * (amount + 1)
        # dp[0] = 0
        dp = {}
        dp[0] = 0


        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        if dp[amount] != amount + 100:
            return dp[amount] 
        else:
            return -1
        
assert Solution().minCoins([1, 3, 4, 5], 7) == 2
            