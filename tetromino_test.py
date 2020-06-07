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

        # test for config.TETROMINO_SHAPES["I"] rotated once clockwise and oposite
        testing_tetromino = tetromino.Tetromino("I")
        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer)
        I_after_rotate = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ]
        self.assertEqual(testing_tetromino.buffer, I_after_rotate)
        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer, clockwise=False) # return to previous (initial) value
        self.assertEqual(testing_tetromino.buffer, config.TETROMINO_SHAPES["I"])


        # test for config.TETROMINO_SHAPES["Z"] rotated once clockwise and oposite
        testing_tetromino = tetromino.Tetromino("Z")

        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer)
        Z_after_rotate = [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
        ]
        self.assertEqual(testing_tetromino.buffer, Z_after_rotate)
        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer)
        print(testing_tetromino.buffer)
        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer)
        print(testing_tetromino.buffer)
        # Z_after_rotate_once_again = [
        #     [0, 0, 0, 0],
        #     [1, 1, 0, 0],
        #     [0, 1, 1, 0],
        #     [0, 0, 0, 0],
        # ]
        # self.assertEqual(testing_tetromino.buffer, Z_after_rotate_once_again)



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