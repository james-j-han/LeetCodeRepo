class Solution(object):

    def majorityElement(self, nums):
        """
      :type nums: List[int]
      :rtype: int
      """
        i = len(nums) / 2
        my_dict = defaultdict(int)
        for n in nums:
            my_dict[n] = my_dict[n] + 1

        for key, value in my_dict.items():
            if value > i:
                return key
