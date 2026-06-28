class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        max_freq=0
        max_val=None
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>max_freq:
                max_freq=freq.get(i)
                max_val=i
        return max_val
        