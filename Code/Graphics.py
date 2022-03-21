from math import sqrt

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import Qt
from exit import Exit



""""
Kopioitu suoraan robots.py
Tavoitteena saada graafinen alusta johon voi sijoittaa labyrintin ruutuja
Mukana myös paikka napeille, kuten robots.py:ssa
"""

class Graphics(QtWidgets.QMainWindow):

    def __init__(self, labyrinth, player, square_size):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.labyrinth = labyrinth
        self.player = player
        self.square_size = square_size
        self.columns = int(sqrt(len(self.labyrinth.tree)))

        self.init_window()
        self.add_player()
        self.add_exit()
        self.add_squares()


    def add_player(self):
        self.scene.addItem(self.player)
        self.player.set_location()

    def add_exit(self):
        ex = Exit(self.square_size, self.labyrinth)
        self.scene.addItem(ex)

    def add_squares(self):
        sum_x = 0
        sum_y = 0
        for x in range(int(sqrt(len(self.labyrinth.tree)))):
            for y in range(int(sqrt(len(self.labyrinth.tree)))):
                item = QtWidgets.QGraphicsRectItem(float(sum_x * self.square_size), float(sum_y * self.square_size),
                                                   float(self.square_size), float(self.square_size))
                self.scene.addItem(item)
                place = self.columns * sum_x + sum_y
                if self.labyrinth.has_edge(place, place + 1):
                    line = QtWidgets.QGraphicsLineItem(float((sum_y + 1) * self.square_size),
                                                       float(sum_x * self.square_size + 1),
                                                       float((sum_y + 1) * self.square_size),
                                                       float((sum_x + 1) * self.square_size - 1))
                    line.setPen(QtGui.QColor(255, 255, 255))
                    line.setZValue(1)
                    self.scene.addItem(line)
                if self.labyrinth.has_edge(place, place + self.columns):
                    line = QtWidgets.QGraphicsLineItem(float(sum_y * self.square_size + 1),
                                                       float((sum_x + 1) * self.square_size),
                                                       float((sum_y + 1) * self.square_size - 1),
                                                       float((sum_x + 1) * self.square_size))
                    line.setPen(QtGui.QColor(255, 255, 255))
                    line.setZValue(1)
                    self.scene.addItem(line)
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
        self.scene.setSceneRect(0, 0, self.columns * self.square_size, self.columns * self.square_size)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_W:
            if self.player.location[1] != 0:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() - int(self.columns)):
                    self.player.location[1] -= self.square_size
                    self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        if event.key() == Qt.Key_S:
            if self.player.location[1] != int(sqrt(len(self.labyrinth.tree) - 1)) * self.square_size:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + int(self.columns)):
                    self.player.location[1] += self.square_size
                    self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        if event.key() == Qt.Key_A:
            if self.player.location[0] != 0:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() - 1):
                    self.player.location[0] -= self.square_size
                    self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        if event.key() == Qt.Key_D:
            if self.player.location[0] != int(sqrt(len(self.labyrinth.tree) - 1)) * self.square_size:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + 1):
                    self.player.location[0] += self.square_size
                    self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))

