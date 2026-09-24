class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l):
            n=0
        
            while nums[i]>0:
                n+=nums[i]%10
                nums[i]=nums[i]//10

            if i==n:
                return i
        return -1
