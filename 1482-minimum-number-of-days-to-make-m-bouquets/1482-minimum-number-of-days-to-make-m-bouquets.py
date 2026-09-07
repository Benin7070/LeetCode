class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1

        l=min(bloomDay)
        r=max(bloomDay)

        def check(day):
            consecutive=0
            bouquet=0
            for i in bloomDay:
                if i<=day:
                    consecutive+=1
                    if consecutive==k:
                        bouquet+=1
                        consecutive = 0
                else:
                    consecutive=0
                    

            return bouquet>=m


        while l<r:
            mid=l+(r-l)//2
            if check(mid):
                r=mid
            else:
                l=mid+1

        return l