class Solution:
    def __init__(self):
        self.dp={}
    def numTrees(self, n: int) -> int:
        res=0
        if n<=1:
            return 1
        if n in self.dp:
            return self.dp[n]
        for i in range(1,n+1):
            left=self.numTrees(i-1)
            self.dp[i-1]=left
            right=self.numTrees(n-i)
            self.dp[n-i]=right

            res+=(left*right)

        return res