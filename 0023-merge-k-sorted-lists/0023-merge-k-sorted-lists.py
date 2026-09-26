# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        start=None
        n=len(lists)
        for i in range(n):
            if lists[i]:
                res=lists[i]
                start=i
                break
        if start==None:
            return None

        for i in range(start+1, n):
            if not lists[i]:
                continue
            curr = lists[i]
            res_p=res
            res_p_prev=None
            while curr and res_p:
                if curr.val<=res_p.val:
                    nxt=curr.next
                    if res_p_prev==None:
                        curr.next=res_p
                        res=curr
                        res_p_prev=curr
                    else:
                        curr.next=res_p
                        res_p_prev.next=curr
                        res_p_prev=curr
                    curr=nxt

                else:
                    res_p_prev=res_p
                    res_p=res_p.next

            if curr:
                res_p_prev.next=curr

        return res
