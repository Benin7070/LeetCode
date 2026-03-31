# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        l=set()
        res=1
        while slow and slow.next:
            if slow in l:
                return slow
            else:
                l.add(slow)
            slow=slow.next
        return None