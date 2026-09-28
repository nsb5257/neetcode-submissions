class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort()

        prev_interval = intervals[0]
        ans = []
        for i in range(1,n):
            if prev_interval[1] < intervals[i][0]:
                ans.append(prev_interval)
                prev_interval = intervals[i]
            else:
                prev_interval = [min(prev_interval[0],intervals[i][0]),max(prev_interval[1],intervals[i][1])]
            
        ans.append(prev_interval)
        return ans

