class Solution:
    def number_of_days_to_save(self, moneySaved):
        def algo(start, end):
            total = 0
            for i in range(start, end + 1):
                if total >= moneySaved:
                    return i

                total += i

            return algo(start + 1, end + 1)

        return algo(1, 7)

        # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
        # 2 + 3 + 4 + 5 + 6 + 7 + 8 = 28 - 1 + 8 = 35
        # 3 + 4 + 5 + 6 + 7 + 8 + 9 = 35 - 2 + 9 = 42
        # 4 + 5 + 6 + 7 + 8 + 9 + 10 = 42 - 3 + 10 = 49

        return total


sol = Solution()
print(sol.number_of_days_to_save(8))  # 4
