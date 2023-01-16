from src.snowcode.solution import SocialMediaSorter
import unittest


class SocialMediaSorterTests(unittest.TestCase):
    def test1(self):
        result = SocialMediaSorter()
        self.assertEqual(result.get_recipient("@JoeBloggs yo", 1), "JoeBloggs")

    def test2(self):
        result = SocialMediaSorter()
        self.assertEqual(
            result.get_recipient(
                "Hey @Joe_Bloggs what time are we meeting @FredBloggs?", 2
            ),
            "FredBloggs",
        )

    def test3(self):
        result = SocialMediaSorter()
        self.assertEqual(
            result.get_recipient("Hey @- what time are we meeting @FredBloggs?", 1),
            "-a4f",
        )

    def test4(self):
        result = SocialMediaSorter()
        self.assertEqual(
            result.get_recipient(
                "@Santa I've been good this year, can I get a PS5 like @Userxyz?", 1
            ),
            "Santa",
        )

    def test5(self):
        result = SocialMediaSorter()
        self.assertEqual(
            result.get_recipient(
                "@Santa I've been good this year, can I get a PS5 like @Userxyz?", 2
            ),
            "Userxyz",
        )


if __name__ == "__main__":
    unittest.main()
