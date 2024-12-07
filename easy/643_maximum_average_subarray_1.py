class Solution(object):

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = ans = float(sum(nums[:k]))
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]  # sliding window
            if curr > ans:
                ans = curr

        return ans / k


# 12/7/2024
class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # ans var
        # curr var
        # left = 0

        # for num in nums[:k-1]
        # curr += num
        # ans = curr / k

        # for right in range(len(nums)):
        # add right to curr
        # sub left from curr
        # ans = max(ans, curr / k)

        # return ans
        left = curr = 0
        for num in nums[:k]:
            curr += num

        ans = curr / k

        for num in nums[k:]:
            curr += num - nums[left]
            left += 1
            ans = max(ans, curr / k)

        return ans
