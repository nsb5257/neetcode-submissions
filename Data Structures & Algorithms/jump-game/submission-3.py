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
            if rem_steps > nums[i]:
                rem_steps -= 1
            else:
                rem_steps = nums[i]

        return False