from collections import deque


class Solution(object):

    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        # arrays are not empty
        # MATCH: two-pointer, queue

        # PSEUDOCODE
        # add arr2 to a queue
        # add arr1 to a dict
        # create an empty list for arr1
        # while queue:
        #     get current num from queue.popleft
        #     while current num in dict:
        #         add current num to new list
        #         dict[current num] -= 1
        #         if dict[current num] == 0
        #             del dict[current num]

        # add remaining elements from arr1 to new list
        # return new list
        my_queue = deque(arr2)
        my_dict = {}

        for n in arr1:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1

        sorted_list = []

        while my_queue:
            curr = my_queue.popleft()
            while curr in my_dict:
                sorted_list.append(curr)
                my_dict[curr] -= 1
                if my_dict[curr] == 0:
                    del my_dict[curr]

        remaining = []

        for key in my_dict:
            i = 0
            while i < my_dict[key]:
                remaining.append(key)
                i += 1

        remaining.sort()

        return sorted_list + remaining
