class Solution(object):

    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1

        a = {}
        b = {}
        judge = -1

        for i in trust:
            key_a = i[0]
            key_b = i[1]
            if key_a in a:
                a[key_a] += 1
            else:
                a[key_a] = 1

            if key_b in b:
                b[key_b] += 1
            else:
                b[key_b] = 1

        for key, value in b.items():
            if value == n - 1 and not key in a:
                judge = key

        return judge
