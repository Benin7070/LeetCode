class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        once=0
        twos=0
        for num in nums:
            once = (once^ num) & ~twos
            twos =(twos^ num) & ~once

        return once