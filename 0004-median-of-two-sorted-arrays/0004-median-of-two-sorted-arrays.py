class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        a=len(nums1)//2
        ans=(nums1[a-1]+nums1[a])/2

        return nums1[a] if len(nums1)%2==1 else float(ans)
        