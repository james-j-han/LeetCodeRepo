# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_paths = []
        self.explore(root, all_paths, '')
        return all_paths

    def explore(self, t, all_paths, current_path):
        if not t:
            return

        current_path += str(t.val)

        if not t.left and not t.right:
            all_paths.append(current_path)
        else:
            current_path += '->'
            self.explore(t.left, all_paths, current_path)
            self.explore(t.right, all_paths, current_path)
