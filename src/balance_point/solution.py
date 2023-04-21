class Solution:
    def balance_point(self, input):
        i = 0
        left_sum = 0
        right_sum = 0

        while i < len(input):
            left_sum = sum(input[:i])
            right_sum = sum(input[i + 1 :])

            if left_sum == right_sum:
                return i

            i += 1

        return -1
