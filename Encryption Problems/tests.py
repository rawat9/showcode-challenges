import unittest
from solution import Solution


class TestSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_handle_file_1(self):
        self.assertEqual(
            self.solution.handle_file("(o)(l)(s)(s)(v).(a)(e)(a)"), "hello.txt"
        )

    def test_handle_file_2(self):
        self.assertEqual(self.solution.handle_file("<l><m><b><c>.<h><q>"), "node.js")

    def test_handle_file_3(self):
        self.assertEqual(
            self.solution.handle_file("(o)(l)(s)(s)(v).(a)(e)(ae)"), "hello.txtx"
        )

    def test_handle_file_4(self):
        self.assertEqual(
            self.solution.handle_file("(olssv)(o)(l)(s)(s)(v).(a)(e)(ae)"),
            "hellohello.txtx",
            "should work for multiple characters within the parenthesis ()",
        )

    def test_handle_file_5(self):
        self.assertEqual(
            self.solution.handle_file("<s>(l)(s)(s)(v).(a)(e)(a)"),
            "uello.txt",
            "should work for multiple characters within the angle brackets <>",
        )

    def test_handle_file_6(self):
        self.assertEqual(
            self.solution.handle_file("<s>0(l)3(s)9(s)0(v).(a)(e)(a)()[]"),
            "u0e3l9l0o.txt[]",
        )

    def test_handle_file_7(self):
        self.assertEqual(
            self.solution.handle_file("<>"), "", "Should pass if passed an empty <>"
        )

    def test_handle_file_8(self):
        self.assertEqual(
            self.solution.handle_file("()"), "", "Should pass if passed an empty ()"
        )

    def test_handle_file_9(self):
        self.assertEqual(
            self.solution.handle_file("{a}"),
            "a",
            "Should pass if passed an empty ()",
        )


if __name__ == "__main__":
    unittest.main()
