import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for num in nums:
            # Find the index of the first element in 'sub' >= num
            i = bisect.bisect_left(sub, num)
            
            # If 'num' is larger than everything, it extends the LIS
            if i == len(sub):
                sub.append(num)
            # Otherwise, replace to keep the sequence elements as small as possible
            else:
                sub[i] = num
                
        return len(sub)