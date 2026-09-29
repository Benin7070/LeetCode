"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        res=res_tmp=None
        n=1
        while temp:
            node=Node(temp.val,None,None)
            if res==None:
                res=node
            else:
                res_tmp.next=node

            res_tmp=node
            n+=1
            temp=temp.next

        def find(val):
            temp=res
            i=1
            while temp:
                if i==val:
                    return temp
                i+=1
                temp=temp.next
            return None

        temp=head
        temp2=res
        while temp:
            s=temp.random
            sam=head
            i=0
            while sam:
                if sam==s:
                    break
                i+=1
                sam=sam.next
            sam2=res
            j=0
            if s!=None:
                while sam2:
                    if i==j:                    
                        temp2.random=sam2
                        break
                    j+=1
                    sam2=sam2.next


            temp=temp.next
            temp2=temp2.next
        
        return res