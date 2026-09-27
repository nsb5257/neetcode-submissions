class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        st = set([0,1,2])

        for t in triplets:
            if t[0] > target[0] or t[1] >target[1] or t[2] > target[2]:
                continue
            
            for i in st.copy():
                if t[i] == target[i]:
                    st.remove(i)
            if not st:
                return True
        
        return False