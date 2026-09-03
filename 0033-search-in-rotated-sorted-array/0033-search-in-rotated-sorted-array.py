class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                pivot=i+1
                break
        if nums[pivot]==target:
            return pivot
        elif target>nums[pivot] and target>nums[n-1]:
            l=0
            r=pivot
        else:
            l=pivot+1
            r=n-1
        
        while l<=r:
            mid=(l+r)//2
            print(mid)
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1