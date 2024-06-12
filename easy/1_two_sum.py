class Solution(object):

    def twoSum(self, nums, target):
        """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
        # store number as key and index as value
        # iterate through nums, if target - num (store in variable) is in my_dict, return indices else
        # my_dict[num] = current_index
        my_dict = {}
        # 0, 2
        # 1, 7
        for i, num in enumerate(nums):
            # comp = 7
            # comp = 2
            comp = target - num
            if comp in my_dict:
                # [0, 1]
                return [my_dict[comp], i]
            else:
                # my_dict[2] = 0
                my_dict[num] = i
