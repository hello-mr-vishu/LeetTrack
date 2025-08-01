# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        queue = []
        queue.append(root)
        current_level = 0
        while queue:
            len_q = len(queue)
            res.append([])
            for _ in range(len_q):
                node = queue.pop(0)
                res[current_level].append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            current_level+=1
        return res