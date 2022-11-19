class Solution:
    def check_average_spending(self, monthly_spending):
        curr_avg = sum(monthly_spending[:3]) / 3
        min_spending = curr_avg
        least_index = 0

        for i in range(1, len(monthly_spending) - 2):
            three_consecutive = monthly_spending[i : i + 3]
            total = sum(three_consecutive) / 3

            if total < curr_avg:
                curr_avg = total
                least_index = i

        return least_index if min_spending != curr_avg else -1
