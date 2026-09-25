# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head==None or k==0:
            return head
        n=1
        temp=head
        while temp.next!=None:
            n+=1
            temp=temp.next

        if k==n or n==1 or (k%n)==0:
            return head
        i=n-(k%n)
        print(i,n) 
        curr=head
        for j in range(i-1):
            curr=curr.next

        nxt=curr.next

        curr.next=None
        temp.next=head
        head=nxt

        return head

        
