from src.nationwide_network.solution import NationwideAnalysis
import unittest


class NationwideAnalysisTests(unittest.TestCase):
    def test1(self):
        result = NationwideAnalysis()
        self.assertEqual(
            result.find_largest_payers(
                ["A paid £6 to B", "B received £1 from C", "A paid £2 to C"]
            ),
            ["A", "C"],
        )

    def test2(self):
        result = NationwideAnalysis()
        self.assertEqual(result.find_largest_payers(["A paid £0 to C"]), [])


if __name__ == "__main__":
    unittest.main()
