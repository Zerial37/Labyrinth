from math import sqrt
from PyQt5 import QtWidgets, QtGui, QtCore



class Player(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, square_size, labyrinth):
        # Call init of the parent object
        super(Player, self).__init__()

        # Do other stuff
        self.square_size = square_size
        self.labyrinth = labyrinth
        brush = QtGui.QBrush(1)  # 1 for even fill
        self.setBrush(brush)
        self.setZValue(2)
        self.constructTriangleVertices()
        self.location = [0, 0]
        self.lab_columns = int(sqrt(self.labyrinth.V))

    def constructTriangleVertices(self):
        """
        This method sets the shape of this item into a triangle.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the robot.
        """
        # Create a new QPolygon object
        triangle = QtGui.QPolygonF()

        # Add the corners of a triangle to the the polygon object
        triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip
        triangle.append(QtCore.QPointF(0, self.square_size)) # Bottom-left
        triangle.append(QtCore.QPointF(self.square_size, self.square_size)) # Bottom-right
        triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)

    def get_square(self):
        x = self.location[0] / self.square_size
        y = self.location[1] / self.square_size
        place = self.lab_columns * y + x
        return int(place)

    def set_location(self):
        self.location[0] = (self.lab_columns // 2) * self.square_size
        self.location[1] = (self.lab_columns // 2) * self.square_size
        self.setPos(float(self.location[0]), float(self.location[1]))

