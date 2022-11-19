import unittest
from src.alarics_treasure.solution import Solution


class TreasureHunterTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.parse_roman_numerals("MCMLXI"), 1961)

    def test2(self):
        result = Solution()
        self.assertEqual(result.parse_roman_numerals("MMXV"), 2015)


if __name__ == "__main__":
    unittest.main()
