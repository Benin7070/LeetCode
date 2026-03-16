from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        pivot = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return

        for j in range(n-1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[j], nums[pivot] = nums[pivot], nums[j]
                break

        nums[pivot+1:] = reversed(nums[pivot+1:])