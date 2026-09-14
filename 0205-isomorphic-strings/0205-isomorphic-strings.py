class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        already_mapped={}

        for i in range(len(s)):
            tmp=already_mapped.get(s[i])
            if tmp:
                if tmp!=t[i]:
                    return False
            else:
                if s[i] in already_mapped.keys() or t[i] in already_mapped.values():
                    return False
                already_mapped[s[i]]=t[i]
                print(already_mapped[s[i]],i)
        return True

