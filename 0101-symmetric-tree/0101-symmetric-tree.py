# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True

        def ismirror(ltree,rtree):
            if not ltree and not rtree:
                return True
            if not ltree or not rtree :
                return False
            return (ltree.val == rtree.val and ismirror(ltree.left,rtree.right) and ismirror(ltree.right,rtree.left))
        
        return ismirror(root.left,root.right)