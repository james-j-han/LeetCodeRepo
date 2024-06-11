# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # head can be null

        # while fast is not None
        # move slow by 1
        # move fast by 1
        # if fast is not None
        # move fast by 1 again
        # if fast is not None
        # if slow == fast return True
        # if fast is None return False

        slow = fast = head

        while fast:
            slow = slow.next
            fast = fast.next

            if not fast:
                return False
            else:
                fast = fast.next

            if not fast:
                return False
            else:
                if slow == fast:
                    return True

        return False
