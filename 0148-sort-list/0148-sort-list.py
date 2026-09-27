# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or head.next==None:
            return head

        def find_mid(node):
            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid=find_mid(head)
        right=mid.next
        left=head
        mid.next=None

        left=self.sortList(left)
        right=self.sortList(right)

        def merge(l1,l2):
            res=tmp=ListNode(0)

            while l1 and l2:
                if l1.val<l2.val:
                    tmp.next=l1
                    l1=l1.next
                else:
                    tmp.next=l2
                    l2=l2.next

                tmp=tmp.next

            tmp.next=l1 if l1 else l2
            return res.next

        return merge(left,right)
    