from math import sqrt
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication

from Labyrinth import Labyrinth
from exit import Exit
from solver import Solver
from Player import Player



""""
Kopioitu suoraan robots.py
Tavoitteena saada graafinen alusta johon voi sijoittaa labyrintin ruutuja
Mukana myös paikka napeille, kuten robots.py:ssa
"""

class Graphics(QtWidgets.QMainWindow):

    def __init__(self, square_size):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.input_windows()
        self.player = Player(square_size, self.labyrinth)
        self.square_size = square_size
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
            x = l % self.size
            y = l // self.size

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
        for x in range(self.size):
            for y in range(self.size):
                item = QtWidgets.QGraphicsRectItem(float(sum_x * self.square_size), float(sum_y * self.square_size),
                                                   float(self.square_size), float(self.square_size))
                self.scene.addItem(item)
                sum_y += 1
            sum_y = 0
            sum_x += 1
        for i in self.labyrinth.tree:
            if i[1] - i[0] == 1:
                y = i[0] // self.size
                x = i[0] % self.size
                line = QtWidgets.QGraphicsLineItem(float((x + 1) * self.square_size),
                                                   float(y * self.square_size + 1),
                                                   float((x + 1) * self.square_size),
                                                   float((y + 1) * self.square_size - 1))
                line.setPen(QtGui.QColor(255, 255, 255))
                line.setZValue(1)
                self.scene.addItem(line)
            elif i[1] - i[0] == self.size:
                y = i[0] // self.size
                x = i[0] % self.size
                line = QtWidgets.QGraphicsLineItem(float(x * self.square_size + 1),
                                                   float((y + 1) * self.square_size),
                                                   float((x + 1) * self.square_size - 1),
                                                   float((y + 1) * self.square_size))
                line.setPen(QtGui.QColor(255, 255, 255))
                line.setZValue(1)
                self.scene.addItem(line)

    def init_window(self):
        """
        Sets up the window.
        """
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Labyrinth')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.size * self.square_size, self.size * self.square_size)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    def input_windows(self):

        self.size, done1 = QtWidgets.QInputDialog.getInt(
            self, 'Input Dialog', 'Select the size of the labyrinth (e.g. typing in 10 means a 10x10 labyrinth):')

        difficulty = ['None', 'A few', 'Many', 'Max']
        weaves, done2 = QtWidgets.QInputDialog.getItem(
            self, 'Input Dialog', 'Select the amount of weaves:', difficulty)

        if done1 and done2:
            self.labyrinth = Labyrinth(self.size * self.size, weaves)
            self.labyrinth.create_graph()
            self.labyrinth.KruskalMST()


    def init_buttons(self):
        """
        Adds button which calls the solver class.
        Copied from robots.py code
        """
        self.solver_btn = QtWidgets.QPushButton("Show solution")
        self.solver_btn.clicked.connect(lambda: self.solver.printAllPaths(self.player.get_square(),
                                                                          self.ex.get_square()))
        self.horizontal.addWidget(self.solver_btn)

        self.save_lab = QtWidgets.QPushButton("Save labyrinth to a file")
        self.save_lab.clicked.connect(lambda: self.labyrinth.save_to_file())
        self.horizontal.addWidget(self.save_lab)

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
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() - int(self.size)):
                    self.player.location[1] -= self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(),
                                             self.player.get_square() - int(self.size) - int(self.size)):
                    self.player.location[1] -= self.square_size * 2
                    self.player_update_position()
        if event.key() == Qt.Key_S:
            if self.player.location[1] != (self.size - 1) * self.square_size:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + int(self.size)):
                    self.player.location[1] += self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(),
                                             self.player.get_square() + int(self.size) + int(self.size)):
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
            if self.player.location[0] != (self.size - 1) * self.square_size:
                if self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + 1):
                    self.player.location[0] += self.square_size
                    self.player_update_position()
                elif self.labyrinth.has_edge(self.player.get_square(), self.player.get_square() + 2):
                    self.player.location[0] += self.square_size * 2
                    self.player_update_position()
