class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=0
        i=1
        while True:
            m=(i*(i+1))//2
            if m<=n:
                res+=1
                i+=1
            else:
                break

        return res
