class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numss=[]
        for i in nums:
            if i not in numss:
                numss.append(i)
        nums[:]=numss