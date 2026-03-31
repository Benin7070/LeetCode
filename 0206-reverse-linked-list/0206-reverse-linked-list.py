# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.res=self.head=self.temp=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recu(node):
            if node==None:
                return 
            else:
                if not self.res:
                    self.res=node
                    node=self.head=self.res.next
                    self.res.next=None
                else:
                    self.temp=self.head
                    self.head=self.head.next
                    self.temp.next=None
                    self.temp.next=self.res
                    self.res=self.temp
                    node=self.head
                    
                recu(node.next)
        recu(head)
        if self.head:
            self.head.next=self.res
        return self.head
        