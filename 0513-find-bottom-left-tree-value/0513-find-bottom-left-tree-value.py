from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        q = deque([root])
        res = root.val
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()

                if i == 0:
                    res = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res