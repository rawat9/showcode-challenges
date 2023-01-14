class Solution:
    def calculate_difference(self, input):
        input.sort(reverse=True)

        minimum_number = self.construct_minimum_number(input)
        maximum_number = self.construct_maximum_number(input)

        return maximum_number - minimum_number

    def construct_minimum_number(self, numbers):
        num = numbers[-1]
        for i in range(len(numbers) - 2, -1, -1):
            num = num * 10 + numbers[i]

        num = str(num)
        zeroes = numbers.count(0)
        print(zeroes)
        return int(num[0] + "0" * zeroes + num[1:])

    def construct_maximum_number(self, numbers):
        num = numbers[0]
        for i in range(1, len(numbers)):
            num = num * 10 + numbers[i]

        return num
