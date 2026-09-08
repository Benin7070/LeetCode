import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        # final=[]
        # for i in range(l,r):
        #     res=0
        #     for j in nums:
        #         res+=math.ceil(j/i)
        #     final.append(res)
        # print(final)
        # return 0


        def check(num):
            res=0
            for i in nums:
                res+=math.ceil(i/num)

            return res


        while l<r:
            mid=(l+r)//2
            res=check(mid)

            if res<=threshold:
                r=mid
            else:
                l=mid+1
            
        return l
