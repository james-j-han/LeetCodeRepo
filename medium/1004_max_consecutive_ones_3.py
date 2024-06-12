class Solution(object):

    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        count_zero = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1

            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
