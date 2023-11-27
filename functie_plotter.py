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

        # Create boxes for start, stop and number of points value
        start_box = QtWidgets.QDoubleSpinBox()
        stop_box = QtWidgets.QDoubleSpinBox()
        num_box = QtWidgets.QSpinBox()

        # Add boxes to hbox
        hbox.addWidget(start_box)
        hbox.addWidget(stop_box)
        hbox.addWidget(num_box)

        # set default values
        start_box.setValue(0)
        stop_box.setValue(2 * pi)
        num_box.setValue(100)

        # If value is changed
        start_box.valueChanged.connect(
            self.plot(start_box.value(), stop_box.value(), num_box.value())
        )
        stop_box.valueChanged.connect(
            self.plot(start_box.value(), stop_box.value(), num_box.value())
        )
        num_box.valueChanged.connect(
            self.plot(start_box.value(), stop_box.value(), num_box.value())
        )

    @Slot()
    def plot(self, start, stop, num_points):
        x = np.linspace(start, stop, num_points)
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
