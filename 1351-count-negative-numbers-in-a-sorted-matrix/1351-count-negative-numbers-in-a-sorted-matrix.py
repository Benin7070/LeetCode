class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        m=len(grid[0])
        for i in grid:
            print(i)
            l=0
            r=m-1
            if i[l]<0:
                res+=m
                continue
            elif i[r]>0:
                continue
            while l<r:
                mid=(l+r)//2
                print(i[mid])
                if i[mid]>=0:
                    l=mid+1
                elif i[mid]<0:
                    print(res)
                    res+=((r-mid)+1)
                    print(res)
                    r=mid-1

                

            if l==r and i[l]<0:
                res+=1
        return res