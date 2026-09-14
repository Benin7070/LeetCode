class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        n=len(s)
        l=len(goal)
        if n!=l:
            return False
        for i in range(n):
            if goal[i]==s[0]:
                tmp=goal[i:]+goal[:i]
                if tmp==s:
                    return True
        return False
