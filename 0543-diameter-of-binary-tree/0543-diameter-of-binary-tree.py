# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return 1+max(height(node.left),height(node.right))

        def dia(node):
            if not node:
                return 0
            lheight = height(node.left)
            rheight = height(node.right)
            ldia = dia(node.left)
            rdia = dia(node.right)
            return max(ldia,rdia,lheight+rheight)
        if not root:
            return 0
        return dia(root)