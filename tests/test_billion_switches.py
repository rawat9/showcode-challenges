from src.billion_switches.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(result.billion_switches([0]), 0)

    def test2(self):
        result = Solution()
        self.assertEqual(result.billion_switches([100]), 100)

    def test3(self):
        result = Solution()
        self.assertEqual(result.billion_switches([100, 100]), 0)

    def test4(self):
        result = Solution()
        self.assertEqual(result.billion_switches([100, 50, 25]), 75)

    def test5(self):
        result = Solution()
        self.assertEqual(
            result.billion_switches(
                [
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                    1000000000,
                ]
            ),
            0,
        )

    def test6(self):
        result = Solution()
        self.assertEqual(
            result.billion_switches([100, 50]),
            50,
        )

    def test7(self):
        result = Solution()
        self.assertEqual(
            result.billion_switches([1000000000]),
            1000000000,
        )

    def test8(self):
        result = Solution()
        self.assertEqual(
            result.billion_switches([200, 100, 50]),
            150,
        )

    def test9(self):
        result = Solution()
        self.assertEqual(
            result.billion_switches([5000, 4000, 3000, 2000, 1000]),
            3000,
        )


if __name__ == "__main__":
    unittest.main()
