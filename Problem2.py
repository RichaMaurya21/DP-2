## Problem2 (https://leetcode.com/problems/coin-change-2/)

class Solution:
    def change(self, amount, coins):
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                    if i - coin >= 0:
                        dp[i] += dp[i-coin]
        return dp[-1] 


sol = Solution()
amount = 5
coins = [1,2,5]
print(sol.change(amount,coins))