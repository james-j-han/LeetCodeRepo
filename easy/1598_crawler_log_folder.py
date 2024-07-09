class Solution(object):

    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for log in reversed(logs):
            stack.append(log)

        count = 0

        while stack:
            command = stack.pop()
            if command == './':
                continue
            elif command == '../':
                if count > 0:
                    count -= 1
            else:
                count += 1

        return count
