class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xors=0
        for num in nums:
            xors ^=num

        lowbit= xors & -xors

        res=[0,0]
        for num in nums:
            if num & lowbit:
                res[0] ^=num
            else:
                res[1] ^=num
            
        return res