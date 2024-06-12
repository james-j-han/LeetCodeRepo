class Solution(object):

    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create prefix sum
        # find min value
        # if negative, abs + 1
        # if positive, min
        # [-3, 2,-3, 4, 2]
        # [-3,-1,-4, 0, 2]

        # [ 2, 3, 5,-5,-1]
        # [ 2, 5,10, 5, 4]

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])

        ans = min(prefix)

        if ans < 0:
            ans = abs(ans) + 1
        elif ans > 1:
            ans = 1

        return ans
