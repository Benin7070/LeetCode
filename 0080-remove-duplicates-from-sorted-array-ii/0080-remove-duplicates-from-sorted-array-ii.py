class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numss=[]
        for i in nums:
            if numss.count(i)<2:
                numss.append(i)
        nums[:]=numss