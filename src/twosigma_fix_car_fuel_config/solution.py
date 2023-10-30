class Solution:
    def __init__(self):
        self.config = []

    def fix_fuel_config(self, config):
        self.config = self.init_config(config)

        print(self.is_collinear())

    def init_config(self, config):
        a = config.split(";")
        return list(map(lambda x: tuple(map(float, x.split(":"))), a))

    def calc_slope(self, x1, x2, y1, y2):
        return (y2 - y1) / (x2 - x1)

    def is_collinear(self):
        slopes = []
        for i in range(len(self.config) - 1):
            # [ (1, 2) (2, 4) ]
            x, y = self.config[i], self.config[i + 1]

            x1, y1 = x
            x2, y2 = y

            if x2 == x1 or y2 == y1:
                continue

            slope = abs(self.calc_slope(x1, x2, y1, y2))
            slopes.append(slope)

        return all(s for s in slopes)
