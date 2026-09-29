import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 or (n>1 and n&(n-1)==0):
            return True
        return False