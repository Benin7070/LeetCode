class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=0
        right=0
        c=0
        if not s:
            return True
        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                right+=1
                left+=1
                c+=1
                if c==len(s):
                    return True
            else:
                right+=1
        return False
                