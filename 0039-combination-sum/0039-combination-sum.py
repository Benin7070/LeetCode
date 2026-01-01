class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        for i in candidates:
            cur_res=[]  
            if i<=target:
                times=target//i
                rem=target%i
                while rem not in candidates and times>1:
                    times-=1
                    rem+=i
                if (rem in candidates or rem==0) and (i*times)+rem==target:
                    cur_res=[i]*times
                    if rem!=0:
                        cur_res.append(rem)
                    if sorted(cur_res) not in res:
                        res.append(cur_res)
        return res