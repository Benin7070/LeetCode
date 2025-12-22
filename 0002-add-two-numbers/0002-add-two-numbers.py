# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = l1
        lst2 = l2
        i = 0
        res1 = 0
        res2 = 0
        
        while lst1:
            res1 += (lst1.val * (10**i))
            i += 1
            lst1 = lst1.next
        
        i = 0
        
        while lst2:
            res2 += (lst2.val * (10**i))
            i += 1
            lst2 = lst2.next
        
        res = res1 + res2
        
       
        if res == 0:
            return ListNode(0)
        
        
        head = None
        tail = None
        
        while res != 0:
            rem = res % 10
            new_node = ListNode(rem)
            
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            
            res //= 10
        
        return head