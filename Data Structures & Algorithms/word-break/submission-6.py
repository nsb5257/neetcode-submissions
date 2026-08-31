class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordset = set(wordDict)
        dp={}
        def f(i,d):
            if i >=n:
                return True if d == "" else False
            if (i,d) in dp:
                return dp[(i,d)]
            dd = d + s[i]
            if dd in wordset:
                clear = f(i+1,"")
                notclear = f(i+1,dd)
                dp[(i,d)] = clear or notclear
                return dp[(i,d)]
            dp[(i,d)] = f(i+1,dd)
            return dp[(i,d)]
        
        return f(0,"")