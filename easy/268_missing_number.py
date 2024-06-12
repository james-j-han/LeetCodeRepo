class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # convert nums to set (which is automatically sorted)
        i = 0
        num_set = set(nums)
        for num in num_set:
            if i != num:
                return i
            i += 1

        return len(num_set)
