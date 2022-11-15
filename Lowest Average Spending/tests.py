from solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(
            result.check_average_spending(
                [300, 700, 9000, 2000, 10000, 5000, 4000, 800, 23000, 1100, 1200, 8000]
            ),
            5,
        )

    def test2(self):
        result = Solution()
        self.assertEqual(
            result.check_average_spending(
                [5000, 4000, 800, 8000, 10000, 5000, 4000, 800, 23000, 800, 4000, 5000]
            ),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
