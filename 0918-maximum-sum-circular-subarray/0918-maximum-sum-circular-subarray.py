class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return None
        g_max=g_min=nums[0]
        curr_max=curr_min=nums[0]
        ttl=sum(nums)
        for i in nums[1:]:
            curr_max=max(curr_max+i,i)
            
            g_max=max(g_max,curr_max)

            curr_min=min(curr_min+i,i)

            g_min=min(g_min,curr_min)

        if g_max>0:
            res=max(ttl-g_min,g_max)

        else:
            res=g_max
        return res