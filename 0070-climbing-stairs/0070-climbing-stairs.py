class Solution:
    def climbStairs(self, n: int) -> int:
        fib=[0,1]
        if n==1:
            return fib[1]
        else:
            for i in range(n):
                fib.append(fib[-2]+fib[-1])

            return fib[-1]