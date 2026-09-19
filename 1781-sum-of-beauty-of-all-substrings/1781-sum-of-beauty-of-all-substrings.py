class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            curr={s[i]:1}
            for j in range(i+1,len(s)):
                curr[s[j]]=curr.get(s[j],0)+1

                freq=curr.values()
                
                res+=max(freq)-min(freq)
               

        return res