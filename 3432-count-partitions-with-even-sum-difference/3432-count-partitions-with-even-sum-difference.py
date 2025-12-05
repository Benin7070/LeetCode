class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(1,len(nums)):
            if(abs(sum(nums[0:i])-sum(nums[i:n]))%2==0):
                count+=1
        return count
        