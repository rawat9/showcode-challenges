from src.balance_point.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.balance_point([2, 7, 4, 5, -3, 8, 9, -1]), 3)

    def test2(self):
        result = Solution()
        self.assertEqual(result.balance_point([]), -1)


if __name__ == "__main__":
    unittest.main()
