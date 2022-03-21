import sys

from Graphics import Graphics
from PyQt5.QtWidgets import QApplication
from Labyrinth import Labyrinth
from Player import Player


def main():
    g = Labyrinth(100)
    g.create_graph()
    g.prims()

    global app
    app = QApplication(sys.argv)
    p = Player(30, g)
    graphics = Graphics(g, p, 30)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()