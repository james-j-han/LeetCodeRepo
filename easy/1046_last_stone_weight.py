class Solution(object):

    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # heapify max stones
        # while len of heap is greater than 1
        # pop twice and abs value of difference
        # if not zero, add to heap
        # return last item
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # -6 -2 -1
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            n = abs(a - b)
            if n != 0:
                heapq.heappush(stones, -n)

        return -heapq.heappop(stones) if stones else 0
