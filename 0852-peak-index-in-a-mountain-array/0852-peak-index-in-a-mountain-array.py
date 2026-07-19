class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak=float('-inf')
        res=0
        for i in range(len(arr)):
            if arr[i]>peak:
                peak=arr[i]
                res=i
            else:
                break
        return res