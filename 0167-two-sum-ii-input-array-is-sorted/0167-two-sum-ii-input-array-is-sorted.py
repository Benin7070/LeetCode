class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        li=[]
        while left<right:
            ans=numbers[left]+numbers[right]
            if ans==target:
                li.append(left+1)
                li.append(right+1)
                return li
            elif ans<target:
                left+=1
            else:
                right-=1