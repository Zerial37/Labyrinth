from math import sqrt
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication

from exit import Exit
from solver import Solver



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
        self.columns = int(sqrt(self.labyrinth.V))
        self.ex = Exit(self.square_size, self.labyrinth)
        self.solver = Solver(self.labyrinth.V, self.labyrinth.tree, self.player, self)

        self.init_window()
        self.add_player()
        self.add_exit()
        self.add_squares()
        self.add_weave()
        self.init_buttons()


    def add_player(self):
        self.scene.addItem(self.player)
        self.player.set_location()

    def add_exit(self):
        self.scene.addItem(self.ex)

    def add_weave(self):
        # Here we set up graphics to represent tunnels we iterate through all possible tunnels, but not all of them end
        # up being actual tunnels
        for z in range(len(self.labyrinth.loc_and_type)):
            l, t = self.labyrinth.loc_and_type[z]
            x = l % self.columns
            y = l // self.columns

            # Tunnels from left to right
            if t == 1:

                # Right side
                line = QtWidgets.QGraphicsLineItem(float((x + 1) * self.square_size + 1),
                                                   float(y * self.square_size + 1),
                                                   float((x + 1) * self.square_size + 1),
                                                   float((y + 1) * self.square_size) - 1)
                line.setPen(QtGui.QColor(39, 39, 39))
                line.setZValue(2)
                self.scene.addItem(line)
                line2 = QtWidgets.QGraphicsLineItem(float((x + 1) * self.square_size + 2),
                                                    float(y * self.square_size + 2),
                                                    float((x + 1) * self.square_size + 2),
                                                    float((y + 1) * self.square_size) - 2)
                line2.setPen(QtGui.QColor(86, 86, 86))
                line2.setZValue(2)
                self.scene.addItem(line2)
                line3 = QtWidgets.QGraphicsLineItem(float((x + 1) * self.square_size + 3),
                                                    float(y * self.square_size + 3),
                                                    float((x + 1) * self.square_size + 3),
                                                    float((y + 1) * self.square_size) - 3)
                line3.setPen(QtGui.QColor(134, 134, 134))
                line3.setZValue(2)
                self.scene.addItem(line3)
                line4 = QtWidgets.QGraphicsLineItem(float((x + 1) * self.square_size + 4),
                                                    float(y * self.square_size + 4),
                                                    float((x + 1) * self.square_size + 4),
                                                    float((y + 1) * self.square_size) - 4)
                line4.setPen(QtGui.QColor(182, 182, 182))
                line4.setZValue(2)
                self.scene.addItem(line4)

                # Left side
                line = QtWidgets.QGraphicsLineItem(float(x * self.square_size - 1),
                                                   float(y * self.square_size + 1),
                                                   float(x * self.square_size - 1),
                                                   float((y + 1) * self.square_size) - 1)
                line.setPen(QtGui.QColor(39, 39, 39))
                line.setZValue(2)
                self.scene.addItem(line)
                line2 = QtWidgets.QGraphicsLineItem(float(x * self.square_size - 2),
                                                    float(y * self.square_size + 2),
                                                    float(x * self.square_size - 2),
                                                    float((y + 1) * self.square_size) - 2)
                line2.setPen(QtGui.QColor(86, 86, 86))
                line2.setZValue(2)
                self.scene.addItem(line2)
                line3 = QtWidgets.QGraphicsLineItem(float(x * self.square_size - 3),
                                                    float(y * self.square_size + 3),
                                                    float(x * self.square_size - 3),
                                                    float((y + 1) * self.square_size) - 3)
                line3.setPen(QtGui.QColor(134, 134, 134))
                line3.setZValue(2)
                self.scene.addItem(line3)
                line4 = QtWidgets.QGraphicsLineItem(float(x * self.square_size - 4),
                                                    float(y * self.square_size + 4),
                                                    float(x * self.square_size - 4),
                                                    float((y + 1) * self.square_size) - 4)
                line4.setPen(QtGui.QColor(182, 182, 182))
                line4.setZValue(2)
                self.scene.addItem(line4)

            # Tunnels from up to bottom
            if t == 2:
                # Bottom
                line = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 1),
                                                   float((y + 1) * self.square_size + 1),
                                                   float((x + 1) * self.square_size - 1),
                                                   float((y + 1) * self.square_size) + 1)
                line.setPen(QtGui.QColor(39, 39, 39))
                line.setZValue(2)
                self.scene.addItem(line)
                line2 = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 2),
                                                    float((y + 1) * self.square_size + 2),
                                                    float((x + 1) * self.square_size - 2),
                                                    float((y + 1) * self.square_size) + 2)
                line2.setPen(QtGui.QColor(86, 86, 86))
                line2.setZValue(2)
                self.scene.addItem(line2)
                line3 = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 3),
                                                    float((y + 1) * self.square_size + 3),
                                                    float((x + 1) * self.square_size - 3),
                                                    float((y + 1) * self.square_size) + 3)
                line3.setPen(QtGui.QColor(134, 134, 134))
                line3.setZValue(2)
                self.scene.addItem(line3)
                line4 = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 4),
                                                    float((y + 1) * self.square_size + 4),
                                                    float((x + 1) * self.square_size - 4),
                                                    float((y + 1) * self.square_size) + 4)
                line4.setPen(QtGui.QColor(182, 182, 182))
                line4.setZValue(2)
                self.scene.addItem(line4)
                line = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 1),
                                                   float(y * self.square_size - 1),
                                                   float((x + 1) * self.square_size - 1),
                                                   float(y * self.square_size) - 1)
                # Up
                line.setPen(QtGui.QColor(39, 39, 39))
                line.setZValue(2)
                self.scene.addItem(line)
                line2 = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 2),
                                                    float(y * self.square_size - 2),
                                                    float((x + 1) * self.square_size - 2),
                                                    float(y * self.square_size) - 2)
                line2.setPen(QtGui.QColor(86, 86, 86))
                line2.setZValue(2)
                self.scene.addItem(line2)
                line3 = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 3),
                                                    float(y * self.square_size - 3),
                                                    float((x + 1) * self.square_size - 3),
                                                    float(y * self.square_size) - 3)
                line3.setPen(QtGui.QColor(134, 134, 134))
                line3.setZValue(2)
                self.scene.addItem(line3)
                line4 = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 4),
                                                    float(y * self.square_size - 4),
                                                    float((x + 1) * self.square_size - 4),
                                                    float(y * self.square_size) - 4)
                line4.setPen(QtGui.QColor(182, 182, 182))
                line4.setZValue(2)
                self.scene.addItem(line4)


    def add_squares(self):
        sum_x = 0
        sum_y = 0
        for x in range(self.columns):
            for y in range(self.columns):
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

    def init_buttons(self):
        """
        Adds button which calls the solver class.
        Copied from robots.py code
        """
        self.solver_btn = QtWidgets.QPushButton("Show solution")
        self.solver_btn.clicked.connect(lambda: self.solver.printAllPaths(self.player.get_square(),
                                                                          self.ex.get_square()))
        self.horizontal.addWidget(self.solver_btn)

    def player_update_position(self):
        """
        Updates the position of the player in labyrinth
        """
        self.player.setPos(float(self.player.location[0]), float(self.player.location[1]))
        self.update()
        QApplication.processEvents()

        if self.player.location == self.ex.location:
            sys.exit(-1)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_W:
            if self.player.location[1] != 0:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() - int(self.columns)):
                    self.player.location[1] -= self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(),
                                             self.player.get_square() - int(self.columns) - int(self.columns)):
                    self.player.location[1] -= self.square_size * 2
                    self.player_update_position()
        if event.key() == Qt.Key_S:
            if self.player.location[1] != (self.columns - 1) * self.square_size:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + int(self.columns)):
                    self.player.location[1] += self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(),
                                             self.player.get_square() + int(self.columns) + int(self.columns)):
                    self.player.location[1] += self.square_size * 2
                    self.player_update_position()
        if event.key() == Qt.Key_A:
            if self.player.location[0] != 0:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() - 1):
                    self.player.location[0] -= self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() - 2):
                    self.player.location[0] -= self.square_size * 2
                    self.player_update_position()
        if event.key() == Qt.Key_D:
            if self.player.location[0] != (self.columns - 1) * self.square_size:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + 1):
                    self.player.location[0] += self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + 2):
                    self.player.location[0] += self.square_size * 2
                    self.player_update_position()
