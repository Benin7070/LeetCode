class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        key=0
        for i in range(len(nums)):
            if key<2 or nums[i]!=nums[key-2]:
                nums[key]=nums[i]
                key+=1
        return key