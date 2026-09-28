class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin,cmax = 0,0

        for c in s:
            if c == '(':
                cmin+=1
                cmax+=1
            elif c == ')':
                cmin-=1
                cmin = max(0,cmin)
                cmax-=1
                if cmax < 0:
                    return False
            else:
                cmin -= 1
                cmin = max(0,cmin)
                cmax += 1
        
        return True if cmin == 0 else False