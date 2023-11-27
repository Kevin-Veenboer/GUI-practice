import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        # Run the super init
        super().__init__()

        # Make central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # vertical stuff


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
