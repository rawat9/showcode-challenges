from src.cipher_error.solution import Solution
import unittest


class CipherTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(
            result.split_string_on_change("TDpmfe&dcqs!@"),
            "T ,D ,p ,m ,f ,e ,& ,d ,c ,q ,s ,! ,@ ",
        )

    def test2(self):
        result = Solution()
        self.assertEqual(
            result.split_string_on_change("BEpk93diawcTW£!£"),
            "B ,E ,p ,k ,9 ,3 ,d ,i ,a ,w ,c ,T ,W ,£ ,! ,£ ",
        )


if __name__ == "__main__":
    unittest.main()
