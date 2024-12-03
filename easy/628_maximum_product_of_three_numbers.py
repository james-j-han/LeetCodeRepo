class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = sorted(nums)

        product1 = numbers[-1] * numbers[-2] * numbers[-3]
        product2 = numbers[0] * numbers[1] * numbers[-1]

        return max(product1, product2)
