from math import sqrt
from PyQt5 import QtWidgets, QtGui, QtCore

"""
A class to represent our player.
Creates a triangle to be our player. Keeps track of players location.
constructTriangleVertices copied from RobotWorld, only color modification added.
"""


class Player(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, square_size, labyrinth):
        super(Player, self).__init__()

        self.square_size = square_size
        self.labyrinth = labyrinth
        brush = QtGui.QBrush(1)
        self.setBrush(brush)
        self.setZValue(5)
        self.constructTriangleVertices()
        self.location = [0, 0]
        self.lab_columns = int(sqrt(self.labyrinth.V))

    def constructTriangleVertices(self):
        """
        Copied from RobotWorld .
        Original comments included.
        This method sets the shape of this item into a triangle.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the robot.
        """
        # Create a new QPolygon object
        triangle = QtGui.QPolygonF()

        # Add the corners of a triangle to the polygon object
        triangle.append(QtCore.QPointF(self.square_size / 2, 0))  # Tip
        triangle.append(QtCore.QPointF(0, self.square_size))  # Bottom-left
        triangle.append(QtCore.QPointF(self.square_size, self.square_size))  # Bottom-right
        triangle.append(QtCore.QPointF(self.square_size / 2, 0))  # Tip

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)
        self.setBrush(QtGui.QBrush(QtGui.QColor("salmon")))

    def get_square(self):
        """
        Returns the tile where our player is at.
        """
        x = self.location[0] / self.square_size
        y = self.location[1] / self.square_size
        place = self.lab_columns * y + x
        return int(place)

    def set_location(self):
        """
        Sets the location of player to the middle of the labyrinth
        """
        self.location[0] = (self.lab_columns // 2) * self.square_size
        self.location[1] = (self.lab_columns // 2) * self.square_size
        self.setPos(float(self.location[0]), float(self.location[1]))

    def update_location(self, next):
        """
        Updates the location of player to the given tile.
        """
        y = next // self.lab_columns
        x = next % self.lab_columns
        self.location = [self.square_size * x, self.square_size * y]
