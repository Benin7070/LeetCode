class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        n=len(nums)
        res=set()
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>(n/3):
                res.add(i)

        return list(res)