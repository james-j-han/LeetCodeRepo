# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diff = 0
        if not root:
            return self.max_diff

        def dfs(node, curr_max, curr_min):
            if not node:
                return

            self.max_diff = max(self.max_diff, abs(curr_max - node.val),
                                abs(curr_min - node.val))
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            dfs(node.left, curr_max, curr_min)
            dfs(node.right, curr_max, curr_min)

        dfs(root, root.val, root.val)
        return self.max_diff
