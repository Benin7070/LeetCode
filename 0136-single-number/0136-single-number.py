class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=nums[0]
        n=len(nums)
        for i in range(1,n):
            
            res^=nums[i]
            print(res)
        return res