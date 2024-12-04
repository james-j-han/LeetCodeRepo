# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        # set to infinity
        self.min_depth = float('inf')

        # start with root and current depth of 0
        self.dfs(root, 0)

        return self.min_depth

    def dfs(self, node, depth):
        if not node:
            return

        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, depth + 1)

        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
