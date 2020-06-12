#!/bin/python3.8

"""
    Tests of class Tetromino from module tetromino
"""

import unittest

import config
import tetromino
import gameboard

class TetrominoTest(unittest.TestCase):

    def test__init__(self):
        testing_x = 3
        testing_y = 4
        testing_times_rotated = 1
        testing_type = "T"

        tetromino_proper_shape = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
        ]

        testing_tetromino = tetromino.Tetromino(type=testing_type, times_rotated=testing_times_rotated, x=testing_x, y=testing_y)
        self.assertEqual(testing_tetromino.current_x, testing_x)
        self.assertEqual(testing_tetromino.current_y, testing_y)
        self.assertEqual(testing_tetromino.buffer, tetromino_proper_shape)


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
        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer, clockwise=False)
        # should be same like previous - Z_after_rotate
        self.assertEqual(testing_tetromino.buffer, Z_after_rotate)

        testing_tetromino.buffer = testing_tetromino.rotate(testing_tetromino.buffer)
        Z_after_rotate_once_again = [
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(testing_tetromino.buffer, Z_after_rotate_once_again)


    def test_fall_down(self):
        gameboard_tested = gameboard.Gameboard()
        testing_tetromino = tetromino.Tetromino("I", times_rotated=0, x=3, y=18)
        self.assertEqual(testing_tetromino.fall_down(gameboard_tested), True)

        # simulating falling of three blocks down
        testing_tetromino.current_y -= 3
        self.assertEqual(testing_tetromino.fall_down(gameboard_tested), False)
        testing_tetromino.current_y += 3
        self.assertEqual(testing_tetromino.fall_down(gameboard_tested), True)


    def test_will_collide(self):
        gameboard_tested = gameboard.Gameboard()
        # filling some of blocks [row][column]
        gameboard_tested.fields[4][6] = config.FALLEN_BLOCK
        gameboard_tested.fields[4][7] = config.FALLEN_BLOCK
        gameboard_tested.fields[4][8] = config.FALLEN_BLOCK
        testing_tetromino = tetromino.Tetromino("I", times_rotated=0, x=5, y=0)
        self.assertEqual(testing_tetromino.will_collide(gameboard_tested), False)
        # should intersects while fall one block down
        testing_tetromino.current_y += 2
        self.assertEqual(testing_tetromino.will_collide(gameboard_tested), True)




        pass

    def test_calculate_buffor_drawing_coordinates(self):
        pass


if __name__ == "__main__":
    unittest.main()