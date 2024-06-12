class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = ans = float(sum(nums[:k]))
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k] # sliding window
            if curr > ans:
                ans = curr

        return ans / k