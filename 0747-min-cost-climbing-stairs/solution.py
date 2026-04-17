class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        # dp[n] と dp[n+1] を使うので n+2 必要
        dp = [0] * (n + 2)

        i = n - 1
        while i >= 0:
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
            i -= 1

        return min(dp[0], dp[1])

