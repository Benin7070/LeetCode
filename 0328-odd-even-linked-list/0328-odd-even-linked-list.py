# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head==None:
            return None

        temp=head
        i=0
        even=odd=odd_tmp=even_tmp=None
        while temp!=None:
            i+=1

            if i%2==0:
                if even==None:
                    even=ListNode(temp.val)
                    even_tmp=even
                else:
                    even_tmp.next=ListNode(temp.val)
                    even_tmp=even_tmp.next

            else:
                if odd==None:
                    odd=ListNode(temp.val)
                    odd_tmp=odd
                else:
                    odd_tmp.next=ListNode(temp.val)
                    odd_tmp=odd_tmp.next
            temp=temp.next
                            
        odd_tmp.next=even
        return odd
