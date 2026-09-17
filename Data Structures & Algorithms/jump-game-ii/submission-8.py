class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp={}
        def f(level_start,level_end):
            if n-1 in range(level_start,level_end+1):
                return 0
            x = level_end
            for j in range(level_start,x+1):
                level_end = max(level_end,j+nums[j])

            return 1+f(x+1,level_end)
                    
        return f(0,0)