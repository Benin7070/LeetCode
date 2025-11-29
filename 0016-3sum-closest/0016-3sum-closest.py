class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        near_val=0
        diff_val=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                diff= abs(val-target)
                if diff<diff_val:
                    near_val=val
                    diff_val=diff
                if val>target:
                    right-=1
                else:
                    left+=1
        return near_val
        