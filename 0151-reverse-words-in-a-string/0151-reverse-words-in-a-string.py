class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        curr=""
        words=[]
        for i in s:
            if i!=" ":
                curr+=i
            else:
                if curr!="":
                    words.append(curr)
                    curr=""

        if curr:
                words.append(curr)

        return " ".join(words[::-1])