class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res_li=[]
        for i in range(m):
            res_li.append(nums1[i])
            print(res_li)
        for j in range(n):
            res_li.append(nums2[j])
        nums1[:]=sorted(res_li)
        