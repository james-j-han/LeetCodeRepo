class Solution(object):

    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # convert jewels into a set
        # store stones in dict
        j_set = set(jewels)
        s_dict = defaultdict(int)
        result = 0

        for stone in stones:
            s_dict[stone] += 1

        for stone in s_dict:
            if stone in j_set:
                result += s_dict[stone]

        return result
