class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def rob_arr(arr):
            l= len(arr)
            prev = max(arr[0],arr[1]) if l>=2 else arr[0]
            pprev = arr[0]
            for i in range(2,l):
                pick = arr[i] + pprev
                notpick = prev
                curr = max(pick,notpick)
                prev = curr
                pprev = notpick

            return prev

        return max(rob_arr(nums[:n-1]),rob_arr(nums[1:]))