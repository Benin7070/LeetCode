class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        res=None
        while i+1<len(nums):
            if nums[i]==nums[i+1]:
                i+=2
            else:
                res=nums[i]
                break
        if i<len(nums):
            res=nums[i]

        return res
