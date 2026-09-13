class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2 = len(word1),len(word2)
        dp={}
        def f(i,j):
            if i == n1 and j == n2:
                return 0
            if i == n1 and j < n2:
                return n2-j
            if j == n2 and i < n1:
                return n1 - i
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] == word2[j]:
                dp[(i,j)] = f(i+1,j+1)
                return dp[(i,j)]
            inse = 1+f(i,j+1)
            dele = 1+f(i+1,j)
            replace = 1 + f(i+1,j+1)
            dp[(i,j)] = min(inse,dele,replace)
            return dp[(i,j)]

        return f(0,0)