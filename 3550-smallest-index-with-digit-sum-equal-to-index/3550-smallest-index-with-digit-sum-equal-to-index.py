class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            n=0
            tmp=nums[i]
            while tmp>0:
                n+=tmp%10
                tmp=tmp//10
            print(n)

            if i==n:
                return i
        return -1
