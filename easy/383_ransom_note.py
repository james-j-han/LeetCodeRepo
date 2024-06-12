class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = defaultdict(int)
        for c in magazine:
            mag_dict[c] += 1

        for c in ransomNote:
            if c in mag_dict:
                mag_dict[c] -= 1
                if mag_dict[c] <= 0:
                    del mag_dict[c]
            else:
                return False

        return True
