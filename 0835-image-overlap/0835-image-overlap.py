class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1[0])
        ans=0
        max_ans=0
        f=1
        for i in range(n):
            for j in range(n):
                if img2[i][j]==1:
                    max_ans+=1

        for dx in range(0-n+1,n):
            for dy in range(0-n+1,n):
                overlap=0

                for i in range(n):
                    for j in range(n):
                        if img2[i][j]==1:
                            x=i-dx
                            y=j-dy
                            if 0 <= x < n and 0 <= y < n:
                                if img1[x][y]==1:
                                    overlap+=1
                ans=max(ans,overlap)
                if ans==max_ans:
                    return ans

        return ans