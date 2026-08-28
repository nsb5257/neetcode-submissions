class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        dp={}
        def f(i,rem):
            if i >= n or rem < 0:
                return math.inf
            if (i,rem) in dp:
                return dp[(i,rem)]
            if rem == 0:
                return 0
            pick = f(i,rem-coins[i])
            notpick = f(i+1,rem)
            dp[(i,rem)]=min(1+pick,notpick)
            return dp[(i,rem)]

        ans = f(0,amount)
        return ans if ans != math.inf else -1
            


        
        