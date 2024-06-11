# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # lists can be empty

        #         if list1 is empty return head of list2
        #         if list2 is empty return head of list1
        #         if list1 and list2 are empty return empty list

        #         new_list = ListNode(None)

        #         while list1 and list2 are not empty
        #             if h1 > h2
        #                 if h2 != none
        #                     add h2 to end of list
        #                     move h2 pointer by 1
        #             else
        #                 if h1 != none
        #                     add h1 to end of list
        #                     move h1 pointer by 1

        #         return

        merged_list = None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val > list2.val:
            merged_list = list2
            list2 = list2.next
        else:
            merged_list = list1
            list1 = list1.next

        current = merged_list
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next

            current = current.next

        current.next = list1 if list1 else list2

        return merged_list
