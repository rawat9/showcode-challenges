from src.next_ready_set_recycle.solution import NextSustainability
import unittest


class NextSustainabilityTests(unittest.TestCase):
    def test1(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled("Paper", ["Paper - 60% recycled"]), 60
        )

    def test2(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "Shirt",
                [
                    "Shirt: 90% cotton 10% polyester",
                    "Cotton - 10% recycled",
                    "Polyester - 50% recycled",
                ],
            ),
            14,
        )

    def test3(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "Shirt",
                [
                    "Shirt: 90% cotton 10% polyester",
                    "Cotton - 10.99% recycled",
                    "Polyester - 50.89% recycled",
                ],
            ),
            15,
        )

    def test4(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "Shirt",
                [
                    "Shirt: 80% cotton 10% polyester 10% abhishek",
                    "Cotton - 10.99% recycled",
                    "Polyester - 50.89% recycled",
                    "ABHISHEk - 20.929% recycled",
                ],
            ),
            16,
        )

    def test5(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "Shirt",
                [
                    "Shirt: 51% cotton 49% polyester",
                    "CottON - 10.99% recycled",
                    "pOlyesTeR - 20.99000% recycled",
                ],
            ),
            16,
        )

    def test6(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "Shirt",
                [
                    "Shirt: 80% cotton 10% polyester 10% abhishek",
                    "Cotton - 10% recycled",
                    "Polyester - 50% recycled",
                ],
            ),
            13,
        )

    def test7(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "9Shirt",
                [
                    "9Shirt: 80% cotton 10% polyester 10% abhishek",
                    "Cotton - 10% recycled",
                ],
            ),
            8,
        )

    def test8(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "9Shirt",
                [
                    "9Shirt: 100% cottON",
                    "Cotton - 10% recycled",
                ],
            ),
            10,
        )

    def test9(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "9Shirt",
                [
                    "9Shirt: 79.91% cotton 20.09% polyester",
                    "Cotton - 10% recycled",
                ],
            ),
            8,
        )

    def test10(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "9Shirt",
                [
                    "9Shirt: 79.91% cotton 20.09% polyester",
                    "Cotton - 10% recycled",
                ],
            ),
            8,
        )

    def test11(self):
        result = NextSustainability()
        self.assertEqual(
            result.percentage_recycled(
                "9Shirt",
                [
                    "9Shirt: 80% cotton 20% polyester",
                    "Cotton - 5.4% recycled",
                    "polyester - 5.4% recycled",
                ],
            ),
            5,
        )


if __name__ == "__main__":
    unittest.main()
