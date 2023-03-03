from src.base_number.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(15, 16), "F")

    def test2(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(23, 8), "27")


if __name__ == "__main__":
    unittest.main()
