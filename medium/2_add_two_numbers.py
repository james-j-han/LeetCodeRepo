# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # iterate through each list and multiply by index + 1
        # [2 4 3] = (2 * 1) + (4 * 10) + (3 * 100) = 342
        # [5 6 4] = (5 * 1) + (6 * 10) + (4 * 100) = 465
        # add the two numbers together 465 + 342 = 807
        # iterate through answer and add to linked list in reverse

        total = 0

        index = 1
        while l1:
            total += l1.val * index
            index *= 10
            l1 = l1.next

        index = 1
        while l2:
            total += l2.val * index
            index *= 10
            l2 = l2.next

        total_as_list = [int(x) for x in str(total)]  # 807

        head = prev = ListNode(total_as_list[-1])  # 7

        if len(total_as_list) > 1:
            for n in total_as_list[len(total_as_list) - 2::-1]:
                new_node = ListNode(n)
                prev.next = new_node
                prev = new_node

        return head
