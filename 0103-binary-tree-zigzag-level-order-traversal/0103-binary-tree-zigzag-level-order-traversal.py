# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def height(node):
            if not node:
                return 0
            lsubtree = height(node.left)
            rsubtree = height(node.right)
            return max(lsubtree,rsubtree)+1
        def ltor(node,level,temp):
            if not node:
                return 
            if level == 1:
                temp.append(node.val)
            else:
                ltor(node.left,level-1,temp)
                ltor(node.right,level-1,temp)

        def rtol(node,level,temp):
            if not node:
                return 
            if level ==1:
                temp.append(node.val)
            else:
                rtol(node.right,level-1,temp)
                rtol(node.left,level-1,temp)


        lefttoright = True
        treeheight = height(root)
        res = []
        for i in range(1,treeheight+1):
            temp =[]
            if lefttoright:
                ltor(root,i,temp)
            else:
                rtol(root,i,temp)
            res.append(temp)
            lefttoright = not lefttoright
        return res