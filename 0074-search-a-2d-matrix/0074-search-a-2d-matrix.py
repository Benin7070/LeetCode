class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=n-1
        if n>1:
            for i in range(n-1):
                if matrix[i][0]<=target and matrix[i+1][0]>target:
                    m=i
        t=matrix[m]
        l=0
        r=len(t)-1
        res=0
        while l<=r:
            mid=(l+r)//2
            if t[mid]==target:
                res=1
                break
            elif target>t[mid]:
                l=mid+1
            else:
                r=mid-1
        if res:
            return True
        else:
            return False
            