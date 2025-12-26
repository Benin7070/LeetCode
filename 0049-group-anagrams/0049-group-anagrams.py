class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        while strs:
            curr_res=[]
            curr_res.append(strs[0])
            curr_el=sorted(strs[0])
            curr_el_ln=len(strs[0])
            strs.pop(0)

            for el in strs:
                if curr_el_ln != len(el):
                    f=0
                    continue
                if sorted(el)==curr_el:
                    curr_res.append(el)
                curr_res.sort()
            res.append(curr_res)
            for ch in curr_res:
                if ch in strs:
                    strs.remove(ch)
        return res
        #         for j,char in enumerate(el):
        #             if char not in tmp or tmp[char]<=0:
        #                 f=0
        #                 break
        #             else:
        #                 tmp[char]-=1
        #         if f==1:
        #             curr_res.append(el)
            
                    
                

            
            