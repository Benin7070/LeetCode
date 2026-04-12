class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        lstack=[]
        rstack=[]
        lres=[-1]*n
        rres=[n]*n

        for h in range(n):
            while lstack and heights[lstack[-1]]>=heights[h]:
                lstack.pop()
            
            if lstack:
                lres[h]=lstack[-1]
            lstack.append(h)

        for h in range(n-1,-1,-1):
            while rstack and heights[rstack[-1]]>=heights[h]:
                rstack.pop()
            
            if rstack:
                rres[h]=rstack[-1]
            rstack.append(h)
        max_area=-1
        for i in range(n):
            width=rres[i]-lres[i]-1
            area=heights[i]*width
            if area>max_area:
                max_area=area
        
        return max_area


            