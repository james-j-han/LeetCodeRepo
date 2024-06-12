class Solution(object):
  def containsDuplicate(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      # convert to set and compare lengths with nums
      # if len of set is less than len of nums, then it contains duplicate

      if not nums:
          return False

      num_set = set(nums)

      return len(num_set) < len(nums)