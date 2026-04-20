class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # build histogram
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # apply histogram logic
            stack = []
            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0
                
                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                
                stack.append(i)
        
        return max_area