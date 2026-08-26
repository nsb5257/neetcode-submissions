class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        def findlongestpalindrome(i):
            l = i
            r = i
            while s[l]==s[r]:
                if l==0 or r == n-1:
                    l-=1
                    r+=1
                    break
                l-=1
                r+=1
            p1 = s[l+1:r]
            l=i
            r=i+1
            while s[l]==s[r]:
                if l==0 or r == n-1:
                    l-=1
                    r+=1
                    break
                l-=1
                r+=1
            p2 = s[l+1:r]
            return p2 if len(p2)>=len(p1) else p1

        for c in range(0,n-1):
            x = findlongestpalindrome(c)
            ans = x if len(x) >= len(ans) else ans
        return ans
            