class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp=[[0,0] for _ in range(n+2)]
        x,y,z,w=0,0,0,0
        for i in range(n-1,-1,-1):
            w = x
            xn = max(-prices[i]+y,x)
            yn = max(prices[i]+z,y)
            x = xn
            y = yn
            z = w

        return x