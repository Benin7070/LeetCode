# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=num2=""
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        
        res=str(int(num1)+int(num2))
        n=len(res)
        ans=None
        for i in range(n):
            if not ans:
                ans=ListNode(int(res[i]))
                head=ans
            else:
                head.next=ListNode(int(res[i]))
                head=head.next

        return ans