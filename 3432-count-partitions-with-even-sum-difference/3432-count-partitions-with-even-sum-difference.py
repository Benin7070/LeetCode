class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        #n=len(nums)
        for i in range(1,len(nums)):
            #li=nums[0:i]
            #li_2=nums[i+1,]
            #print(sum(nums[0:i]),sum(nums[i+1:len(nums)-1]))
            #print(nums[i:len(nums)])
            if(abs(sum(nums[0:i])-sum(nums[i:len(nums)]))%2==0):
                count+=1
        
        return count
        