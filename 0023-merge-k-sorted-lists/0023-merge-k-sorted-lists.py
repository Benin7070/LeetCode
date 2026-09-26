# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        res = lists[0]

        for i in range(1, len(lists)):
            curr = lists[i]

            while curr:
                nxt = curr.next 
                res_p = res  
                res_p_prev = None

                while res_p and res_p.val < curr.val:
                    res_p_prev = res_p
                    res_p = res_p.next

                if res_p_prev is None:  
                    curr.next = res
                    res = curr
                else:                  
                    curr.next = res_p
                    res_p_prev.next = curr

                curr = nxt

        return res