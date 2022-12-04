from src.analyst_agony.solution import Solution
import unittest


class TradersTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(
            result.aggregate_ohlcv(
                [
                    "15,12.5000,50",
                    "25,10.2000,100",
                    "45,14.8000,20",
                    "55,13.1000,30",
                ]
            ),
            ["0,12.5000,14.8000,10.2000,13.1000,200"],
        )


if __name__ == "__main__":
    unittest.main()
