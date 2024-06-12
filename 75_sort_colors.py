class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #         get len of nums array

        #         iterate through nums array
        #         left = i
        #         right = i + 1
        #         while right < len nums
        #         if right < left
        #         swap left and right
        #         increment r

        #         return nums

        nums_length = len(nums)

        for i in range(nums_length):
            left = i
            right = i + 1
            while right < nums_length:
                if nums[right] < nums[left]:
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp

                right += 1

        return nums
