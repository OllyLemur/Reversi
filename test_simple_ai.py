import unittest
from model.simple_ai import SimpleAI

class TestSimpleAi(unittest.TestCase):
    def test_get_move_with_correct_array(self):
        possible_moves = {(1, 3): [(-1, 1), (0, 2)], (1, 4): [((-1, 1), (1, 2))], (3, 4): [((-1, 0), (1, 2))]}
        simple_ai = SimpleAI(2)
        point = simple_ai.get_move(possible_moves)
        self.assertEqual(point, (3, 4))

    def test_get_move_with_empty_array(self):
        simple_ai = SimpleAI(2)
        possible_moves = []
        self.assertRaises(ValueError, simple_ai.get_move, possible_moves)