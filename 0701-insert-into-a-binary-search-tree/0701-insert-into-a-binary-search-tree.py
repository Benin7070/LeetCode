# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        tmp=prev=root
        if not root and val:
            return TreeNode(val)
        while tmp:
            prev=tmp
            if val>=tmp.val:
                tmp=tmp.right
            elif val<tmp.val:
                tmp=tmp.left

        node=TreeNode(val)
        if val>=prev.val:
            prev.right=node
        else:
            prev.left=node
        return root
        