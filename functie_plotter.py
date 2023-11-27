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

        # If value is changed
        self.start_input.valueChanged.connect(self.plot)
        self.stop_input.valueChanged.connect(self.plot)
        self.num_input.valueChanged.connect(self.plot)

    @Slot()
    def plot(self):
        # clear old stuff first
        self.plot_widget.clear()

        # plotting
        x = np.linspace(
            self.start_input.value(), self.stop_input.value(), self.num_input.value()
        )
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
