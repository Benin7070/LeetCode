class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numbers=[i+1 for i in range(len(grid)*len(grid[0]))]
        res=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in numbers:
                    numbers.remove(grid[i][j])
                else:
                    res.append(grid[i][j])
        return res+numbers