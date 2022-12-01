import unittest
from src.simp1337.solution import Solution


class Simp1337Tests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.simp([192, 900]), 92)

    def test2(self):
        result = Solution()
        self.assertEqual(result.simp([186, 200, 141, 200, 900]), 86)

    def test3(self):
        result = Solution()
        self.assertEqual(result.simp([122, 300, 900]), 22)

    def test4(self):
        result = Solution()
        self.assertEqual(result.simp([122, 300, 200, 900]), 22)

    def test5(self):
        result = Solution()
        self.assertEqual(result.simp([122, 422, 900]), 44)

    def test6(self):
        result = Solution()
        self.assertEqual(result.simp([188, 540, 900]), 48)

    def test7(self):
        result = Solution()
        self.assertEqual(result.simp([110, 520, 900]), -10)

    def test8(self):
        result = Solution()
        self.assertEqual(result.simp([130, 699, 900]), -30)

    def test9(self):
        result = Solution()
        self.assertEqual(result.simp([130, 703, 120, 900]), 30)

    def test10(self):
        result = Solution()
        self.assertEqual(result.simp([100, 803, 120, 900]), 20)

    def test11(self):
        result = Solution()
        self.assertEqual(result.simp([101, 803, 120, 900]), 1)


if __name__ == "__main__":
    unittest.main()
