class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[tmp] = nums[i]
                tmp += 1
        return tmp
