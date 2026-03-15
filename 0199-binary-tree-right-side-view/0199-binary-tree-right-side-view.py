# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self):
        self.res=[]
        self.height=0
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return self.res
        q=deque([root])
        while q:
            level_size=len(q)
            for i in range(level_size):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i==level_size-1:
                    self.res.append(node.val)
        return self.res
        
