class Solution(object):

    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # store frequency of each char in hashmap
        my_dict = defaultdict(int)
        result = 0

        for c in text:
            my_dict[c] += 1

        while True:
            if 'b' not in my_dict:
                break
            else:
                if my_dict['b'] - 1 < 0:
                    del my_dict['b']
                    break
                my_dict['b'] -= 1

            if 'a' not in my_dict:
                break
            else:
                if my_dict['a'] - 1 < 0:
                    del my_dict['a']
                    break
                my_dict['a'] -= 1

            if 'l' not in my_dict:
                break
            else:
                if my_dict['l'] - 2 < 0:
                    del my_dict['l']
                    break
                my_dict['l'] -= 2

            if 'o' not in my_dict:
                break
            else:
                if my_dict['o'] - 2 < 0:
                    del my_dict['o']
                    break
                my_dict['o'] -= 2

            if 'n' not in my_dict:
                break
            else:
                if my_dict['n'] - 1 < 0:
                    del my_dict['n']
                    break
                my_dict['n'] -= 1

            result += 1

        return result
