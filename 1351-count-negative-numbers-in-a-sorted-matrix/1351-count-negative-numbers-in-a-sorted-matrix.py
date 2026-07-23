class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        m=len(grid[0])
        for i in grid:

            l=0
            r=m-1
            if i[l]<0:
                res+=m
                continue
            elif i[r]>0:
                continue
            while l<r:
                mid=(l+r)//2
                if i[mid]>=0:
                    l=mid+1
                elif i[mid]<0:

                    res+=((r-mid)+1)
                    r=mid-1

                

            if l==r and i[l]<0:
                res+=1
        return res