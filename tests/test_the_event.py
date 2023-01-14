from src.the_event.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.calculate_difference([1, 0, 3, 4, 5]), 43965)


if __name__ == "__main__":
    unittest.main()
