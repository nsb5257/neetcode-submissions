class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0
        ans =0
        intervals.sort()
        prev_end = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prev_end:
                prev_end=end
            else:
                ans += 1
                prev_end = min(end,prev_end)
        return ans
            
        