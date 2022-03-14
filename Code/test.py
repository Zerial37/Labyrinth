import unittest
import sys

from Graphics import Graphics
from PyQt5.QtWidgets import QApplication
from Labyrinth import Labyrinth
from Player import Player


class Test(unittest.TestCase):

    def setUp(self):
        self.test_labyrinth = Labyrinth(9)
        self.test_labyrinth.add_edge(0, 1)
        self.test_labyrinth.add_edge(0, 3)
        self.test_labyrinth.add_edge(1, 2)
        self.test_labyrinth.add_edge(1, 4)
        self.test_labyrinth.add_edge(2, 5)
        self.test_labyrinth.add_edge(3, 4)
        self.test_labyrinth.add_edge(3, 6)
        self.test_labyrinth.add_edge(4, 5)
        self.test_labyrinth.add_edge(4, 7)
        self.test_labyrinth.add_edge(5, 8)
        self.test_labyrinth.add_edge(6, 7)
        self.test_labyrinth.add_edge(7, 8)

        global app
        app = QApplication(sys.argv)
        self.player = Player(30, self.test_labyrinth)
        self.graphics = Graphics(self.test_labyrinth, self.player)

        sys.exit(app.exec_())


    def test_player_get_square(self):
        square = self.player.get_square()

        self.assertEqual(0, square, "player should be at square 0")




if __name__ == "__main__":
    unittest.main()
