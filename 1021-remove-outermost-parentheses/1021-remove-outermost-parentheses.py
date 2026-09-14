class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        res=""
        for i in s:
            if i=="(":
                stack.append(i)
                if len(stack)>1:
                    res+="("
            else:

                if len(stack)==1:
                    stack=[]
                else:
                    stack.pop()
                    res+=")"


        return res
