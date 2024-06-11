# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        temp = head
        ptr = head.next

        while ptr:
            if ptr.val == temp.val:
                ptr = ptr.next
                # temp.next.next = None
                temp.next = ptr
            else:
                temp = ptr
                ptr = ptr.next

        return head
