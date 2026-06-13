class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        curr_sum=0
        if len(nums)==0:
            return 0
        for i in nums:
            if max_sum<curr_sum+i:
                max_sum=curr_sum+i
            if curr_sum+i>0:
                curr_sum+=i
            else:
                curr_sum=0

        return max_sum
            