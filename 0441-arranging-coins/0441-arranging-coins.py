class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=0
        sub=1
        while n:
            n-=sub
            if n>=0:
                sub+=1
                res+=1
            else:
                break
        return res
