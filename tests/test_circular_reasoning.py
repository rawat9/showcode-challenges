from src.circular_reasoning.solution import Network
import unittest


class NetworkTests(unittest.TestCase):
    def test1(self):
        result = Network()
        self.assertEqual(result.nodes_visited(12, 3, [10]), 7)

    def test2(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 4, [2, 4]), 4)


if __name__ == "__main__":
    unittest.main()
