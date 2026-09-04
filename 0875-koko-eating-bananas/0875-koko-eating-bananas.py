import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res_final=0
        def check(i):
            res=0
            for j in piles:
                res+=(j + i - 1) // i
            if res<=h:
                return True
            return False

        while l<=r:
            mid=(l+r)//2
            if check(mid):
                res_final=mid
                r=mid-1
            else:
                l=mid+1
        return res_final
