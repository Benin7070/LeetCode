class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(num):
            cur_sum=0
            p=1
            for i in nums:
                if cur_sum+i<=num:
                    cur_sum+=i
                else:
                    cur_sum=i
                    p+=1
            if p<=k:
                return True
            else:
                return False
        l=max(nums)
        r=sum(nums)

        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return r