class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dp = {}
        def f(i,j):
            if i<0 or j<0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if text1[i]==text2[j]:
                return 1+f(i-1,j-1)

            x,y = f(i-1,j),f(i,j-1)
            dp[(i,j)]= max(x,y)
            return dp[(i,j)]

        return f(n-1,m-1)