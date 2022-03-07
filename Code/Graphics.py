from math import sqrt

from PyQt5 import QtWidgets
from PyQt5.Qt import Qt



""""
Kopioitu suoraan robots.py
Tavoitteena saada graafinen alusta johon voi sijoittaa labyrintin ruutuja
Mukana myös paikka napeille, kuten robots.py:ssa
"""

class Graphics(QtWidgets.QMainWindow):

    def __init__(self, labyrinth, player):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.labyrinth = labyrinth
        self.player = player
        self.square_size = 30

        self.init_window()
        self.add_squares()
        self.add_player()

    def add_player(self):
        self.scene.addItem(self.player)

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

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_W:
            if self.player.location[1] != 0:
                self.player.location[1] -= self.square_size
                self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        if event.key() == Qt.Key_S:
            if self.player.location[1] != 60:
                self.player.location[1] += self.square_size
                self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        if event.key() == Qt.Key_A:
            if self.player.location[0] != 0:
                self.player.location[0] -= self.square_size
                self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        if event.key() == Qt.Key_D:
            if self.player.location[0] != 60:
                self.player.location[0] += self.square_size
                self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))

