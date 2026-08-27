class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        st = set()
        for i in range(65,91):
            st.add(str(i-64))
        dp = [-1 for _ in range(n)]
        def decodings(i):
            if i >= n:
                return 1
            if s[i]=="0":
                return 0
            if dp[i] != -1:
                return dp[i]
            path1 = 1*decodings(i+1) if s[i] in st else 0
            path2 = 1*decodings(i+2) if i+1 <= (n-1) and s[i:i+2] in st else 0
            dp[i]= path1+path2
            return path1 + path2
                
        return decodings(0)