## Problem1(https://leetcode.com/problems/paint-house/)
class Solution:
    def minCost(self, costs):
        dp = [0, 0, 0]

        # Iterate over each house
        for cost in costs:
            # Store the current values of dp to avoid overwriting issues
            prev_dp = dp[:]
            # Calculate the new costs for painting the current house
            dp[0] = cost[0] + min(prev_dp[1], prev_dp[2])
            dp[1] = cost[1] + min(prev_dp[0], prev_dp[2])
            dp[2] = cost[2] + min(prev_dp[0], prev_dp[1])

        # Return the minimum cost to paint all houses
        return min(dp)

sol = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(sol.minCost(costs))
