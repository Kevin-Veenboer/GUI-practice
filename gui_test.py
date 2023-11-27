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
        vbox = QtWidgets.QVBoxLayout(central_widget)

        # Makes an attribute for text display
        self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.textedit)

        # Add the hbox
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        # tHIRD BUTTON
        hello_button = QtWidgets.QPushButton("Hello World")
        vbox.addWidget(hello_button)

        # Make clear and add-text button
        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)
        add_text_button = QtWidgets.QPushButton("Add text")
        hbox.addWidget(add_text_button)

        # Something to do with signals?
        clear_button.clicked.connect(self.textedit.clear)
        add_text_button.clicked.connect(self.add_text_button_clicked)
        hello_button.clicked.connect(self.hello_world)

    @Slot()
    def add_text_button_clicked(self):
        self.textedit.append("KYS")

    @Slot()
    def hello_world(self):
        self.textedit.append("Hello World")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
