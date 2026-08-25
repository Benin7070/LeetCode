class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res=0
        def split(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=split(nums[:mid])
            right=split(nums[mid:])

            return merge(left,right)

        def merge(left,right):
            nonlocal res
            j=0
            for i in range(len(left)):
                while j<len(right) and left[i]>(2*right[j]):
                    j+=1
                res+=j
            sorted_list=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    sorted_list.append(left[i])
                    i+=1
                else:
                    sorted_list.append(right[j])
                    j+=1

            sorted_list.extend(left[i:])
            sorted_list.extend(right[j:])

            return sorted_list
        split(nums)
        return res


            