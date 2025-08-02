# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxheight = 0
        if not root:
            return 0
        def dia(node):
        
            if not node :
                return 0
            lh = dia(node.left)
            rh = dia(node.right)
            self.maxheight = max(self.maxheight,lh+rh)
            return 1+max(lh,rh)
        dia(root)
        return self.maxheight