class Solution(object):

    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        # return type int

        #         sort seats array and students array in place
        #         create a stack of sorted seats array backwards
        #         for each student:
        #             num of moves = 0
        #             if student not in seats array:
        #                 num of moves = stack.pop() - student

        #             total num of moves += num of moves

        #         return total num of moves

        total_moves = 0

        seats.sort()
        students.sort()

        seat_stack = []
        for seat in reversed(seats):
            seat_stack.append(seat)

        for s in students:
            num_moves = 0
            last = seat_stack.pop()
            if last != s:
                num_moves = abs(last - s)

            total_moves += num_moves

        return total_moves
