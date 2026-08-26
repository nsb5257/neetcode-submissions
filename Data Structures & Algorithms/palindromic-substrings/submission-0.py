class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        def finpalindrome(i):
            count = 0
            l = i
            r = i
            while l>=0 and r<n and s[l]==s[r]:
                count += 1
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count

        for c in range(0,n-1):
            cnt += finpalindrome(c)
        return cnt+1