import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def f(i,p):
            if i >= n:
                return 0
            if (i,p) in dp:
                return dp[(i,p)]
            notpick = f(i+1,p)
            ans = notpick
            if p == -1 or nums[p] < nums[i]:
                pick = 1+f(i+1,i)
                ans = max(pick,ans)
                
            dp[(i,p)] = ans
            return ans

        return f(0,-1)