class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res_li=[]
        if target in nums:
            num=nums.index(target)
            res_li.append(num)
            nums.reverse()
            num=nums.index(target)
            res_li.append(len(nums)-1-num)
        else:
            res_li+=[-1,-1]
        return res_li