# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_l1=list1
        head_l2=list2
        res=head_res=None
        def addnode(val):
            nonlocal res,head_res
            if not res:
                res=ListNode(val)
                head_res=res
            else:
                head_res.next=ListNode(val)
                head_res=head_res.next

        while head_l2 and head_l1:
            if head_l1.val==head_l2.val:
                addnode(head_l1.val)
                addnode(head_l2.val)
                head_l1=head_l1.next
                head_l2=head_l2.next
            elif head_l1.val<head_l2.val:
                addnode(head_l1.val)
                head_l1=head_l1.next
            else:
                addnode(head_l2.val)
                head_l2=head_l2.next
        if head_l1:
            while head_l1:
                addnode(head_l1.val)
                head_l1=head_l1.next
        if head_l2:
            while head_l2:
                addnode(head_l2.val)
                head_l2=head_l2.next
        return res