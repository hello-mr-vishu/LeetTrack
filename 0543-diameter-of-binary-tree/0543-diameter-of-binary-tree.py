# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     dia = 0
    #     res = self.preOrder(dia,root)
    #     return res
    # def preOrder(self,dia,node):
    #     if node is None:
    #         # print("None")
    #         return
    #     print(node.val,"val")
    #     print(node.left,"left")
    #     self.preOrder(dia+1,node.left)
    #     print(node.right,"right")
    #     self.preOrder(dia+1,node.right)
    #     return dia

        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res,left+right)
            return 1+max(left,right)

        dfs(root)
        return self.res