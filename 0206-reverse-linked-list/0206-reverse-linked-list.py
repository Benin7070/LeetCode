# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.end=0
        self.res=self.head=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recu(node):
            if node==None:
                return 
            if not self.end and node.next!=None:
                recu(node.next)
            else:
                self.end=1
            if self.end:
                if not self.res:
                    self.res=ListNode(node.val)
                    self.head=self.res
                else:
                    n1=ListNode(node.val)
                    self.head.next=n1
                    self.head=n1
        recu(head)
        return self.res
        