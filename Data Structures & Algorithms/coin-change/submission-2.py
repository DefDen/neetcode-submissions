class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if not amount:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for v in coins:
                if v > i:
                    continue
                if dp[i - v] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - v] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - v] + 1)
        print(dp)
        return dp[-1]