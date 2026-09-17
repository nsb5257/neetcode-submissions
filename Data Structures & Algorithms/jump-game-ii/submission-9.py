class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        mini = 0
        level_start,level_end=0,0
        while n-1 not in range(level_start,level_end+1):
            x = level_end
            for j in range(level_start,x+1):
                level_end = max(level_end,j+nums[j])
            level_start = x+1
            mini += 1
        return mini

        
                    
        