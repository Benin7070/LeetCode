class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                last_idx = stack.pop()
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1  
                area = heights[last_idx] * width
                max_area = max(area, max_area)
            stack.append(i)
        

        while stack:
            last_idx = stack.pop()
            left_boundary = stack[-1] if stack else -1
            width = len(heights) - left_boundary - 1  
            area = heights[last_idx] * width
            max_area = max(area, max_area)
        
        return max_area