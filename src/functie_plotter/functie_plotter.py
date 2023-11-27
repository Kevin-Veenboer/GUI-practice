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
    """This describes the UserInterface class

    Args:
        QtWidgets.QMainWindow (class): parent class of the UserInterface class
    """

    def __init__(self):
        """This function creates the user interface"""
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

        # Add function selection box
        self.function_box = QtWidgets.QComboBox()
        self.function_box.addItems(
            ["sin(x)", "cos(x)", "tan(x)", "exp(x)", "X", "X^2", "X^3", "X^-1"]
        )
        vbox.addWidget(self.function_box)

        # Create Vbox for start value
        self.start_box = QtWidgets.QVBoxLayout()
        start_label = QtWidgets.QLabel("Start value")
        self.start_input = QtWidgets.QDoubleSpinBox()
        self.start_input.setRange(-50.0, 50.0)
        self.start_box.addWidget(start_label)
        self.start_box.addWidget(self.start_input)

        # Create Vbox for start value
        self.stop_box = QtWidgets.QVBoxLayout()
        stop_label = QtWidgets.QLabel("Stop value")
        self.stop_input = QtWidgets.QDoubleSpinBox()
        self.stop_input.setRange(-50.0, 50.0)
        self.stop_box.addWidget(stop_label)
        self.stop_box.addWidget(self.stop_input)

        # Create Vbox for start value
        self.num_box = QtWidgets.QVBoxLayout()
        num_label = QtWidgets.QLabel("Point value")
        self.num_input = QtWidgets.QSpinBox()
        self.num_input.setRange(0, 999)
        self.num_box.addWidget(num_label)
        self.num_box.addWidget(self.num_input)

        # Add boxes to hbox
        hbox.addLayout(self.start_box)
        hbox.addLayout(self.stop_box)
        hbox.addLayout(self.num_box)

        # set default values
        self.start_input.setValue(0)
        self.stop_input.setValue(2 * pi)
        self.num_input.setValue(100)

        # Plot with default values
        self.plot()

        # If value is changed of start, stop or number of points
        self.start_input.valueChanged.connect(self.plot)
        self.stop_input.valueChanged.connect(self.plot)
        self.num_input.valueChanged.connect(self.plot)

        # if selected function is changed
        self.function_box.currentTextChanged.connect(self.plot)

    @Slot()
    def plot(self):
        """This function handles the plotting of the selected function"""
        # clear old plot first
        self.plot_widget.clear()

        # check which function is selected and plot accordingly
        if self.function_box.currentText() == "sin(x)":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            self.plot_widget.plot(
                x, np.sin(x), symbol=None, pen={"color": "k", "width": 5}
            )
            self.plot_widget.setLabel("left", "sin(x)")
            self.plot_widget.setLabel("bottom", "x [radians]")

        elif self.function_box.currentText() == "cos(x)":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            self.plot_widget.plot(
                x, np.cos(x), symbol=None, pen={"color": "k", "width": 5}
            )
            self.plot_widget.setLabel("left", "cos(x)")
            self.plot_widget.setLabel("bottom", "x [radians]")

        elif self.function_box.currentText() == "tan(x)":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            self.plot_widget.plot(
                x, np.tan(x), symbol=None, pen={"color": "k", "width": 5}
            )
            self.plot_widget.setLabel("left", "tan(x)")
            self.plot_widget.setLabel("bottom", "x [radians]")

        elif self.function_box.currentText() == "exp(x)":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            self.plot_widget.plot(
                x, np.exp(x), symbol=None, pen={"color": "k", "width": 5}
            )
            self.plot_widget.setLabel("left", "exp(x)")
            self.plot_widget.setLabel("bottom", "x")

        elif self.function_box.currentText() == "X":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            self.plot_widget.plot(x, x, symbol=None, pen={"color": "k", "width": 5})
            self.plot_widget.setLabel("left", "x")
            self.plot_widget.setLabel("bottom", "x")

        elif self.function_box.currentText() == "X^2":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            f = lambda x: x**2
            self.plot_widget.plot(x, f(x), symbol=None, pen={"color": "k", "width": 5})
            self.plot_widget.setLabel("left", "x^2")
            self.plot_widget.setLabel("bottom", "x")

        elif self.function_box.currentText() == "X^3":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            f = lambda x: x**3
            self.plot_widget.plot(x, f(x), symbol=None, pen={"color": "k", "width": 5})
            self.plot_widget.setLabel("left", "x^3")
            self.plot_widget.setLabel("bottom", "x")

        elif self.function_box.currentText() == "X^-1":
            x = np.linspace(
                self.start_input.value(),
                self.stop_input.value(),
                self.num_input.value(),
            )
            self.plot_widget.plot(
                x,
                np.where(x != 0, 1 / x, 0),
                symbol=None,
                pen={"color": "k", "width": 5},
            )
            self.plot_widget.setLabel("left", "x^-1")
            self.plot_widget.setLabel("bottom", "x")


def main():
    """This function runs the application and creates an instance of the UserInterface class."""
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
