import unittest

from Labyrinth import Labyrinth
from Player import Player
from exit import Exit

"""
Used to test few functions of the code. 
Not that useful in our case, since most of the problems are easily seen in graphics window.
"""


class Test(unittest.TestCase):

    def setUp(self):
        self.g = Labyrinth(100, "None")
        self.g.create_graph()
        self.g.KruskalMST()

        self.p = Player(30, self.g)

    def test_player_location(self):
        """
        Test to see if the player is in the correct starting position
        """
        self.p.set_location()
        square = self.p.get_square()

        self.assertEqual(55, square, "player should be at square 55")

    def test_exit_location(self):
        """
        Test to see if the exit is in the correct position.
        """
        self.ex = Exit(30, self.g)
        square = self.ex.get_square()
        value = False
        p_locations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89,
                       90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        if square in p_locations:
            value = True

        self.assertTrue(value, "exit should be somewhere around the edges")


if __name__ == "__main__":
    unittest.main()
