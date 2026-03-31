# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.res=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recu(node):
            if node==None:
                return 
            else:
                if not self.res:
                    self.res=ListNode(node.val)
                else:
                    n1=ListNode(node.val)
                    n1.next=self.res
                    self.res=n1
                recu(node.next)
        recu(head)
        return self.res
        