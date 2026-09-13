class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        tracker = 0
        for num in nums:
            tracker += num
            maxi = max(maxi,tracker)
            if tracker <= 0:
                tracker = 0

        return maxi