class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x=y=float("inf")
        
        for i in range(x1,x2+1):
            x=min(abs(xCenter-i),x)

        for i in range(y1,y2+1):
            y=min(abs(yCenter-i),y)


        if (x**2)+(y**2)<=(radius**2):
            return True
        else:
            return False