from src.bataille.solution import Bataille
import unittest


class BatailleTests(unittest.TestCase):
    def test1(self):
        result = Bataille()
        self.assertEqual(result.play("2A", "2K"), 0)

    def test2(self):
        result = Bataille()
        self.assertEqual(result.play("A2QK", "457JT"), 1)

    def test3(self):
        result = Bataille()
        self.assertEqual(result.play("", ""), 0)

    def test4(self):
        result = Bataille()
        self.assertEqual(result.play("", "A"), 2)

    def test5(self):
        result = Bataille()
        self.assertEqual(result.play("J", ""), 1)

    def test6(self):
        result = Bataille()
        self.assertEqual(result.play("B", ""), 0)


if __name__ == "__main__":
    unittest.main()
