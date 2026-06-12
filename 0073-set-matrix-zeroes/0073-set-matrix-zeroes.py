class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        def make_zero(row,col):
            for k in range(m):
                matrix[row][k]=0
            for l in range(n):
                matrix[l][col]=0
        zeros=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zeros.append([i,j])


        for i in zeros:
            make_zero(i[0],i[1])

        print(matrix)
        
