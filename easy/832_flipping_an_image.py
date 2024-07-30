class Solution(object):

    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        if not image:
            return result

        rows = len(image)
        cols = len(image[0])

        for i in range(rows):
            new_row = []
            for j in range(cols):
                if image[i][j] == 0:
                    new_row.append(1)
                else:
                    new_row.append(0)

            result.append(reversed(new_row))

        return result
