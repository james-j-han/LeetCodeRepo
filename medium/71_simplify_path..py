class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # split path
        # for element in split_path:
        # if element:
        # if stack and element == '..':
        # pop stack
        # if not element == '.':
        # push to stack

        split_path = path.split('/')
        print(split_path)
        stack = []

        for e in split_path:
            if e:
                if e == '..':
                    if stack:
                        stack.pop()

                elif not e == '.':
                    stack.append(e)

        joined_stack = '/'.join(stack)
        print(joined_stack)
        return '/' + joined_stack
