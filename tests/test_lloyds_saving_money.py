import unittest
from src.lloyds_saving_money.solution import Solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(8), 4)

    def test2(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(36), 10)

    def test3(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(0), 0)

    def test4(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(55), 13)

    def test5(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(56), 14)

    def test6(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(74778), 999)

    def test7(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(74779), 1000)

    def test8(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(33900), 665)

    def test9(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(74927), -1)

    def test10(self):
        result = Solution()
        self.assertEqual(result.number_of_days_to_save(-1), -1)


if __name__ == "__main__":
    unittest.main()
