class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp={}
        def f(i,rem):
            if i >= n:
                if rem == 0:
                    return 1
                return 0
            if (i,rem) in dp:
                return dp[(i,rem)]
            notpick = f(i+1,rem)
            pick = 0
            if coins[i] <= rem:
                pick = f(i,rem-coins[i])
            dp[(i,rem)] = pick + notpick
            return dp[(i,rem)]
        
        return f(0,amount)