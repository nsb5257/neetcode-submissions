class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])
        dp={}
        dirs = [[-1,0],[0,1],[0,-1],[1,0]]

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r not in range(n) or c not in range(m):
                return 0
            maxi = 1
            for dr,dc in dirs:
                x,y=r+dr,c+dc
                a = 1
                if x in range(n)and y in range(m) and matrix[x][y] > matrix[r][c]:
                    a += dfs(x,y)
                maxi = max(maxi,a)
            dp[(r,c)] = maxi
            return maxi
        for i in range(n):
            for j in range(m):
                dfs(i,j)
        return max(dp.values())
        