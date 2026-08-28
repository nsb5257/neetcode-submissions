class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        dp={}
        def f(i,rem):
            if i >= n or rem < 0:
                return -1
            if (i,rem) in dp:
                return dp[(i,rem)]
            if rem == 0:
                return 0
            pick = f(i,rem-coins[i])
            notpick = f(i+1,rem)
            if pick == -1 and notpick == -1:
                dp[(i,rem)]=-1
                return -1
            if pick == -1:
                dp[(i,rem)] =notpick
                return notpick
            elif notpick == -1:
                dp[(i,rem)]=1+pick
                return 1+pick
            dp[(i,rem)]=min(1+pick,notpick)
            return dp[(i,rem)]

        return f(0,amount)
            


        
        