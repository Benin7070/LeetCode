class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        curr=""
        for i in s:
            if i!=" ":
                curr+=i
            else:
                if curr!="":
                    if res=="":
                        res=curr
                    else:
                        res=curr+" "+res
                    
                    curr=""
        if curr!="":
            if res=="":
                res=curr
            else:
                res=curr+" "+res
        
        return res
