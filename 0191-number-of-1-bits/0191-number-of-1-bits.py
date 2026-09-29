class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            print(n)
            if n%2!=0:
                res+=1
            n=n>>1
        return res