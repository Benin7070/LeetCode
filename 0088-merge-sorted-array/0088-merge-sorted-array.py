class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=j=0
        temp=nums1.copy()
        nums1.clear()
        while i<m and j<n:
            if temp[i]<nums2[j]:
                nums1.append(temp[i])
                i+=1
            elif temp[i]>nums2[j]:
                nums1.append(nums2[j])
                j+=1
            elif temp[i]==nums2[j]:
                nums1.append(temp[i])
                nums1.append(nums2[j])
                i+=1
                j+=1

        if i<m:
            for k in range(m-i):
                nums1.append(temp[k+i])
        if j<n:
            for k in range(n-j):
                nums1.append(nums2[k+j])