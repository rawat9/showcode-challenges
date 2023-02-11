from src.remove_tags.solution import Solution
import unittest


class SolutionTests(unittest.TestCase):
    def test1(self):
        result = Solution()
        self.assertEqual(
            result.remove_tags("The <em>quick</em> fox and the <b>lazy</b> dog"),
            "The quick fox and the lazy dog",
        )


if __name__ == "__main__":
    unittest.main()
