class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}
        def f(i):
            if i > n-1:
                return 0
            if i == n-1:
                return 1
            if nums[i] >= n-i-1:
                return 1
            if i in dp:
                return dp[i]
            summ = 0
            for j in range(1, min(n-i,nums[i]+1)):
                summ += f(i+j)
            dp[i] = 1 if summ > 0 else 0
            return dp[i]

        ans = f(0)
        return True if ans > 0 else False