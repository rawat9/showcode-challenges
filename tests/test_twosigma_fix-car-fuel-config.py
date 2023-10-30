from src.twosigma_fix_car_fuel_config.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.fix_fuel_config("1:2;2:4;3.5:7;4:8"), "1:2;2:4;3.5:7;4:8")

    def test2(self):
        result = Solution()
        self.assertEqual(result.fix_fuel_config("1:1;2:5;3:3;4:6"), "KEEP_PREVIOUS")

    def test3(self):
        result = Solution()
        self.assertEqual(result.fix_fuel_config("1:1;1:2;3:3;4:4"), "KEEP_PREVIOUS")

    def test4(self):
        result = Solution()
        self.assertEqual(
            result.fix_fuel_config("1:1;2:2;3.5:3.5;4:5"), "1:1;2:2;3.5:3.5;4:4"
        )


if __name__ == "__main__":
    unittest.main()
