class Solution:
    def __init__(self):
        self.dp={}
    def numTrees(self, n: int) -> int:
        res=0
        if n<=1:
            return 1
        for i in range(1,n+1):
            if i-1 not in self.dp:
                left=self.numTrees(i-1)
                self.dp[i-1]=left
            else:
                left=self.dp[i-1]
            if n-i not in self.dp:
                right=self.numTrees(n-i)
                self.dp[n-i]=right
            else:
                right=self.dp[n-i]
            res+=(left*right)

        return res