class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        num1=0
        num2=0
        res=[]
        n=len(digits)
        for i in range(n):
            for j in range(n):
                if j!=i:
                    for k in range(n):
                        if k!=i and k!=j:
                            r=(digits[i]*100)+(digits[j]*10)+digits[k]
                            if r%2==0 and r>99 and r not in res:
                                print(r)
                                res.append(r)
        return len(res)