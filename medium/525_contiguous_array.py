class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = ones = 0
        max_length = 0
        # key = diff of ones - zeros : value = index
        diff_index = defaultdict(int)

        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1

            diff = ones - zeros

            # check if diff not in dict
            if diff not in diff_index:
                diff_index[diff] = i

            if diff == 0:
                max_length = ones + zeros
            else:
                max_length = max(max_length, i - diff_index[diff])

        return max_length