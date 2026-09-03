class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s%2 == 1:
            return False
        dp={}
        def f(i,l):
            if l == s/2:
                return True
            if i >= n:
                return False
            if (i,l) in dp:
                return dp[(i,l)]
            pick = f(i+1,l+nums[i])
            notpick = f(i+1,l)
            dp[(i,l)] = pick or notpick
            return pick or notpick
        
        return f(0,0)