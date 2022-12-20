class Solution:
    def __init__(self):
        self.counter = 0

    def number_of_days_to_save(self, moneySaved):
        if moneySaved < 0 or moneySaved > 74926:
            return -1

        total_days = 0

        def algo(start, end):
            nonlocal total_days

            for i in range(start, end + 1):
                if total_days >= moneySaved:
                    return self.counter

                total_days += i
                self.counter += 1

            return algo(start + 1, end + 1)

        self.counter = 0
        return algo(1, 7)
