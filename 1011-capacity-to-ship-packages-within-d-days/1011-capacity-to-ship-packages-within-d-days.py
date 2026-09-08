class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)

        def possible(w):
            d=1
            temp=0

            for i in weights:
                if temp + i > w:
                    d += 1
                    temp = i
                else:
                    temp += i

            return d
        
        while l<r:

            mid=(l+r)//2
            if possible(mid)<=days:
                r=mid
            else:
                l=mid+1
        return l
        