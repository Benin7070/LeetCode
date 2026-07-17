class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        dp=[]
        while left<=right:
            mid=(left+right)//2
            if ord(target)<ord(letters[mid]):
                right=mid-1
                dp.append(letters[mid])
            elif ord(target)>ord(letters[mid]):
                left=mid+1
                dp.append(letters[mid])
            else:
                left=mid+1
        while dp:
            if ord(dp[-1])>ord(target):
                return dp[-1]
            else:
                dp.pop()
        return letters[0]