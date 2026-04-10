class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        l = len(nums)

        pivot = -1
        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        for i in range(l - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        res = int("".join(nums))
        return res if res < 2**31 else -1