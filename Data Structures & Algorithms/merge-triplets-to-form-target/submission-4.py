class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0,0,0]

        for t in triplets:
            if t[0] > target[0] or t[1] >target[1] or t[2] > target[2]:
                continue

            for i in range(3):
                if ans[i]:
                    continue
                if t[i] == target[i]:
                    ans[i]=1
        
        return True if sum(ans) == 3 else False