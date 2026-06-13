class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        curr_sum=0
        if len(nums)==0:
            return 0
        for i in nums:
            res=curr_sum+i
            if max_sum<res:
                max_sum=res
            if res>0:
                curr_sum+=i
            else:
                curr_sum=0
            print(i,curr_sum,res)
        return max_sum
            