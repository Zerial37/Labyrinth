from PyQt5 import QtWidgets, QtGui, QtCore
import random
from math import sqrt


class Stairs(QtWidgets.QGraphicsRectItem):

    def __init__(self, square_size, labyrinth, x, y):
        super(Stairs, self).__init__()
        self.square_size = square_size
        self.labyrinth = labyrinth
        self.lab_columns = int(sqrt(self.labyrinth.V))
        self.location = [x, y]

        brush = QtGui.QBrush(1)
        brush.setColor(QtGui.QColor(255, 0, 0))
        self.setBrush(brush)
        self.setRect(self.location[0], self.location[1], self.square_size, self.square_size)
