import re


class Solution:
    def is_not_valid(self, input):
        return len(re.findall(r"\d{1}-\d{2}-\d{6}-x", input)) == 0

    def get_check_digit(self, input):
        if not isinstance(input, str):
            return -1

        if self.is_not_valid(input):
            return -1

        numbers = "".join(input.split("-"))
        n = 0
        i = 1
        for num in numbers:
            if num.isnumeric():
                n += int(num) * i
                i += 1

        return n % 11
