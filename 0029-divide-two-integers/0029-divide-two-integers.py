class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int, min_int = 2**31 - 1, -2**31
        if dividend == min_int and divisor == -1:
            return max_int
        positive = (dividend > 0) == (divisor > 0)
        a=abs(dividend)
        b=abs(divisor)
        ans= 0
        while a >= b:
            shift = 0
            while a >= (b << (shift + 1)):
                shift += 1
            a -= (b << shift)
            ans += (1 << shift)
        return ans if positive else -ans