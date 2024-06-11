class Solution(object):

    def makeGood(self, s):
        """
      :type s: str
      :rtype: str
      """
        # edge case, len of s is 1 or 0
        if len(s) <= 1:
            return s

        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
