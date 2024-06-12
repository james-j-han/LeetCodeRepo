# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # create prev, curr, and next pointer nodes
        # set curr = head
        # set next = head.next
        # set prev = none
        # while curr
        # set curr.next to prev
        # set prev to curr
        # set curr to next
        # set next to next.next
        # return curr

        if not head:
            return head

        curr = head
        ptr = head.next
        prev = None

        if not ptr:
            return head

        while curr:
            curr.next = prev
            prev = curr
            if ptr:
                curr = ptr
                ptr = ptr.next
            else:
                break

        return curr
