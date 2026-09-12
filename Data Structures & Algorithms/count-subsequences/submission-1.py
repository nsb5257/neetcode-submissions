class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        if m>n:
            return 0
        dp={}
        def f(i,j):
            if j >= m:
                return 1
            if i>=n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            notpick = f(i+1,j)
            pick = 0
            if s[i]==t[j]:
                pick = f(i+1,j+1)
            dp[(i,j)] = pick+notpick
            return dp[(i,j)]

        return f(0,0)

