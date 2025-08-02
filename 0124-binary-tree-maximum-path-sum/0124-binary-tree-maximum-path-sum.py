# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxpath(node,maxi):
            if not node:
                return 0
            lh = max(0,maxpath(node.left,maxi))
            rh = max(0,maxpath(node.right,maxi))
            maxi[0] =max(maxi[0],lh+rh+node.val)
            return node.val + max(lh,rh) 
        maxi = [float('-inf')]
        maxpath(root,maxi)
        return maxi[0]