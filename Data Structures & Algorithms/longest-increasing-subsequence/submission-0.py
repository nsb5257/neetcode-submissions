class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Every element is an LIS of at least length 1
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                # If strictly increasing, can we make a longer sequence?
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)