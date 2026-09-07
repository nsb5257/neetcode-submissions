class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp={}
        def f(i,bought):
            if i>=n:
                return 0
            if (i,bought) in dp:
                return dp[(i,bought)]
            if not bought:
                buy = -prices[i]+f(i+1,True)
                notbuy = f(i+1,False)
                dp[(i,bought)]=max(buy,notbuy)
                return dp[(i,bought)]
            if bought:
                sell = prices[i]+f(i+2,False)
                notsell = f(i+1,True)
                dp[(i,bought)]=max(sell,notsell)
                return dp[(i,bought)]

        return f(0,False)