class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        count = Counter(s)
        st = set()
        st.add(s[0])
        i=0
        l = 0
        ans = []
        while i < n:
            while st:
                if s[i] not in st:
                    st.add(s[i])
                l+=1
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    st.remove(s[i])
                i+=1
                
            ans.append(l)
            if i == n:
                return ans
            l=0
            st = {s[i]}
            
        return ans



