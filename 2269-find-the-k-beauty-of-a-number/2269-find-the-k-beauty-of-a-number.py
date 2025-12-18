class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_dup=str(num)
        res=0
        for i in range(len(num_dup)-k+1):
            cur_window=int(num_dup[i:i+k])
            if cur_window!=0 and num%cur_window==0:
                res+=1
        return res