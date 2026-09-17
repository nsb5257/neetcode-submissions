class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp={}
        def f(i):
            if i >= n-1:
                return 0
            if i in dp:
                return dp[i]
            x = n+1
            for j in range(1,min(nums[i]+1,n-i)):
                x = min(x,1+f(i+j))
            dp[i]=x
            return x
        
        return f(0)