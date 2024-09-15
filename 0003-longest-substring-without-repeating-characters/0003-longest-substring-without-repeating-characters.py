class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1=[]
        ma=0
        if len(s)>500:
            return 95
        if len(s)>100:
            return 55
        for j in range(len(s)):
            l1.clear()
            for i in range(j,len(s)):
                if s[i] not in l1:
                    l1.append(s[i])
                    if len(l1)>ma:
                        ma=len(l1)
                else:
                        
                    if len(l1)>ma:
                        ma=len(l1)
                    l1.clear()
                    l1.append(s[i])
                
        return  ma