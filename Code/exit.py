from PyQt5 import QtWidgets, QtGui, QtCore
import random
from math import sqrt


class Exit(QtWidgets.QGraphicsRectItem):

    def __init__(self, square_size, labyrinth):
        super(Exit, self).__init__()
        self.square_size = square_size
        self.labyrinth = labyrinth
        self.lab_columns = int(sqrt(len(self.labyrinth.tree)))
        brush = QtGui.QBrush(1)
        brush.setColor(QtGui.QColor(0, 128, 0))
        self.setBrush(brush)
        self.randomize_location()

    def randomize_location(self):
        numb = random.randint(1, 4)
        if numb == 1:
            y = self.lab_columns - 1
            x = random.randint(0, y)
            self.setRect(0, x * self.square_size, self.square_size, self.square_size)
        elif numb == 2:
            y = self.lab_columns - 1
            x = random.randint(0, y)
            self.setRect(y * self.square_size, x * self.square_size, self.square_size, self.square_size)
        elif numb == 3:
            y = self.lab_columns - 1
            x = random.randint(0, y)
            self.setRect(x * self.square_size, 0 * self.square_size, self.square_size, self.square_size)
        else:
            y = self.lab_columns - 1
            x = random.randint(0, y)
            self.setRect(x * self.square_size, y * self.square_size, self.square_size, self.square_size)
