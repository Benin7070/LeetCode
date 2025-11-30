class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)

        num=[x for x in nums if x!=val]
        nums[:]=num
        
