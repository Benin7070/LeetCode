# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 1:
            return head
        
        def reverse(head):
            curr=head
            prev=None
            while curr!=None:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
                
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        curr = head

        while curr:
            end = curr                      

            for i in range(k - 1):       
                if end.next==None:
                    return dummy.next
                end = end.next

            next_node = end.next
            end.next = None

            r = reverse(curr)

            prev_group.next = r            
            curr.next = next_node


            prev_group = curr
            curr = next_node

        return dummy.next