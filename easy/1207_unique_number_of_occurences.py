class Solution(object):

    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # if length of arr is 1 return True

        # iterate through arr and add to dict key = element value = occurences
        # iterate through values of dict and add to set and if already in set return False

        if len(arr) == 1:
            return True

        my_dict = {}

        for n in arr:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1

        my_set = set()

        for value in my_dict.values():
            if value in my_set:
                return False
            else:
                my_set.add(value)

        return True
