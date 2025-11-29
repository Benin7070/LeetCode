from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_li = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):             
            if i > 0 and nums[i] == nums[i - 1]:
                continue                    
            left, right = i + 1, n - 1    
            while left < right:         
                val = nums[i] + nums[left] + nums[right]

                if val == 0:
                    res_li.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1

        return res_li
