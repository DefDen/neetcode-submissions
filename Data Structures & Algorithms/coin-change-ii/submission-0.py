class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        for i in range(len(coins)):
            memo[(i, 0)] = 1
        def recursive(i, a):
            if a < 0:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in memo:
                return memo[(i, a)]
            memo[(i, a)] = recursive(i, a - coins[i]) + recursive(i + 1, a)
            return memo[(i, a)]
        return recursive(0, amount) 