import sys

from Graphics import Graphics
from PyQt5.QtWidgets import QApplication


def main():

    global app
    app = QApplication(sys.argv)
    graphics = Graphics(30)

    sys.exit(app.exec_())

if __name__ == "__main__":
    #https://www.youtube.com/watch?v=dmnA3axZ3FY
    import cProfile
    cProfile.run('main()', "output.dat")

    import pstats

    with open("output_time.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()
