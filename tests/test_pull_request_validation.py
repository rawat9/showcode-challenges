import unittest
from src.pull_request_validation.solution import Solution


class TestSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_verfifypr_1(self):
        self.assertEqual(
            self.solution.verifypr(
                [
                    "0x10a,3012-chore-updating Dependencies,9019222,341",
                    "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741",
                    "0x10c,2999-feat-added UI Buttons,1234299,52",
                ]
            ),
            True,
        )

    def test_verfifypr_2(self):
        self.assertEqual(
            self.solution.verifypr(
                [
                    "0x5fc,1005-fix-fixed bugs,4191399,29",
                    "0x5fd,-fix-fixed UI,9109344,011",
                ]
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
