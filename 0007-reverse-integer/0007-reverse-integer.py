class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        s=str(abs(x))
        l=list(s)
        if x>0:
            for i in range(len(l),0,-1):
                if i=="0":
                    l.pop()
                else:
                    l.reverse()
                    a=int("".join(l))
                    if a<(2**31)-1:
                        return a
                    else:
                        return 0

        if x<0:
            for i in range(len(l),0,-1):
                if i=="0":
                    l.pop()
                else:
                    l.reverse()
                    a=int('-'+"".join(l))
                    if a>-2**31: 
                        return a
                    else:
                        return 0