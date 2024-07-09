class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        if n == 1 or n == 2:
            return True

        num = 2
        while num <= n:
            num *= 2
            if num == n:
                return True

        return False
