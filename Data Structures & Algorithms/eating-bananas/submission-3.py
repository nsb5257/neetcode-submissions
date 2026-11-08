class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(k):
            hours = sum(math.ceil(pile/k) for pile in piles)
            return hours <= h 
        
        l,r = 1, max(piles)
        res = r
        while l<=r:
            mid= (l+r)//2
            if can_eat(mid):
                res = mid
                r = mid-1
            else:
                l = mid + 1
        return res