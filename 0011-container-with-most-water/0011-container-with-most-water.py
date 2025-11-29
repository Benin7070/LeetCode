class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left,right=0,len(height)-1
        while left<right:
            h= min(height[left],height[right])
            area=(right-left)*h
            if area>max_area:
                max_area=area
            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return max_area
