class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff = start^goal
        if diff==0:
            return 0
        res=0
        while diff>0:
            if (diff&1)==1:
                res+=1
            diff>>=1

        return res
