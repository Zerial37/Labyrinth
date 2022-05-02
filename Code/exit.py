from PyQt5 import QtWidgets, QtGui

import random
from math import sqrt

"""
A class to represent exit, which is a green tile somewhere around the edges of the labyrinth
"""


class Exit(QtWidgets.QGraphicsRectItem):

    def __init__(self, square_size, labyrinth):
        super(Exit, self).__init__()
        self.square_size = square_size
        self.labyrinth = labyrinth
        self.lab_columns = int(sqrt(self.labyrinth.V))
        self.location = [0, 0]

        brush = QtGui.QBrush(1)
        brush.setColor(QtGui.QColor(0, 128, 0))
        self.setBrush(brush)
        self.randomize_location()

    def get_square(self):
        """
        Returns the tile where our exit is at.
        """
        x = self.location[0] / self.square_size
        y = self.location[1] / self.square_size
        place = self.lab_columns * y + x
        return int(place)

    def randomize_location(self):
        """
        Sets the location of exit randomly somewhere around the edges of the labyrinth
        """
        numb = random.randint(1, 4)
        y = self.lab_columns - 1
        x = random.randint(0, y)
        if numb == 1:
            self.location[1] = x * self.square_size
        elif numb == 2:
            self.location = [y * self.square_size, x * self.square_size]
        elif numb == 3:
            self.location = [x * self.square_size, 0 * self.square_size]
        else:
            self.location = [x * self.square_size, y * self.square_size]

        self.setRect(self.location[0], self.location[1], self.square_size, self.square_size)
