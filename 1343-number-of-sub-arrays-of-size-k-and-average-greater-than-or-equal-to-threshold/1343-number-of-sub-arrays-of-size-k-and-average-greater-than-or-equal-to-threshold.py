class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        curr_sum=sum(arr[:k])
        if curr_sum>=threshold*k:
            res+=1
        for i in range(k,len(arr)):
            curr_sum+=arr[i]
            curr_sum-=arr[i-k]
            if curr_sum>=threshold*k:
                res+=1

        return res