class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        prev=nums[0]
        for i in range(1,n):
            if nums[i]==prev:
                return nums[i]
            else:
                prev=nums[i]
            