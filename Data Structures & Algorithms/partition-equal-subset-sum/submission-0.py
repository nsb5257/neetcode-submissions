class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp={}
        def f(i,l,r):
            if i >= n:
                return False
            if l == r:
                return True
            if (i,l,r) in dp:
                return dp[(i,l,r)]
            pick = f(i+1,l+nums[i],r-nums[i])
            notpick = f(i+1,l,r)
            dp[(i,l,r)] = pick or notpick
            return pick or notpick
        
        return f(0,0,sum(nums))