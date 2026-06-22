class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numbers=[i+1 for i in range(len(grid)*len(grid[0]))]
        num=sum(numbers)
        res=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==numbers[grid[i][j]-1]:
                    num-=numbers[grid[i][j]-1]
                    numbers[grid[i][j]-1]=None
                elif numbers[grid[i][j]-1]==None:
                    print(numbers[grid[i][j]-1],numbers)
                    res.append(grid[i][j])
        res.append(num)
        return res