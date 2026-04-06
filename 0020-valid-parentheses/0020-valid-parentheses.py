class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_tags=")]}"
        match_tags={")":"(","]":"[","}":"{"}
        flg=1

        for i in s:
            n=ord(i)
            if n==91 or n==123 or n==40:
                stack.append(i)
            else:
                if stack and stack[-1]==match_tags.get(i):
                    stack.pop()
                else:
                    flg=0
                    break
        if flg and not stack:
            return True
        else:
            return False