# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.h=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        if head==None:
            return head
        while itr:
            if self.h==None:
                node=ListNode(itr.val,None)
            else:
                node=ListNode(itr.val,self.h)
            self.h=node
            itr=itr.next
        return self.h
            
                