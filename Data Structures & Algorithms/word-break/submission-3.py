class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dummy=""
        dp={}
        def f(i,d):
            if i >=n:
                return True if d == "" else False
            if (i,d) in dp:
                return dp[(i,d)]
            d += s[i]
            if d in wordDict:
                clear = f(i+1,"")
                notclear = f(i+1,d)
                dp[(i,d)] = clear or notclear
                return dp[(i,d)]
            dp[(i+1,d)] = f(i+1,d)
            return dp[(i+1,d)]
        
        return f(0,"")