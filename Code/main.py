import sys

from Graphics import Graphics
from PyQt5.QtWidgets import QApplication
from Labyrinth import Labyrinth
from Player import Player


def main():
    g = Labyrinth(9)
    g.add_edge(0, 1)
    #g.add_edge(0, 3)
    g.add_edge(1, 2)
    #g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(3, 6)
    g.add_edge(4, 5)
    #g.add_edge(4, 7)
    #g.add_edge(5, 8)
    g.add_edge(6, 7)
    g.add_edge(7, 8)

    global app
    app = QApplication(sys.argv)
    p = Player(30, g)
    graphics = Graphics(g, p)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()