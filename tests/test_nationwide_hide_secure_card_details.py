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
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details("598241111111111104454"),
            ["VISA", "5982*************4454"],
        )

    def test12(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details("22254121212121212123333"),
            ["MASTERCARD", "222****************3333"],
        )

    def test13(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details("11111111113434343434343431111111111"),
            ["AMEX", "1111111111***************1111111111"],
        )

    def test14(self):
        solution = Solution()
        self.assertEqual(solution.redact_card_details(""), ["NONE", ""])

    def test15(self):
        solution = Solution()
        self.assertEqual(solution.redact_card_details(" "), ["NONE", " "])

    def test16(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details("4111111111110 and 4111111111112"),
            ["VISA", "VISA", "************* and *************"],
        )

    def test17(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details(
                "343434343434343 and 343434343434344 and 343434343434345"
            ),
            [
                "AMEX",
                "AMEX",
                "AMEX",
                "*************** and *************** and ***************",
            ],
        )

    def test18(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details(
                "5111111111111111 and 5111111111111112 and 5111111111111113"
            ),
            [
                "MASTERCARD",
                "MASTERCARD",
                "MASTERCARD",
                "**************** and **************** and ****************",
            ],
        )

    def test19(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details("5111111111111111 and 343434343434343"),
            ["MASTERCARD", "AMEX", "**************** and ***************"],
        )

    def test20(self):
        solution = Solution()
        self.assertEqual(
            solution.redact_card_details(
                "5111111111111111 and 343434343434343 and 4111111111111"
            ),
            [
                "MASTERCARD",
                "AMEX",
                "VISA",
                "**************** and *************** and *************",
            ],
        )

    def test21(self):
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
