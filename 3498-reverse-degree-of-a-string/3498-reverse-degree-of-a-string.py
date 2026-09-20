class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            res+=(123-ord(s[i]))*(i+1)

        return res