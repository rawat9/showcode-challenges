class Solution:
    def parse_roman_numerals(self, input):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        i = 0
        num = 0
        while i < len(input):
            if i + 1 < len(input) and input[i : i + 2] in roman:
                print(input[i : i + 2])
                num += roman[input[i : i + 2]]
                i += 2
            else:
                num += roman[input[i]]
                i += 1
        return num
