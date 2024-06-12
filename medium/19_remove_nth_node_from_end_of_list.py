# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # three-pointer

        #         start with left and right ptr at head and prev ptr = None
        #         set right ptr = right ptr + n
        #         n = 2 left = 0 right = 2
        #         traverse linked list while right ptr
        #         right = right.next
        #         prev = left
        #         left = left.next

        #         prev.next = left.next
        #         return head

        prev = None
        left = right = head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            prev = left
            left = left.next

        if prev:
            prev.next = left.next
        else:
            return left.next

        return head
