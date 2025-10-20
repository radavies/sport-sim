from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from game.enums.misc import Misc


class StartWindow(QWidget):
    def __init__(self, new_game_function):
        super().__init__()
        self.setWindowTitle(Misc.GameName.value)

        self.setFixedSize(500, 350)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel(Misc.GameNameWithEmoji.value)
        title_label.setObjectName("headingLbl")

        new_game_button = QPushButton("New Game 🆕")

        new_game_button.clicked.connect(new_game_function)

        #load_game_button = QPushButton("Load Game 💾")

        layout.addWidget(title_label)
        layout.addWidget(new_game_button)
        #layout.addWidget(load_game_button)
