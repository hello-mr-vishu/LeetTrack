# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        # print(stack)
        while stack:
            curr_data = stack.pop()
            res.append(curr_data.val)
            if curr_data.right:
                stack.append(curr_data.right)
            if curr_data.left:
                stack.append(curr_data.left)
        return res