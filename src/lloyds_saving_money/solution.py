class Solution:
    def __init__(self):
        self.counter = 0

    def algo(self, start, end):
        self.counter += 1
        if start < end:
            return start + self.algo(start + 1, end)
        else:
            return end

    def number_of_days_to_save(self, moneySaved):

        # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
        # 2 + 3 + 4 + 5 + 6 + 7 + 8 = 28 - 1 + 8 = 35
        # 3 + 4 + 5 + 6 + 7 + 8 + 9 = 35 - 2 + 9 = 42
        # 4 + 5 + 6 + 7 + 8 + 9 + 10 = 42 - 3 + 10 = 49

        return self.algo(2, 8)


sol = Solution()
print(sol.number_of_days_to_save(8), 4)
print(sol.counter)
