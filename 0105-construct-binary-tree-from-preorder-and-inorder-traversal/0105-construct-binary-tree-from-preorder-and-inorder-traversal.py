# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode()
        root_val = preorder[0]
        root.val = root_val
        # print(root)
        idx = inorder.index(root.val)
        # print(idx)
        root.left = self.buildTree(preorder[1:1+idx],inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:],inorder[idx+1:])
        return root