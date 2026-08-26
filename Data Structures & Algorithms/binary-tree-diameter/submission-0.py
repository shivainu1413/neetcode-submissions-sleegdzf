# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def maxdepth(node):
            if not node:
                return 0
            L = maxdepth(node.left)
            R = maxdepth(node.right)
            self.res = max(self.res, L+R)
            return 1 + max(L, R)
        maxdepth(root)
        return self.res