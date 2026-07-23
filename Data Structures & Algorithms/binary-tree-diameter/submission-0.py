# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def rec(node):
            if not node:
                return -1
            nonlocal result
            left = rec(node.left) + 1
            right = rec(node.right) + 1
            result = max(result, left + right)
            return max(left, right)
        rec(root)
        return result