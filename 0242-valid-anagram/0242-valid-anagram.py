class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        if len(s) != len(t):
            return False
        else:
            for i, char in enumerate(s):
                if char not in c:
                    c[char]=1
                else:
                    c[char]+=1
            for i, char in enumerate(t):
                if c.get(char,0)<=0:
                    return False
                else:
                    c[char]-=1
            return True