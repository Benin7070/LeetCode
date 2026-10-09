class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        res=0
        j=0
        n=len(s)
        g=sorted(g)
        s=sorted(s)

        i=j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                res+=1
                i+=1

            j+=1
        return res