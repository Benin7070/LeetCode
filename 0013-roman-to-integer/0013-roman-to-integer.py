class Solution:
    def romanToInt(self, s: str) -> int:
        roman_chr={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)):
            print(i)
            if i+1<len(s) and roman_chr[s[i]]<roman_chr[s[i+1]]:
                res-=roman_chr[s[i]]
            else:
                res+=roman_chr[s[i]]
        return res
