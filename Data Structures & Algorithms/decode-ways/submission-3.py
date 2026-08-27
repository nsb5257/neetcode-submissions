class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        st = set()
        for i in range(65,91):
            st.add(str(i-64))
        ans = 0
        dp = {}
        def decodings(string):
            if string in dp:
                return dp[string]
            l = len(string)
            if l==0:
                return 1
            if l == 1:
                if string == "0":
                    return 0
                return 1
            # if l == 2:
            #     if string[0]=="0":
            #         return 0
            #     if string[1] =="0":
            #         if string not in st:
            #             return 0
            #         return 1
            #     x = 2
            #     if string not in st:
            #         x-=1
            #     return x
            i=0
            path1 = 1*decodings(string[i+1:]) if string[i] in st else 0
            path2 = 1*decodings(string[i+2:]) if string[i:i+2] in st else 0
            dp[string]= path1+path2
            return path1 + path2
                
        return decodings(s)