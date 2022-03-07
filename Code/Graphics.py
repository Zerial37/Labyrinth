from math import sqrt

from PyQt5 import QtWidgets
from PyQt5.Qt import Qt


""""
Kopioitu suoraan robots.py
Tavoitteena saada graafinen alusta johon voi sijoittaa labyrintin ruutuja
Mukana myös paikka napeille, kuten robots.py:ssa
"""

class Graphics(QtWidgets.QMainWindow):

    def __init__(self, labyrinth):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.labyrinth = labyrinth

        self.init_window()
        self.add_squares()


    def add_squares(self):
        sum_x = 0
        sum_y = 0
        for x in range(int(sqrt(len(self.labyrinth.adjMatrix)))):
            for y in range(int(sqrt(len(self.labyrinth.adjMatrix)))):
                item = QtWidgets.QGraphicsRectItem(float(sum_x * 30), float(sum_y * 30),
                                                   float(30), float(30))
                self.scene.addItem(item)
                sum_y += 1
            sum_y = 0
            sum_x += 1

    def init_window(self):
        """
        Sets up the window.
        """
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Labyrinth')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
