# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            if not node:
                return 0
            q = deque([node])
            depth = 0
            while q:
                levelsize = len(q)
                for _ in range(levelsize):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                depth += 1
            return depth

        return bfs(root)