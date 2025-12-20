class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        n=len(s)
        res=""
        cycle=2*numRows-2
        for r in range(numRows):
            idx=r
            while idx<n:
                res+=s[idx]
                if r!=0 and r!=numRows-1:
                    up_idx=idx+2*(numRows-r-1)
                    if up_idx<n:
                        res+=s[up_idx]
                idx+=cycle
        return res