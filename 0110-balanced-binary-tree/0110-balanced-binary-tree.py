# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(node):
            if not node:
                return 0
            return 1+max(height(node.left),height(node.right))
        def checkbal(root):
            if not root:
                return True
            lheight = height(root.left)
            rheight = height(root.right)
            if abs(lheight-rheight)>1:
                return False
            return checkbal(root.left) and checkbal(root.right)
        return checkbal(root)