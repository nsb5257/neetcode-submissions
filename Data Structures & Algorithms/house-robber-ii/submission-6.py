class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def rob_arr(arr):
            l= len(arr)
            dp = [-1 for _ in range(l)]
            dp[0]=arr[0]
            if l>=2:
                dp[1]=max(arr[0],arr[1])
            for i in range(2,l):
                pick = arr[i] + dp[i-2]
                notpick = dp[i-1]
                dp[i] = max(pick,notpick)

            return dp[l-1]

        return max(rob_arr(nums[:n-1]),rob_arr(nums[1:]))