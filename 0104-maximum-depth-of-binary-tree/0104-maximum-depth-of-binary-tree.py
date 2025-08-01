# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def height(node):
            q = deque([root])
            depth = 0
            while q:
                level_size = len(q)
                for _ in range(level_size):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                depth+=1
            return depth
        return height(root)