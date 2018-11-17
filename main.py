# General packages
from collections import deque
import numpy as np
# PyQt5
from PyQt5.QtWidgets import QApplication
import sys
import qdarkstyle
# My packages
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    openbci_gui = MainWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



