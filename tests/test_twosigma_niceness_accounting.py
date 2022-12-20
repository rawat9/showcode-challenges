from src.twosigma_niceness_accounting.solution import NiceMigration
import unittest


class NiceMigrationTests(unittest.TestCase):
    def test1(self):
        result = NiceMigration()
        self.assertEqual(
            result.convert(
                "20150602 #4516 + 20.02\n20150603 #4516 * 2\n20150605 #4516 / 2\n20150604 #4516 - 2"
            ),
            "20150602 @4516 20.02\n20150603 @4516 40.04\n20150604 @4516 38.04\n20150605 @4516 19.02",
        )

    def test2(self):
        result = NiceMigration()
        self.assertEqual(
            result.convert("20150602 #12358 = 20.02\n20150603 #12358 + 40.02"),
            "20150602 @12358 20.02\n20150603 @12358 60.04",
        )

    def test3(self):
        result = NiceMigration()
        self.assertEqual(
            result.convert(
                "20150810 #121 = 5.01\n20150811 #121 - 5.2\n20150812 #121 = 10.21"
            ),
            "20150810 @121 5.01\n20150811 @121 ?\n20150812 @121 10.21",
        )

    def test4(self):
        result = NiceMigration()
        self.assertEqual(
            result.convert(
                "20150810 #121 = 5.01\n20150811 #121 - 5.2\n20150812 #121 = 10.21\n20150812 #129 + 1"
            ),
            "20150810 @121 5.01\n20150811 @121 ?\n20150812 @121 10.21\n20150812 @129 11.21",
        )

    def test5(self):
        result = NiceMigration()
        self.assertEqual(
            result.convert(
                "20150810 #121 = 5.01\n20150811 #121 - 5.2\n20150812 #121 = 10.21\n20150801 #120 + 2"
            ),
            "20150801 @120 2.00\n20150810 @121 5.01\n20150811 @121 ?\n20150812 @121 10.21",
        )


if __name__ == "__main__":
    unittest.main()
