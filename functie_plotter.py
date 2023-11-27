import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
import numpy as np
from numpy import pi


# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        # Run the parent init
        super().__init__()

        # Create plot widget
        self.plot_widget = pg.PlotWidget()

        # Create central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical box and add plot widget
        vbox = QtWidgets.QVBoxLayout(central_widget)
        vbox.addWidget(self.plot_widget)

        # Add hbox for buttons
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        # Creating plot and clear buttons
        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)
        plot_button = QtWidgets.QPushButton("Plot")
        hbox.addWidget(plot_button)

        # Connect button signals to functions
        clear_button.clicked.connect(self.plot_widget.clear)
        plot_button.clicked.connect(self.plot)

    def plot(self):
        x = np.linspace(0, 2 * pi, 100)
        self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "k", "width": 5})
        self.plot_widget.setLabel("left", "sin(x)")
        self.plot_widget.setLabel("bottom", "x [radians]")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
