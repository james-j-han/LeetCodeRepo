class Solution(object):

    def longestConsecutive(self, nums):
        """
      :type nums: List[int]
      :rtype: int
      """
        # unsorted array of integers: nums
        # return type: int
        # edge case nums is empty

        #         var longest_streak = 0

        #         if nums is empty return longest_streak

        #         iterate through nums array
        #         while element - 1 is in nums array:
        #             current_num = element - 1 (3)
        #             current_streak += 1 1

        #         longest_streak = max of longest_streak or current_streak

        #         return longest_streak
        longest_streak = 0

        num_set = set(nums)

        if not num_set:
            return longest_streak

        for n in num_set:
            # if previous number not in set, start from this number
            if n - 1 not in num_set:
                current_num = n
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
