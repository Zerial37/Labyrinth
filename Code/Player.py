from PyQt5 import QtWidgets
from PyQt5.Qt import Qt

class Player():
    def __init__(self):
        self.location = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_down:
            print("D")

        if event.key() == Qt.Key_Up:
            print("U")

        if event.key() == Qt.Key_Left:
            print("L")

        if event.key() == Qt.Key_Right:
            print("R")
