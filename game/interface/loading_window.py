from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from game.enums.misc import Misc


class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("{} - {}".format(Misc.GameName.value, "Loading"))

        self.setFixedSize(500, 350)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel("Loading...")
        title_label.setObjectName("headingLbl")
        layout.addWidget(title_label)

        #self.progress = QProgressBar()
        #self.progress.setMinimum(0)
        #self.progress.setMaximum(0)

        layout.addWidget(title_label)
        #layout.addWidget(self.progress)
