from src.strike.solution import PlayerFrames
import unittest


class PlayerFramesTests(unittest.TestCase):
    def test1(self):
        result = PlayerFrames()
        self.assertEqual(
            result.get_score(
                [
                    "9",
                    "/",
                    "7",
                    "1",
                    "X",
                    "5",
                    "1",
                    "0",
                    "7",
                    "9",
                    "0",
                    "3",
                    "6",
                    "X",
                    "3",
                    "1",
                    "9",
                    "0",
                ]
            ),
            99,
        )


if __name__ == "__main__":
    unittest.main()
