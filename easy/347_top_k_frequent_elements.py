class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        result = []
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for i in range(k):
            max_key = max(my_dict, key=my_dict.get)
            result.append(max_key)
            del my_dict[max_key]

        return result