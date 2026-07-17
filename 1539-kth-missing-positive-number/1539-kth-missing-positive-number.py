class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        pos=0
        while True:
            i+=1
            if pos<len(arr) and arr[pos]==i:
                pos+=1
            else:
                k-=1
            if not k:
                return i
            

