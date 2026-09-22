# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        groupPrev = dummy
        
        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break  
                
            groupNext = kth.next
            
            
            prev = kth.next  
            curr = groupPrev.next
            
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            
            tmp = groupPrev.next  
            groupPrev.next = kth  
            groupPrev = tmp       
            
        return dummy.next

    def getKthNode(self, curr: ListNode | None, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr