class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        i=0
        j=len(s)-1
        while(j>i):
            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j-=1
            if s[i] in vowels and s[j] in vowels:
                tmp=s[i]
                s[i]=s[j]
                s[j]=tmp
                i+=1
                j-=1
        s=''.join(s)
        return s
        