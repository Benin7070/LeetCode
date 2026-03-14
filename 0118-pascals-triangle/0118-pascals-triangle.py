class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            res=[[1]]
            return res
        elif numRows==2:
            res=[[1],[1,1]]
            return res
        else:
            res=[[1],[1,1]]
            for i in range(2,numRows):
                cur_res=[]
                for j in range(i+1):
                    if j==0 or j==i:
                        cur_res.append(1)
                    else:
                        prev=res[i-1][j-1]
                        aft=res[i-1][j]
                        r=prev+aft
                        cur_res.append(r)
                res.append(cur_res)
            return res
