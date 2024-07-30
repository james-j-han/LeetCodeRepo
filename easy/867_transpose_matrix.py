class Solution(object):

    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        cols = len(matrix[0])
        rows = len(matrix)
        result = []
        if not matrix:
            return result

        for i in range(cols):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])

            result.append(new_row)

        return result
