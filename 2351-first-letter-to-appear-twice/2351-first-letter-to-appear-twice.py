class Solution:
    def repeatedCharacter(self, s: str) -> str:
        li=[]
        for i in s:
            if i not in li:
                li.append(i)
            else:
                return i