from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        pivot = -1
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        if pivot == -1:
            nums.reverse()
            return

        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                j = i
                break

        nums[pivot], nums[j] = nums[j], nums[pivot]

        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
