class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp={}
        def f(i,rem):
            if i >= n:
                if rem == 0:
                    return 1
                return 0
            if (i,rem) in dp:
                return dp[(i,rem)]
            add = f(i+1,rem+nums[i])
            sub = f(i+1,rem-nums[i])
            dp[(i,rem)] = add+sub
            return dp[(i,rem)]

        return f(0,target)