class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        i=0
        while strs:
            curr_res=[]
            c={}
            for j,char in enumerate(strs[i]):
                if char not in c:
                    c[char]=1
                else:
                    c[char]+=1
            curr_res.append(strs[i])
            el_l=len(strs[i])
            strs.pop(i)

            for el in strs:
                tmp=c.copy()
                f=1
                if el_l != len(el):
                    f==0
                    continue
                for j,char in enumerate(el):
                    if char not in tmp or tmp[char]<=0:
                        f=0
                        break
                    else:
                        tmp[char]-=1
                if f==1:
                    curr_res.append(el)
            curr_res.sort()
            res.append(curr_res)
            for ch in curr_res:
                if ch in strs:
                    strs.remove(ch)
        return res
                    
                

            
            