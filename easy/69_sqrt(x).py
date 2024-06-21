class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l = 0
        r = x
        #     r l
        # 0 1 2 3 4 5 6 7 8
        while l <= r:
            m = (l + r) // 2  # 3

            if m * m <= x:
                l = m + 1
            else:
                r = m - 1

        return r
