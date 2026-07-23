# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0))
        levels = {}
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if not level in levels:
                levels[level] = []
            levels[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        result = []
        for i in range(len(levels)):
            result.append(levels[i])
        return result