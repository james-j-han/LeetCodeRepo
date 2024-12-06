# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans

        queue = collections.deque([root])

        while queue:
            largest = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()
                largest = max(largest, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(largest)

        return ans
