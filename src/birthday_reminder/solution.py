from datetime import date, timedelta


class Solution:
    def get_repeating_event(self, starting_date, repeat_instruction):
        year, month, day = map(int, starting_date.split("/"))
        d = date(year, month, day)
        return d + timedelta(weeks=1)


sol = Solution()
print(sol.get_repeating_event("2021/10/14", "every 3 days"))
