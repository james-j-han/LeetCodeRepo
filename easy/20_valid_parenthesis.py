class Solution(object):

    def isValid(self, s):
        """
      :type s: str
      :rtype: bool
      """
        # create a stack
        # iterate through string and push open brackets onto stack
        # while iterating through string and encounter closed bracket, see if it matches with open bracket
        # in stack[-1] else return false

        # edge case: string is empty or string starts with closed bracket

        my_stack = []
        if not s:
            return False

        for char in s:
            if char == ')':
                if my_stack and my_stack[-1] == '(':
                    my_stack.pop()
                else:
                    return False
            elif char == ']':
                if my_stack and my_stack[-1] == '[':
                    my_stack.pop()
                else:
                    return False
            elif char == '}':
                if my_stack and my_stack[-1] == '{':
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(char)

        return not my_stack
