#!/bin/python3.8

"""
    Tests of module tetromino

"""

import unittest

import config
import tetromino

class TetrominoTest(unittest.TestCase):

    # __init__

    def test_rotate(self):
        """Testing method rotate from Tetromino."""
        self.testing_tetromino = tetromino.Tetromino("I")
        self.testing_tetromino.buffer = self.testing_tetromino.rotate(self.testing_tetromino.buffer)
        Z_after_rotate =  [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ]
        self.assertEqual(self.testing_tetromino.buffer, Z_after_rotate)


        pass

    def test_fall_down(self):
        pass

    def test_move(self):
        pass

    def test_will_collide(self):
        pass

    def test_calculate_buffor_drawing_coordinates(self):
        pass

    def test_draw(self):
        pass

if __name__ == "__main__":
    unittest.main()