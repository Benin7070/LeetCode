class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colr_freq={0:0,1:0,2:0}
        for i in nums:
            colr_freq[i]=colr_freq.get(i)+1
        j=0
        for keys,values in colr_freq.items():
            for i in range(values):
                nums[j]=keys
                j+=1
        