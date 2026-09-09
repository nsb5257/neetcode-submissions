class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1+n2 != n3:
            return False
        dp={}
        def f(l,r):
            if (l,r) in dp:
                return dp[(l,r)]
            if l >= n1:
                dp[(l,r)] = True if s3[l+r:] == s2[r:] else False
                return dp[(l,r)]
            if r >= n2:
                dp[(l,r)] = True if s3[l+r:] == s1[l:] else False
                return dp[(l,r)]
            if s1[l] == s3[l+r] and s2[r] == s3[l+r]:
                dp[(l,r)] = f(l+1,r) or f(l,r+1)
                return dp[(l,r)]
            if s1[l] == s3[l+r]:
                dp[(l,r)] = f(l+1,r)
                return dp[(l,r)] 
            if s2[r] == s3[l+r]:
                dp[(l,r)] = f(l,r+1)
                return dp[(l,r)] 
            return False

        return f(0,0)

            
                
