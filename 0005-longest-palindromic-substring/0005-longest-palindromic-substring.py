class Solution:
    def longestPalindrome(self, s: str) -> str:
        p=""
        ma=0
        ans=""
        for i in range(len(s)):
            p=""
            for j in range(i,len(s)):
               p=p+s[j]
               if p==p[::-1]:
                if len(p)>ma:
                    ans=p
                    ma=len(ans)
        return ans


