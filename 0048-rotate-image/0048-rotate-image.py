class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(i,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                print(matrix[i][j],matrix[j][i])
        for i in range(n):
            matrix[i].reverse()