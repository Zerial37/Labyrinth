import sys

from Graphics import Graphics
from PyQt5.QtWidgets import QApplication

"""
Running this will start the game.
The use app copied from RobotWorld
"""


def main():
    global app
    app = QApplication(sys.argv)
    Graphics(30)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
