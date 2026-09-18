class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        res=0
        neg=0
        digit_reached=0
        INT_MIN = -2**31     
        INT_MAX = 2**31 - 1
        for i in range(n):
            if s[i].isdigit():
                res=(res*10)+int(s[i])
                digit_reached=1
            elif not digit_reached:
                if s[i]=="-":
                    neg=1
                    digit_reached=1
                elif s[i]=="+":
                    digit_reached=1
                    pass
                elif s[i]!=" ":
                    break
            else:
                break
            print(res)

        if neg:
            res*=-1
        return max(INT_MIN,min(res,INT_MAX))