class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i in range(len(digits)-1,-1,-1):
            ans+=digits[(len(digits)-1)-i]*(10**i)
        ans+=1
        ans_lst=list(map(int,str(ans)))
        return ans_lst