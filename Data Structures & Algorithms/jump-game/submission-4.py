class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:
            return True
        rem_steps = nums[0]
        i = 0
        while rem_steps:
            i += 1
            if i >= n-1:
                return True
            rem_steps = max(rem_steps-1,nums[i])
        return False