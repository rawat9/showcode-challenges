import unittest
from src.lloyds_saving_money.solution import Solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(8), 4)

    def test2(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(36), 10)


if __name__ == "__main__":
    unittest.main()
