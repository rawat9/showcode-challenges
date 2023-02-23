from src.secret_value.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.secret_value([1, 2, 5, 8, 11, 12], 5), "2")

    def test2(self):
        result = Solution()
        self.assertEqual(result.secret_value([2, 7, 9, 13, 18, 22, 31], 14), "-1")


if __name__ == "__main__":
    unittest.main()
