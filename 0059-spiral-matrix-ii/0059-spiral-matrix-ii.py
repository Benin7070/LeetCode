from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        
        while top <= bottom and left <= right:
            
            # left → right
            for j in range(left, right + 1):
                nums[top][j] = num
                num += 1
            top += 1
            
            # top → bottom
            for i in range(top, bottom + 1):
                nums[i][right] = num
                num += 1
            right -= 1
            
            # right → left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    nums[bottom][j] = num
                    num += 1
                bottom -= 1
            
            # bottom → top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    nums[i][left] = num
                    num += 1
                left += 1
        
        return nums