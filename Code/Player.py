from PyQt5 import QtWidgets, QtGui, QtCore


class Player(QtWidgets.QGraphicsPolygonItem):
    def __init__(self, square_size):
        # Call init of the parent object
        super(Player, self).__init__()

        # Do other stuff
        self.square_size = square_size
        brush = QtGui.QBrush(1)  # 1 for even fill
        self.setBrush(brush)
        self.constructTriangleVertices()
        self.location = [0, 0]

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
