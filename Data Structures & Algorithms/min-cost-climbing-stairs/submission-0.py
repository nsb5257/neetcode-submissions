class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        dp[0]=dp[1]=0
        def recurse(i):
            if dp[i]!=-1:
                return dp[i]
            dp[i]=min(cost[i-1]+recurse(i-1),cost[i-2]+recurse(i-2))
            return dp[i]

        return recurse(n)