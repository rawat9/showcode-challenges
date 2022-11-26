from src.nationwide_hide_secure_card_details.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details(
                "This is a secret but my card number is 4000000000000! Shhhh! Don't tell anyone!"
            ),
            [
                "VISA",
                "This is a secret but my card number is *************! Shhhh! Don't tell anyone!",
            ],
        )

    def test2(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details(
                "123-5200000000000000-123 oops! Don't read that!!"
            ),
            ["MASTERCARD", "123-****************-123 oops! Don't read that!!"],
        )

    def test3(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("5300000000000000123456789"),
            ["MASTERCARD", "****************123456789"],
        )

    def test4(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("987675400000000000000"),
            ["MASTERCARD", "98767****************"],
        )

    def test5(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("370000000000000"), ["AMEX", "***************"]
        )

    def test6(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("15986700000000000000075670987654321"),
            ["NONE", "15986700000000000000075670987654321"],
        )

    def test7(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("No private data here!"),
            ["NONE", "No private data here!"],
        )

    def test8(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details(
                "blah blah blah blah 5100000000000000 blah blah blah"
            ),
            ["MASTERCARD", "blah blah blah blah **************** blah blah blah"],
        )

    def test9(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("secret secrets: 340000000000000"),
            ["AMEX", "secret secrets: ***************"],
        )

    def test10(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("dont read this -> 4111111111111 <- no! stop!"),
            ["VISA", "dont read this -> ************* <- no! stop!"],
        )

    def test11(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details(
                "dont read this -> 4111111111111 <- here's another one 340000000000000"
            ),
            [
                "VISA",
                "dont read this -> ************* <- here's another one 340000000000000",
            ],
        )

    def test12(self):
        result = Solution()
        self.assertEqual(
            result.redact_card_details("dont read this -> 54114111111111111"),
            [
                "MASTERCARD",
                "dont read this -> ****************1",
            ],
        )


if __name__ == "__main__":
    unittest.main()
