class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_dec_stack=[]
        next_greater={}
        res=[]
        for i in reversed(nums2):
            while mono_dec_stack and mono_dec_stack[-1]<i:
                mono_dec_stack.pop()
            if not mono_dec_stack:
                next_greater[i]=-1
            elif mono_dec_stack and mono_dec_stack[-1]>i:
                next_greater[i]=mono_dec_stack[-1]
            mono_dec_stack.append(i)
            print(mono_dec_stack)
        for i in nums1:
            res.append(next_greater[i])
        return res