# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        # head is at least length 1

        sprev = fprev = None
        slow = fast = head
        fnext = fast.next

        i = 1

        while i < right:
            fprev = fast
            fast = fnext
            fnext = fnext.next

            if i < left:
                sprev = slow
                slow = slow.next
            else:
                fast.next = fprev

            i += 1

        if sprev:
            sprev.next = fast
        else:
            head = fast

        slow.next = fnext

        return head
