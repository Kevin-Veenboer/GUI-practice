import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from ui_simple_app import Ui_MainWindow


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.clear_button.clicked.connect(self.ui.textedit.clear)
        self.ui.add_text_button.clicked.connect(self.add_button_clicked)

        self.show()

    @Slot()
    def add_button_clicked(self):
        self.ui.textedit.append("You clicked me.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
