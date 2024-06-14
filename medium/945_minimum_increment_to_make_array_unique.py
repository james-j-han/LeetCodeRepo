class Solution(object):

    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total_moves = 0

        if len(nums) == 1:
            return total_moves

        nums.sort()

        for i in range(1, len(nums)):
            moves = 0
            if nums[i] <= nums[i - 1]:
                moves = nums[i - 1] - nums[i] + 1
                nums[i] += moves

            total_moves += moves

        return total_moves
