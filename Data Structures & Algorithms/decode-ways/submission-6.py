class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        st = set()
        for i in range(65,91):
            st.add(str(i-64))
        dp = [0 for _ in range(n+1)]
        dp[n]=1
        i=n-1
        while i>=0:
            if s[i]=="0":
                i-=1
                continue
            path1 = 1*dp[i+1]
            path2 = 1*dp[i+2] if i<n-1 and s[i:i+2] in st else 0
            dp[i] = path1+path2
            i-=1
        return dp[0]