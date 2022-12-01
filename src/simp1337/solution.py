class Solution:
    def __init__(self):
        self.registers = {"PC": 0, "ACC": 0, "BAK": 0}

    def get_instruction_type(self, number: int) -> int:
        if number < 10:
            return number
        return self.get_instruction_type(number // 10)

    def get_immediate_value(self, number):
        return number % 100

    def simp(self, input: list[int]) -> int:
        for num in input:
            instruction_type = self.get_instruction_type(num)
            immediate_value = self.get_immediate_value(num)

            match instruction_type:
                case 1:
                    self.registers["ACC"] = immediate_value
                case 2:
                    self.registers["ACC"], self.registers["BAK"] = self.registers["BAK"], self.registers["ACC"]
                case 3:
                    self.registers["BAK"] = self.registers["ACC"]
                case 4:
                    self.registers["ACC"] += immediate_value
                case 5:
                    self.registers["ACC"] -= immediate_value
                case 6:
                    self.registers["ACC"] *= -1
                case 7:
                    return self.simp([input[self.registers["PC"] + immediate_value - 1]])
                case 8:
                    if self.registers["ACC"] <= 0:
                        continue
                    return self.simp([input[self.registers["PC"] + immediate_value - 1]])

            self.registers["PC"] += 1

        return self.registers["ACC"]
