import sys

from Graphics import Graphics
from PyQt5.QtWidgets import QApplication


def main():

    global app
    app = QApplication(sys.argv)
    graphics = Graphics()

    sys.exit(app.exec_())





if __name__ == "__main__":
    main()