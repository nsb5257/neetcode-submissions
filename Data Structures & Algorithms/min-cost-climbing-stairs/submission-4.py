class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        x=y=0
        for i in range(2,n+1):
            z = min(cost[i-1]+x,cost[i-2]+y)
            y=x
            x=z

        return z

        