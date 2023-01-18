from src.the_archives.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.get_check_digit("0-19-852663-x"), 6)

    def test2(self):
        result = Solution()
        self.assertEqual(result.get_check_digit("0-19-85266-x"), -1)

    def test3(self):
        result = Solution()
        self.assertEqual(result.get_check_digit("0-x"), -1)

    def test4(self):
        result = Solution()
        self.assertEqual(result.get_check_digit("0"), -1)


if __name__ == "__main__":
    unittest.main()
