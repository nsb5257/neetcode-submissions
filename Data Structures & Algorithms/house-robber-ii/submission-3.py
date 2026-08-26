class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [[-1,-1] for _ in range(n)]

        def f(i,zeroselected):
            if i >= n:
                return 0
            if dp[i][zeroselected] != -1:
                return dp[i][zeroselected]
            if zeroselected and i == n-1:
                return 0
            if i == 0:
                pick = nums[i]+f(i+2,True)
                notpick = f(i+1,False)
                dp[i][True] = pick
                dp[i][False]=notpick
                return max(pick,notpick)
            pick = nums[i]+f(i+2,zeroselected)
            notpick = f(i+1,zeroselected)
            dp[i][zeroselected] = max(pick,notpick)
            return dp[i][zeroselected]

        return f(0,True)