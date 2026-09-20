import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        
        if not head or not head.next:
            return None

        slow=head
        fast=head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        slow.next=slow.next.next

        return head