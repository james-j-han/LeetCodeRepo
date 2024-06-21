# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        #  R BL
        # [1 2 3] n = 3
        while l <= r:
            m = (l + r) // 2  # 1

            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1

        return l
